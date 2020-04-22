from flask import Blueprint, render_template

single_product_bp = Blueprint('single_product', __name__, template_folder='templates', static_folder='static')

@single_product_bp.route('/single_product')
def single_product():    
    return render_template('single_product.html')