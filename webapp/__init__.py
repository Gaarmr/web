from flask import Flask, render_template
from webapp.model import db
from webapp.python_news import get_python_news
from webapp import settings
from webapp.weather import weather_by_city

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app) 

    @app.route("/")
    def index():
        title = 'Новости Python'
        weather = weather_by_city(settings.WEATHER_CITY_NAME)
        news = get_python_news()
        return render_template(
            'index.html', 
            city_name=settings.WEATHER_CITY_NAME, 
            page_title=title, 
            weather_text=weather, 
            news_list=news
        )
    return app