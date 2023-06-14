from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.
def index(request):
    return HttpResponse("Страница приложения women")

def categories(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<p>{cat}</p>')

def archive(request, year):
    if year > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
