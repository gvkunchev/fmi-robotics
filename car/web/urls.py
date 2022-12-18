from django.urls import path
from web import views


urlpatterns = [
    path('', views.index),
    path('command', views.command),
    path('get_distance', views.get_distance)
]
