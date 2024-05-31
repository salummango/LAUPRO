from django.urls import path
from . import views

app_name = 'AlumniEvents'
urlpatterns = [
    path('eventlist/', views.event_list, name='lists'),
    path('create/', views.create_event, name='create_event'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    
    # path('events/', views.events, name='event_calendar'),
    # path('eventcalendar/', views.event_calendar, name='event_calendar'),
]
