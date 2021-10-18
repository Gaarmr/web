from bs4 import BeautifulSoup
from datetime import datetime
import requests
from webapp.db import db
from webapp.news.models import News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status
        return result.text
    except(requests.RequestException, ValueError):
        print('Network Error. python_news')
        return False

def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
        
def get_python_news():
    url = 'https://www.python.org/blogs/'
    html = get_html(url)
    if html: 
        soup = BeautifulSoup(html, 'html.parser')
        news_list = soup.find('ul', class_='list-recent-posts').find_all('li')
        #print(news_list)
        for news in news_list:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time')['datetime']
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)