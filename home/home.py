from flask import Blueprint, render_template, url_for

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='static')

@home_bp.route('/')
def home():    
    is_logged_in = False

    return render_template('home.html', is_logged_in = is_logged_in)