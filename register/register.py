from flask import Blueprint, render_template

register_bp = Blueprint('register_bp', __name__, template_folder='templates', static_folder='static')

@register_bp.route('/register')
def register():    
    return render_template('register.html')