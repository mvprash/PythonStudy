from flask  import Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email=request.form.get('email')
    name=request.form.get('name')
    password=request.form.get('password')
    
    print(email, name, password)    
    user=User.query.filter_by(email=email).first()
    if user:
        print('User already exists')
        return redirect(url_for('auth.signup'))
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user=User(email=email, username=name, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()


    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email=request.form.get('email')
    password=request.form.get('password')
    remember=True if request.form.get('remember') else False
    user=User.query.filter_by(email=email).first()
    if not user:
        print('User does not exist')
        return redirect(url_for('auth.login'))
    if not check_password_hash(user.password, password):
        print('Password is incorrect')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)    
    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))