from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from weblog.models import post
def blog_view (request):
    posts=post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'blog/blog.html',context)

def blog_single(request,pid):
    posts=post.objects.filter(status=1)
    post1=get_object_or_404(posts,pk=pid,status=1)
    context={'post':post1}
    return render(request,'blog/blog-single.html',context)
