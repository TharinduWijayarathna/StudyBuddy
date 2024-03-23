from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'Let\'s learn Django'},
    {'id': 2, 'name': 'Let\'s learn React'},
    {'id': 3, 'name': 'Let\'s learn Python'},
    {'id': 4, 'name': 'Let\'s learn JavaScript'},
    {'id': 5, 'name': 'Let\'s learn HTML'},
    {'id': 6, 'name': 'Let\'s learn CSS'},
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request, 'base/room.html', context)
