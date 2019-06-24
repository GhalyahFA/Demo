import requests
from django.shortcuts import render


def home(request):
  
    offset = 0
    limit = 20
    base_url = 'https://pokeapi.co/api/v2/pokemon/?offset={0}?limit={1}'
    data = {}
    all_data =[]

    while offset < 960 :
        url = base_url.format(offset,limit )
        req = requests.get(url=url)
        out = req.json()
        data = out['results']
        all_data += data
        offset += limit

    
    sorted_data= sorted(all_data,key = lambda i: i['name'])


    context={
        'count': out['count'],
        'sorted_data': sorted_data,
    }

    return render(request, 'home.html', context)


def detail(request):
    if request.method == 'POST':
        poke_id = request.POST['name'] 
        base_url = 'https://pokeapi.co/api/v2/pokemon/{}'
        url = base_url.format(poke_id)
        req = requests.get(url=url)
        data = req.json()

    context = {
        'data' : data,
        'poke_id': poke_id,
    }

    return render(request, 'details.html', context)



