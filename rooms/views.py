from django.shortcuts import render, redirect
from .forms import New_Room
from .models import Room

# Create your views here.
def new_room(request):
    context = {}
    context['form'] = New_Room()
    if request.method == 'POST':
        form = New_Room(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    return render(request,
                  'rooms/new_room.html',
                  context)


def get_all_rooms(request):
    return render(request, 'rooms/all_rooms.html', {'rooms': Room.objects.all()})


def get_room(request, room_name):
    return render(request, 'rooms/get_room.html', {'get_room': Room.objects.filter(name = room_name).first()})