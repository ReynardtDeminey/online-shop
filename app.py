from flask import Flask, render_template

from home.home import home_bp
from cart.cart import cart_bp
from login.login import user_login_bp
from payment.payment import payment_bp
from register.register import register_bp
from single_product.single_product import single_product_bp
from logoff.logoff import user_logoff_bp

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(cart_bp, url_prefix='/')
app.register_blueprint(user_login_bp, url_prefix='/')
app.register_blueprint(payment_bp, url_prefix='/')
app.register_blueprint(register_bp, url_prefix='/')
app.register_blueprint(single_product_bp, url_prefix='/')
app.register_blueprint(user_logoff_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
