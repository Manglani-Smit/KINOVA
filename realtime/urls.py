from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('screen/<str:room_code>/', views.screen_view, name='screen'),
    path('controller/<str:room_code>/', views.controller_view, name='controller'),
    path('api/upload/', views.upload_file, name='upload_file'),
]