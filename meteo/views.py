from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render

def index(request):
    context = {'name': 'Ksawery'}
    return render(request, 'main.html', context)