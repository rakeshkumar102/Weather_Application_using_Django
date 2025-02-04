import requests
from django.shortcuts import render
from weather.models import *
from weather.forms import *

# Create your views here.
def weather(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city='Bengaluru'

    if request.method == 'POST':
        
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities=City.objects.all()
    
    weather_data=[]

    for city in cities:

        r = requests.get(url.format(city)).json()
    
        
        city_weather = {
            'city':city.name,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)
    
    context={'weather_data' : weather_data, 'form' : form}
    return render(request,'weather.html',context)