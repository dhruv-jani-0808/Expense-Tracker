from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime

from extensions import db
from models.expense_model import Expense
from models.category_model import Category

expense = Blueprint('expense', __name__)

# --- Route 1: View All Expenses ---
@expense.route('/expenses')
@login_required
def index():
    expenses = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).all()
    categories = Category.query.filter_by(user_id=current_user.id).all()
    return render_template('expenses/expenses.html', expenses=expenses, categories=categories)


# --- Route 2: Add an Expense ---
@expense.route('/add-expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    categories = Category.query.filter_by(user_id=current_user.id).all()

    if request.method == 'POST':
        amount = request.form.get('amount')
        description = request.form.get('description')
        category_id = request.form.get('category')
        date_string = request.form.get('date')

        expense_date = datetime.strptime(date_string, '%Y-%m-%d').date() if date_string else datetime.today().date()

        new_expense = Expense(
            amount=float(amount),
            description=description,
            date=expense_date,
            user_id=current_user.id,
            category_id=category_id
        )

        db.session.add(new_expense)
        db.session.commit()

        flash('Expense added successfully!', 'success')
        return redirect(url_for('expense.index'))

    return render_template('expenses/add_expense.html', categories=categories, legend='Add', expense=None)


# --- Route 3: Edit an Expense ---
@expense.route('/edit-expense/<int:expense_id>', methods=['GET', 'POST'])
@login_required
def edit_expense(expense_id):
    expense_to_edit = Expense.query.get_or_404(expense_id)

    if expense_to_edit.user_id != current_user.id:
        flash('You are not authorized to edit this expense.', 'danger')
        return redirect(url_for('expense.index'))

    categories = Category.query.filter_by(user_id=current_user.id).all()

    if request.method == 'POST':
        expense_to_edit.amount = float(request.form.get('amount'))
        expense_to_edit.description = request.form.get('description')
        expense_to_edit.category_id = request.form.get('category')
        
        date_string = request.form.get('date')
        if date_string:
            expense_to_edit.date = datetime.strptime(date_string, '%Y-%m-%d').date()

        db.session.commit()
        flash('Expense updated successfully!', 'success')
        return redirect(url_for('expense.index'))

    return render_template('expenses/add_expense.html', categories=categories, legend='Update', expense=expense_to_edit)


# --- Route 4: Delete an Expense ---
@expense.route('/delete-expense/<int:expense_id>', methods=['POST'])
@login_required
def delete_expense(expense_id):
    expense_to_delete = Expense.query.get_or_404(expense_id)

    if expense_to_delete.user_id == current_user.id:
        db.session.delete(expense_to_delete)
        db.session.commit()
        flash('Expense deleted successfully.', 'info')
    else:
        flash('You are not authorized to delete this expense.', 'danger')

    return redirect(url_for('expense.index'))