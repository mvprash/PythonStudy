from flask import Blueprint, render_template,request,redirect,url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.username)

@main.route('/newWorkout')
@login_required
def new_workout():
    return render_template('create_workout.html')

@main.route('/newWorkout', methods=['POST'])
@login_required
def new_workout_post():
    pushups=request.form.get('pushups')
    comments=request.form.get('comments')
    print(pushups, comments)
    return redirect(url_for('main.index'))