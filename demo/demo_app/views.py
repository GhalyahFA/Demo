from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/')
    pokemon = response.json()
    context={
        'count': pokemon['count'],
        'results': pokemon['results']
    }

    return render(request, 'home.html', context)
