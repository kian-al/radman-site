from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from blog.forms import ContactForm,NewsletterForm
from django.contrib import messages
from blog.models import Project
def base_view(request):
    current_time = timezone.now()
    project=Project.objects.filter(status=1)
    context={'clock': current_time,
             'projects':project,
             }
    return render(request, 'blog/base.html',context)
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
            return redirect('blog:contact') 
        else:
            messages.add_message(request,messages.ERROR,"لطفا دوباره پیام خود را ارسال کنید پیام شما به درستی ارسال نشده")
            return redirect('blog:contact')

    else:
        form = ContactForm()
    return render(request, 'blog/contact.html',{'form':form})
def portfolio(request):
    project=Project.objects.filter(status=1)
    context={'projects':project,
             }
    return render(request,'blog/portfolio.html',context)
def portfolio_details(request,pid):
    project=Project.objects.filter(status=1)
    project1=get_object_or_404(project,pk=pid,status=1)
    context={'project':project1,
    }

    return render(request,'blog/portfolio-details.html',context)
def testimonials(request):
    return render(request,'blog/testimonials.html')
def NewsLetter(request):
    if request.method == 'POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"ایمیل شما به درستی دریافت شد ")
            return redirect('blog:home') 
        else:
            messages.add_message(request,messages.ERROR,"ایمیل شما به درستی ارسال نشده لطفا دوبارع ارسال کنید")
            return redirect('blog:home') 
    else:
        messages.add_message(request,messages.ERROR,"ایمیل شما به درستی ارسال نشده لطفا دوبارع ارسال کنید")
        return redirect('blog:home') 
    
    
    