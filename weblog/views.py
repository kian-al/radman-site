from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from weblog.models import post,Category
def blog_view (request):
    posts=post.objects.filter(status=1)
    category = Category.objects.all()  
    context={'posts':posts,
             'category': category
             }
    return render(request,'blog/blog.html',context)

def blog_single(request,pid):
    posts=post.objects.filter(status=1)
    post1=get_object_or_404(posts,pk=pid,status=1)
    category = Category.objects.all() 
    context={'post':post1,
             'category': category
             }
    return render(request,'blog/blog-single.html',context)
