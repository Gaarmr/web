# Flask weather and news

Сервис показывает новости о языке Python и погоду.

### Установка

1. Клонировать репозиторий, создать виртуальное окружение
2. Установить зависимости `pip install -r requirements.txt`
3. Установить Redis https://github.com/MicrosoftArchive/redis/releases
4. В директории webapp cоздать файл settings.py со следующим содержанием:
    ```
    import os

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
    ```
    И добавить в него переменные:
    ```
    WEATHER_API_KEY='Ваш ключ API'
    WEATHER_CITY_NAME='Имя города'
    WEATHER_URL='http://api.worldweatheronline.com/premium/v1/weather.ashx'

    SECRET_KEY = ''

    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```
5. Для корретной работы выполнить пункты:
    1. Создать базу данных:
        set FLASK_APP=webapp
        $env:FLASK_APP = "webapp"
        flask db init
        flask db migrate -m ""
        flask db upgrade 

    2. Создать учётную запись админа в базе -> create_admin.py

6. Запуск
    1. Для запуска сервиса использовать run.bat
    2. Для запуска celery использовать run_celery.bat
    3. Для запуска задач использовать celery -A tasks beat