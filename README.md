# Flask weather and news

Сервис показывать новости о языке Python и погоду.

### Установка

1. Клонировать репозиторий, создать виртуальное окружение
2. Установить зависимости `pip install -r requirements.txt`
3. В директории webapp cоздать файл settings.py со следующим содержанием:
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
    ```
4. Для корретной работы выполнить пункты:
    1. Создать -> create_db.py
    2. Получить новости -> get_all_news.py
    3. Создать учётную запись админа в базе -> create_admin.py

5. Команды для запуска сервиса
    ```
    set FLASK_APP=webapp 
    set FLASK_ENV=development 
    set FLASK_DEBUG=1 
    flask run
    ```