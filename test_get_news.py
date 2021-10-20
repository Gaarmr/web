from webapp import create_app
from webapp.news.parsers.habr import get_news_snippets

app = create_app()
with app.app_context():
    get_news_snippets()