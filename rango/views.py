from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   # html = 'smile Rnago says hey there partner yippee' + '<a href="/rango/about">
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

