from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    print(current_user)
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Authorization'
    login_form = LoginForm()
    return render_template(
        'user/login.html', 
        page_title=title, 
        form=login_form
    )

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You have entered the site')
            return redirect(url_for('news.index'))
    flash('Invalid username or password')
    return redirect(url_for('user.login'))

@blueprint.route('/logout')
def logout():
    flash('Logout')
    logout_user()
    return redirect(url_for('news.index'))

@blueprint.route('/registration')
def registration():
    print(current_user)
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Registration'
    registartion_form = RegistrationForm()
    return render_template(
        'user/registration.html', 
        page_title=title, 
        form=registartion_form
    )

@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(user_name=form.user_name.data, email=form.email.data, role='user')
        new_user.set_password(form.reg_password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registered')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле "{getattr(form, field).label.text}": - {error}')
        return redirect(url_for('user.registration'))