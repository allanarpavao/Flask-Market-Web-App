from models.item import Item
from models import Session
from routes.forms import RegisterForm
from run import app
from flask import render_template


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Session.query(Item).all()
    return render_template('market.html', items=items)

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)