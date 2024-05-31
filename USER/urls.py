from django.urls import path,include
from . import views

# urlpatterns = [
#     path('login/', views.user_login, name='login'),
   
# ]

# urls.py
from django.urls import path
from .views import (
    list_details_view, add_other_info, add_history, add_achieve,
    edit_other_info, edit_history, edit_achieve,
    delete_other_info, delete_history, delete_achieve
)

urlpatterns = [
    path('details/', list_details_view, name='list_details'),
    path('details/add/other_info/', add_other_info, name='add_other_info'),
    path('details/add/history/', add_history, name='add_history'),
    path('details/add/achieve/', add_achieve, name='add_achieve'),
    path('details/edit/other_info/<int:pk>/', edit_other_info, name='edit_other_info'),
    path('details/edit/history/<int:pk>/', edit_history, name='edit_history'),
    path('details/edit/achieve/<int:pk>/', edit_achieve, name='edit_achieve'),
    path('details/delete/other_info/<int:pk>/', delete_other_info, name='delete_other_info'),
    path('details/delete/history/<int:pk>/', delete_history, name='delete_history'),
    path('details/delete/achieve/<int:pk>/', delete_achieve, name='delete_achieve'),
    
    path('login/', views.user_login, name='login'),
    path('registration/', views.register, name='registartions'),
    path('ajax/load-courses/', views.load_courses, name='load_courses'),
    

    path('create_education/', views.create_educational_background, name='create_edu'),
]
