from django.urls import path 
from blog.views import *
app_name='blog'
urlpatterns = [
    path('',base_view,name='home'),
    path('services/',services,name='services'),
    path('about/',about,name='about'),
    path('team/',team,name='team'),
    path('contact/',contact,name='contact'),
    path('portfolio/',portfolio,name='portfolio'),
    path('testimonials/',testimonials,name='testimonials'),
    path('pricing/',pricing,name='pricing'),
]