from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


# Create your views here.

def get_stations(request):
    return HttpResponse(f"get station ids endpoint.")

def get_data(request, station_id):
    # use a handler here
    return HttpResponse(f"stationId:{station_id}\nget data endpoint.")


def post_data(request, station_id):
    # use a handler here
    return HttpResponse(f"stationId:{station_id}\npost data endpoint.")
