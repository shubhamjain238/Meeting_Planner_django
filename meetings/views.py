from django.shortcuts import render, redirect
from .forms import New_meeting
from .models import Meeting

def new_meeting(request):
    if request.method == 'POST':
        form = New_meeting(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    return render(request, 'meetings/new_meeting.html', {'form': New_meeting()})

def get_meeting(request, meeting_title):
    return render(request, 'meetings/get_meeting.html', {'meeting': Meeting.objects.filter(title = meeting_title).first()})


def get_all(request):
    return render(request, 'meetings/get_all.html', {'meetings': Meeting.objects.all()})