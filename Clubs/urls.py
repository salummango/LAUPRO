from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Clubs'
urlpatterns = [
    path('club_list/', views.club_list, name='club_list'),
    path('clubs/<int:pk>/', views.club_detail_view, name='club_detail'),
    # path('post_list/<int:club_id>/', views.post_list, name='post_list'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('add_comment/<int:post_id>/', views.add_comment, name='comment'),
    # Define URLs for other views
    path('club_view/<int:club_id>/', views.view_club, name='view_club'),
    path('join_club/<int:club_id>/', views.join_club, name='join_club'),
    path('club/<int:club_id>/post/<int:post_id>/', views.view_post, name='view_post'),
    # jh
    path('clubs/<int:club_id>/post/', views.create_post, name='create_post'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
