from django.urls import path 
from weblog.views import *
app_name='weblog'
urlpatterns = [
    path('',blog_view,name='blog_view'),
    path('single/',blog_single,name='blog_single')
]