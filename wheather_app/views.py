import datetime
import requests
from django.shortcuts import render


# Create your views here.


def index(request):
    API_KEY = open("/home/baratzade/Desktop/wheather_app_with_django/APIKEY","r").read()
    current_wheather_url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    fore_cast_url="https://api.openweathermap.org/data/2.5/onecall?latt={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
    if request.method=="POST":
        city_1=request.POST["city1"]
        city_2=request.POST.get("city2",None)

        wheater_data1,daily_forecasts_1=fetch_wheather_and_forecast(city_1,API_KEY,current_wheather_url,fore_cast_url)
        if city_2:
            wheater_data2,daily_forecasts_2=fetch_wheather_and_forecast(city_2,API_KEY,current_wheather_url,fore_cast_url)
        else:
            wheater_data2,daily_forecasts_2=None,None
        context={
            "wheater_data1":wheater_data1,
            "wheater_data2":wheater_data2,
            "daily_forecasts_1":daily_forecasts_1,
            "daily_forecasts_2":daily_forecasts_2
        }
        return render(request,"wheater_app/index.html",context)
    else:
        return render(request,"wheather_app/index.html")
    

def fetch_wheather_and_forecast(city,api_key,current_wheather_url,forecast_url):
    response=requests.get(current_wheather_url.format(city,api_key)).json()
    lat, lon=response['coord']['lat'],response['coord']['lon']
    forecast_response=requests.get(forecast_url.format(lat,lon,api_key)).json()
    wheater_data={
        "city":city,
        "temperature":round(response['main']["temp"]-273.15,2),
        "description":response["wheater"][0]["description"],
        "icon": response["weaher"][0]["icon"]

    }
    daily_forecasts=[]
    for daily_data in forecast_response["daily"][:5]:
        daily_forecasts.append({
            "day":datetime.datetime.fromtimestamp(daily_data["dt"]).strftime("%A"),
            "min_temp":round(daily_data["temp"]["min"]-273.15,2),
            "max_temp":round(daily_data["temp"]["max"]-273.15,2),
            "description":daily_data["wheater"][0]["description"],
            "icon":daily_data['wheater'][0]["icon"]
        })
    return wheater_data,daily_forecasts