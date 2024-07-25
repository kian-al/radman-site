from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from blog.forms import ContactForm,NewsletterForm
from django.contrib import messages
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
            messages.add_message(request,messages.SUCCESS,"پیام شما دریافت شد متخصصان ما در اسرع وقت با شما تماس میگیرند ")
        else:
            messages.add_message(request,messages.ERROR,"لطفا دوباره پیام خود را ارسال کنید پیام شما به درستی ارسال نشده")

    else:
        form = ContactForm()
    return render(request, 'blog/contact.html',{'form':form})
def portfolio(request):
    return render(request,'blog/portfolio.html')
def portfolio_details(request):
    return render(request,'blog/portfolio-details.html')
def testimonials(request):
    return render(request,'blog/testimonials.html')
def NewsLetter(request):
    if request.method == 'POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
    
    