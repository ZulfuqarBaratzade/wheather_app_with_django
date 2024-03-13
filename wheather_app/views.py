import datetime
import requests
from django.shortcuts import render


# Create your views here.


def index(request):
    API_KEY = open("APIKEY.env","r").read()
    current_wheather_url="https://api.openwheathermap.org/data/2.5/wheather?q={}&appid={}"
    fore_cast_url="https://api.openwheathermap.org/data/2.5/onecall?latt={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
    if request.method=="POST":
        pass
    else:
        return render(request,"wheather_app/index.html")