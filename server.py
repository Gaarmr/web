from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route("/")

def index():
    weather = weather_by_city('Nur-Sultan')
    #weather = False
    if weather:
        return f"Температура: {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        return 'Сервис временно недоступен'

if __name__=="__main__":
    app.run(debug=True)