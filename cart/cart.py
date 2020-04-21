from flask import Blueprint, render_template

cart_bp = Blueprint('cart_bp', __name__, template_folder='templates', static_folder='static')

@cart_bp.route('/cart')
def cart():    
    return render_template('cart.html')