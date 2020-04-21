from flask import Blueprint, render_template

payment_bp = Blueprint('payment_bp', __name__, template_folder='templates', static_folder='static')

@payment_bp.route('/payment')
def payment():    
    return 'Hello from the payment blueprint'