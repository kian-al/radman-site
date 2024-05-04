from django.shortcuts import render
from django.http import HttpResponse
def index_view(request):
    return render(request,'blog/index.html')
def about_view(request):
    return render(request,'blog/about.html')
def contacts_view(request):
    return render(request,'blog/contacts.html')
