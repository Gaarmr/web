from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import locale
import platform
from webapp.db import db
from webapp.news.models import News
from webapp.news.parsers.utils import get_html, save_news

# if platform.system() == 'Windows':
#     locale.setlocale(locale.LC_ALL, "russian")
# else:
#     locale.setlocale(locale.LC_TIME, 'ru_RU')

def parse_habr_date(date_str):
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str, '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()

def get_news_snippets():
    url = 'https://habr.com/ru/search/?q=python&target_type=posts&order=date'
    html = get_html(url)
    if html: 
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', class_='tm-articles-list').findAll('article', class_='tm-articles-list__item')
        for news in all_news:
            try:
                title = news.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').text
                url = news.find('a', class_='tm-article-snippet__title-link')['href']
                published = news.find('span', class_='tm-article-snippet__datetime-published').text
                published = parse_habr_date(published)
                #print(f'{title}, https://habr.com{url}, {published}')
                save_news(title, 'https://habr.com'+url, published)
            except AttributeError:
                print('Не удалось получить новость. AttributeError')

def get_news_content():
    news_without_text = News.query.filter(News.text.is_(None))
    for news in news_without_text:
        html = get_html(news.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            article = soup.find('div', class_='tm-article-body').decode_contents()
            #print(article)
            if article:
                news.text = article
                db.session.add(news)
                db.session.commit()
            