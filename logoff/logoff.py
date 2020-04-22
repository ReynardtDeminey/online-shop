from flask import Blueprint, render_template

user_logoff_bp = Blueprint('user_logoff_bp', __name__, template_folder='templates', static_folder='static')

@user_logoff_bp.route('/user_logoff')
def user_logoff():    
    return render_template('logoff.html')