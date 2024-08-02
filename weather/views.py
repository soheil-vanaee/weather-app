from django.shortcuts import render
import requests

def home(request):
    return render(request, 'weather/home.html')

def index(request):
    api_key = 'c7be2bae3fcdc0529d1d02d7ff1cac9c'
    city = request.GET.get('city', 'London')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    context = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
    }
    return render(request, 'weather/index.html', context)

def contact(request):
    return render(request, 'weather/contact.html')
