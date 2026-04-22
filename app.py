from flask import Flask, redirect, url_for
from flask_login import current_user
from extensions import db, login_manager
import os

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'your-super-secret-key-change-this-later'
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # 1. Import Models
    from models.category_model import Category
    from models.expense_model import Expense
    from models.user_model import User

    # 2. Tell Flask-Login how to load the logged-in user
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # 3. Import and Register Blueprints
    from routes.auth_routes import auth
    from routes.dashboard_routes import dashboard
    from routes.expense_routes import expense
    from routes.category_routes import category

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(expense)
    app.register_blueprint(category)

    # 4. Root route — redirect to dashboard if logged in, else to login
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard.index'))
        return redirect(url_for('auth.login'))

    # 5. Create database tables if they don't exist yet
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)