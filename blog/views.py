from django.shortcuts import render
from django.http import HttpResponse
def base_view(request):
    return render(request, 'blog/base.html',)
def services(request):
    return render(request,'blog/services.html')
def about(request):
    return render(request,'blog/about.html')
def team(request):
    return render(request,'blog/team.html')
def contact(request):
    return render(request, 'blog/contact.html')
def portfolio(request):
    return render(request,'blog/portfolio.html')
def testimonials(request):
    return render(request,'blog/testimonials.html')
def pricing(request):
    return render(request,'blog/pricing.html')