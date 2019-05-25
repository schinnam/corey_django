from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Blog Home </h1>')

def about(request):
    return HttpResponse('<h2> This is an About Page </h2>')
