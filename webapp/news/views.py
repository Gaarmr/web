from flask import Blueprint, render_template
from webapp.news.models import News
from webapp.settings import WEATHER_CITY_NAME
from webapp.weather import weather_by_city


blueprint = Blueprint('news', __name__)

@blueprint.route("/")
def index():
    title = 'Новости Python'
    weather = weather_by_city(WEATHER_CITY_NAME)
    news = News.query.order_by(News.published.desc()).all()
    return render_template(
        'news/index.html', 
        city_name=WEATHER_CITY_NAME, 
        page_title=title, 
        weather_text=weather, 
        news_list=news
    )