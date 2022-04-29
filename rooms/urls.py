from django.urls import path
from .views import new_room, get_all_rooms, get_room
urlpatterns = [
    path('new/', new_room, name = 'new_room'),
    path('get_all', get_all_rooms, name='get_all_rooms'),
    path('get/<str:room_name>', get_room, name='get_room'),
]