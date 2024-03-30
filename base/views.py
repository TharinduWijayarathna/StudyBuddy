from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def home(request):
    rooms = Room.objects.all() # Get all rooms from the database
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
