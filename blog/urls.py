from django.urls import path 
from blog.views import *
urlpatterns = [
    path('',index_view),
    path('about/',about_view),
    path('contacts/',contacts_view)
]
