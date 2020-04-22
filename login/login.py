from flask import Blueprint, render_template

user_login_bp = Blueprint('user_login_bp', __name__, template_folder='templates', static_folder='static')

@user_login_bp.route('/user_login')
def user_login():    
    return render_template('login.html')