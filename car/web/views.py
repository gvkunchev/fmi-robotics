from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .garage.car import Car


car = Car()


def index(request):
    return render(request, "index.html")


def command(request):
    if request.GET.get('parameter'):
        getattr(car, request.GET['name'])(request.GET['parameter'])
    else:
        getattr(car, request.GET['name'])()
    return HttpResponse('')

def get_distance(request):
    return JsonResponse({'distance': car.get_distance()})