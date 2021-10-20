from flask import abort, Blueprint, render_template
from webapp.news.models import News
from webapp.settings import WEATHER_CITY_NAME
from webapp.weather import weather_by_city


blueprint = Blueprint('news', __name__)

@blueprint.route("/")
def index():
    title = 'Новости Python'
    weather = weather_by_city(WEATHER_CITY_NAME)
    news = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    return render_template(
        'news/index.html', 
        city_name=WEATHER_CITY_NAME, 
        page_title=title, 
        weather_text=weather, 
        news_list=news
    )

@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    if not my_news:
        abort(404)
    return render_template('news/single_news.html', page_title=my_news.title, news=my_news)
