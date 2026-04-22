# routes/auth_routes.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

# Import your database and User model
from extensions import db
from models.user_model import User

# 1. Create the Blueprint (Think of this as creating the "Auth Department")
auth = Blueprint('auth', __name__)

# 2. The Register Route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    # If the user is already logged in, send them to the dashboard
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index')) # We will build dashboard later

    if request.method == 'POST':
        # Step 1: Grab the form data using request.form.get('input_name')
        # Step 2: Check if passwords match
        # Step 3: Check if the email already exists in the database
        # Step 4: Hash the password
        # Step 5: Create the new User object, add to db, and commit!
        # Step 6: Flash a success message and redirect to 'auth.login'        pass # Remove this pass when you add your code
        
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('auth.register'))
        
        existing_email = User.query.filter_by(email=email).first()
        existing_user = User.query.filter_by(username=username).first()

        if existing_email:
            flash('Email address already exists. Please log in.', 'warning')
            return redirect(url_for('auth.register'))
        
        if existing_user:
            flash('Username is already taken. Please choose another.', 'warning')
            return redirect(url_for('auth.register'))
        
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    # If it's a GET request, just show the page
    return render_template('auth/register.html')


# 3. The Login Route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        # Step 1: Grab email and password from the form
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Step 2: Query the database for a user with that email
        user = User.query.filter_by(email=email).first()

        # Step 3: Check if the user exists AND the password hash matches
        if(user and check_password_hash(user.password_hash, password)):
        # Step 4: If yes, use login_user() and redirect to dashboard
            login_user(user)
            flash('Logged in successfully!', 'success')
            
            return redirect(url_for('dashboard.index'))
        # Step 5: If no, flash an error message
        else:
            flash('Login Failed. Please check you email and password.', 'danger')
        

    return render_template('auth/login.html')


# 4. The Logout Route
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))