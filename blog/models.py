from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.name
    
    class Meta:
        ordering=["-created_date","updated_date"]
        verbose_name="درخواست مورد نظر"
        verbose_name_plural="پیام های ارتباط با ما"
        
class Newsletter(models.Model):
    email=models.EmailField()
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name="ایمیل مورد نظر"
        verbose_name_plural="ایمیل های اخرین اخبارها"
        
class Project(models.Model):
    image1=models.ImageField(upload_to="blog/",default="blog/image_file/new1.jpg",verbose_name="تصویر:")
    image2=models.ImageField(upload_to="blog/",default="blog/image_file/new1.jpg",verbose_name="تصویر:")
    image3=models.ImageField(upload_to="blog/",default="blog/image_file/new1.jpg",verbose_name="تصویر:")

    title=models.CharField(max_length=255,verbose_name="عنوان:")
    content= models.TextField(verbose_name="متن:")
    tag=TaggableManager(verbose_name="برچسب زدن:")
    status=models.BooleanField(verbose_name="وضعیت پست",default=False)
    client = models.CharField(max_length=255, verbose_name="اسم مشتری:", null=True, blank=True, default="")
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name="نویسنده:")
    counted_view=models.IntegerField(default=0,verbose_name="تعداد بازدید ها:")
    published_date=models.DateTimeField(default=timezone.now,verbose_name="تاریخ نشر:")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ساخت:")
    updated_date=models.DateTimeField(auto_now=True,verbose_name="تاریخ بروزرسانی:")
    
    def __str__(self) :
        return "title : {} - id : {}".format(self.title,self.id)
    
    class Meta:
        ordering = ["-created_date", "updated_date"]
        verbose_name="پروژه مورد"
        verbose_name_plural="پروژه ها"

    def __str__(self):
        return self.title
    


        
    

