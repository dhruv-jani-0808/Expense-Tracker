from flask import Blueprint, render_template
from flask_login import login_required, current_user
from extensions import db
from models.expense_model import Expense
from models.category_model import Category
from datetime import date
from sqlalchemy import func, extract

# 1. Create the Blueprint
dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def index():
    today = date.today()

    # --- Query 1: Today's Total ---
    todays_expenses = Expense.query.filter_by(user_id=current_user.id, date=today).all()
    total_today = sum(expense.amount for expense in todays_expenses)

    # --- Query 2: This Month's Total ---
    this_month_expenses = Expense.query.filter(
        Expense.user_id == current_user.id,
        extract('month', Expense.date) == today.month,
        extract('year', Expense.date) == today.year
    ).all()
    total_month = sum(expense.amount for expense in this_month_expenses)

    # --- Query 3: Recent Transactions ---
    recent_expenses = Expense.query.filter_by(user_id=current_user.id)\
        .order_by(Expense.date.desc())\
        .limit(5).all()

    # --- Query 4: Chart Data (Group by Category) ---
    chart_data = db.session.query(
        Category.name, 
        func.sum(Expense.amount)
    ).join(Expense, Category.id == Expense.category_id)\
     .filter(Expense.user_id == current_user.id)\
     .group_by(Category.name).all()

    chart_labels = [row[0] for row in chart_data]
    chart_values = [row[1] for row in chart_data]

    return render_template(
        'dashboard/dashboard.html',
        total_today=total_today,
        total_month=total_month,
        recent_expenses=recent_expenses,
        chart_labels=chart_labels,
        chart_values=chart_values
    )