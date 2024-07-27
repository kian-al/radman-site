from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from weblog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from datetime import datetime, time

def blog_view (request,**kwargs):
    posts = Post.objects.filter(status=1)
    
    if 'cat_name' in kwargs:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if 'author_username' in kwargs:
        posts = posts.filter(author__username=kwargs['author_username'])
        
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(1)

    for post in posts:
        if isinstance(post.published_date, datetime):
            post.published_datetime = post.published_date
        elif isinstance(post.published_date, date):
            post.published_datetime = datetime.combine(post.published_date, time.min)
        else:
            post.published_datetime = None

    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

def blog_single(request,pid):
    posts=Post.objects.filter(status=1)
    post1=get_object_or_404(posts,pk=pid,status=1)
    context={'post':post1}
    return render(request,'blog/blog-single.html',context)

def blog_category(request,cat_name):
    posts=Post.objects.filter(status=1,category__name=cat_name)
    context={'posts':posts,}
    return render(request,'blog/blog.html',context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        s = request.GET.get('s')
        if s:
            posts = posts.filter(content__icontains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)
