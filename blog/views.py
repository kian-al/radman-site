from django.shortcuts import render
from django.http import HttpResponse
def index_view(request):
    return HttpResponse('<h1>this is homme page</h1>')
def about_view(request):
    return HttpResponse('<h1>this is about page</h1>')
def contacts_view(request):
    return HttpResponse('<h1>this is contacts page</h1>')