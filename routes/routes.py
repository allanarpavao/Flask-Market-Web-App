from models.item import Item
from models.user import User
from models import Session
from routes.forms import RegisterForm, LoginForm
from run import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Session.query(Item).all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password.data
        )
        Session.add(user_to_create)
        Session.commit()
        return redirect(url_for('market_page'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}',
                category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Session.query(User).filter_by(
            username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}',
                category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not a match! Please try again',
                category='danger')
    return render_template('login.html', form=form)
