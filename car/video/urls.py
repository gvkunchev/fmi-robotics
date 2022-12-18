from django.urls import path
from video import views


urlpatterns = [
    path('video', views.video)
]
