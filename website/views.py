from django.shortcuts import render
from meetings.models import Meeting

# Create your views here.
def welcome(request):
    context = {}
    context['num_meetings'] = Meeting.objects.count()
    context['meetings'] = Meeting.objects.all()
    return render(request, 'website/welcome.html', context)