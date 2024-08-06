#weblog/views.py
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.core.cache import cache
from weblog.models import Post,Comments
from weblog.forms import CommentForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from datetime import datetime, time
from django.contrib import messages

def blog_view (request,**kwargs):
    posts = Post.objects.filter(status=1)
    
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])
        
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            similar_comment = Comments.objects.filter(
                post=post1,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            ).exists()
            
            if not similar_comment:
                form.save()
                messages.add_message(request, messages.SUCCESS, "کامنت شما به درستی ایجاد شد")
                return redirect('weblog:blog_single', pid=post1.id)  
            else:
                messages.add_message(request, messages.WARNING, "کامنت مشابهی قبلاً ثبت شده است.")
        else:
            messages.add_message(request, messages.ERROR, "کامنت شما به درستی ایجاد نشد")
         
    
    cache_key = f"comments_{post1.id}"
    comments = cache.get(cache_key)
    if not comments:
        comments = Comments.objects.filter(post=post1.id, approved=1)
        cache.set(cache_key, comments, timeout=60*15)  # کش برای 15 دقیقه
    form = CommentForm()
    context={'post':post1,
            'comments':comments,
            'form':form
            }
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
