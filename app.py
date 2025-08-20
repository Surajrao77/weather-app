from fastapi import FastAPI
import requests
import os

app=FastAPI()
key=os.getenv("OPENWEATHER_API_KEY")


@app.get('/weather/{city}')
def weather(city):
    
    cord_url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={key}"
    cord_data=requests.get(cord_url).json()
    lat=cord_data[0]['lat']
    lon=cord_data[0]['lon']

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"
    weather_data=requests.get(weather_url).json()
    return {
        "city": city,
        "temperature": weather_data['main']['temp'],
        "weather": weather_data['weather'][0]['description']
    }
