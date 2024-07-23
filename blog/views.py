from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from blog.models import contact
from blog.forms import NameForm,ContactForm
def base_view(request):
    current_time = timezone.now()
    return render(request, 'blog/base.html', {'clock': current_time})
def services(request):
    return render(request,'blog/services.html')
def about(request):
    return render(request,'blog/about.html')
def  team(request):
    return render(request,'blog/team.html')
def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html',{'form':form})
def portfolio(request):
    return render(request,'blog/portfolio.html')
def portfolio_details(request):
    return render(request,'blog/portfolio-details.html')
def testimonials(request):
    return render(request,'blog/testimonials.html')

