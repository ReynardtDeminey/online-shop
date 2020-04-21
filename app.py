from flask import Flask, render_template

from home.home import home_bp
from cart.cart import cart_bp
from login.login import login_bp
from payment.payment import payment_bp

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(cart_bp, url_prefix='/')
app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(payment_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
