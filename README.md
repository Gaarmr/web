# Flask weather and news

Сервис показывать новости о языке Python и погоду.

### Установка

1. Клонировать репозиторий, создать виртуальное окружение
2. Установить зависимости `pip install -r requirements.txt`
3. В директории webapp cоздать файл settings.py и добавить него переменные:
    ```
    WEATHER_API_KEY='Ваш ключ API'
    WEATHER_CITY_NAME='Имя города'
    WEATHER_URL='http://api.worldweatheronline.com/premium/v1/weather.ashx'
    ```
4. Для запуска сервиса используйте команды 
    ```
    set FLASK_APP=webapp 
    set FLASK_ENV=development 
    set FLASK_DEBUG=1 
    flask run
    ```