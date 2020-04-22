from flask import Blueprint, render_template

cart_bp = Blueprint('cart_bp', __name__, template_folder='templates', static_folder='static')

@cart_bp.route('/cart')
def cart(): 
    is_logged_in = False

    return render_template('cart.html', is_logged_in=is_logged_in)