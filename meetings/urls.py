from django.urls import path
from .views import new_meeting, get_meeting, get_all
urlpatterns = [
    path('new/', new_meeting, name = 'new_meeting'),
    path('get/<str:meeting_title>', get_meeting, name = 'get_meeting'),
    path('get_all', get_all, name='get_all_meetings')
]