from celery import Celery
from celery.schedules import crontab
from webapp import create_app
from webapp.news.parsers.habr import get_news_snippets, get_news_content

flask_app = create_app()

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def habr_snippets():
    with flask_app.app_context():
        get_news_snippets()


@app.task
def habr_content():
    with flask_app.app_context():
        get_news_content()

app.conf.beat_schedule = {
    'get_news_snippets': {
        'task': 'tasks.habr_snippets', 
        'schedule': crontab(minute="*/1")
    },
    'get_news_content': {
        'task': 'tasks.habr_content', 
        'schedule': crontab(minute="*/1")
    }
}


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(crontab(minute='*/1'), habr_snippets.s())
#     sender.add_periodic_task(crontab(minute='*/2'), habr_content.s())