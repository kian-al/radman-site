from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from weblog.models import post
def blog_view (request,**kwargs):
    posts=post.objects.filter(status=1)
    if kwargs.get('cat_name')  != None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts=posts.filter(author__username=kwargs['author_username'])   
    context={'posts':posts}
    return render(request,'blog/blog.html',context)

def blog_single(request,pid):
    posts=post.objects.filter(status=1)
    post1=get_object_or_404(posts,pk=pid,status=1)
    context={'post':post1}
    return render(request,'blog/blog-single.html',context)

def blog_category(request,cat_name):
    posts=post.objects.filter(status=1,category__name=cat_name)
    context={'posts':posts,}
    return render(request,'blog/blog.html',context)

def blog_search(request):
    posts = post.objects.filter(status=1)
    if request.method == 'GET':
        s = request.GET.get('s')
        if s:
            posts = posts.filter(content__icontains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)
