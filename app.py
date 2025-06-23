from flask import Flask, render_template, request
import requests
import var
import os
import mysql.connector

app = Flask(__name__)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            return None
    except Exception as e:
        return None

def save_to_db(city, weather_data):
    try:
        conn = mysql.connector.connect(
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS"),
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME")
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO weather (city, temperature, description) VALUES (%s, %s, %s)",
            (city, weather_data['main']['temp'], weather_data['weather'][0]['description'])
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Database error:", e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = var.key
        weather_data = get_weather(api_key, city)
        if weather_data:
            save_to_db(city, weather_data)
        return render_template('index.html', weather_data=weather_data)
    return render_template('index.html', weather_data=None)

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)
