from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from webapp.forms import LoginForm
from webapp.model import db, News, User
from webapp import settings
from webapp.weather import weather_by_city

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index():
        title = 'Новости Python'
        weather = weather_by_city(settings.WEATHER_CITY_NAME)
        news = News.query.order_by(News.published.desc()).all()
        return render_template(
            'index.html', 
            city_name=settings.WEATHER_CITY_NAME, 
            page_title=title, 
            weather_text=weather, 
            news_list=news
        )

    @app.route('/login')
    def login():
        print(current_user)
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Authorization'
        login_form = LoginForm()
        return render_template(
            'login.html', 
            page_title=title, 
            form=login_form
        )

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(user_name=form.user_name.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash('You have entered the site')
                return redirect(url_for('index'))
        flash('Invalid username or password')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        flash('Logout')
        logout_user()
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Admin'
        else:
            return 'Not админ!'

    return app