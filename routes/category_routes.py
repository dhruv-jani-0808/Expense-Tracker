from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from extensions import db
from models.category_model import Category

category = Blueprint('category', __name__)

# --- Route 1 & 2: View and Add Categories ---
@category.route('/categories', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        
        existing_category = Category.query.filter_by(name=name, user_id=current_user.id).first()
        
        if existing_category:
            flash(f'Category "{name}" already exists.', 'warning')
        elif name:
            new_category = Category(name=name, user_id=current_user.id)
            db.session.add(new_category)
            db.session.commit()
            flash('Category added successfully!', 'success')
            
        return redirect(url_for('category.index'))

    categories = Category.query.filter_by(user_id=current_user.id).all()
    return render_template('categories/categories.html', categories=categories)


# --- Route 3: Delete a Category ---
@category.route('/delete-category/<int:category_id>', methods=['POST'])
@login_required
def delete_category(category_id):
    category_to_delete = Category.query.get_or_404(category_id)

    if category_to_delete.user_id == current_user.id:
        try:
            db.session.delete(category_to_delete)
            db.session.commit()
            flash('Category deleted successfully.', 'info')
        except:
            db.session.rollback()
            flash('Cannot delete this category because it is attached to existing expenses.', 'danger')
    else:
        flash('You are not authorized to delete this category.', 'danger')

    return redirect(url_for('category.index'))