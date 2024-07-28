#weblog/urls.py
from django.urls import path 
from weblog.views import *
app_name='weblog'
urlpatterns = [
    path('',blog_view,name='blog_view'),
    path('<int:pid>',blog_single,name='blog_single'),
    path('category/<str:cat_name>/', blog_view, name='category'),
    path('author/<str:author_username>/', blog_view, name='author'),
    path('search/',blog_search, name='search')
    
]