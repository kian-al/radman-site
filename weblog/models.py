#weblog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,verbose_name="اسم دسته بندی :")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="دسته بندی "
        verbose_name_plural="دسته بندی ها"


class Post(models.Model):
    image=models.ImageField(upload_to="weblog/",default="weblog/image_file/p2.jpg",verbose_name="تصویر بالای متن:")
    image_single_blog=models.ImageField(upload_to="weblog/",default="weblog/image_file/p2.jpg",verbose_name="تصویر پایین متن:")
    title=models.CharField(max_length=255,verbose_name="عنوان پست:")
    content= models.TextField(verbose_name="متن:")
    tag=TaggableManager(verbose_name="برچسب زدن:")
    category=models.ManyToManyField(Category,verbose_name="دسته بندی:")
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name="نویسنده:")
    counted_view=models.IntegerField(default=0,verbose_name="تعداد بازدید ها:")
    status=models.BooleanField(verbose_name="وضعیت پست",default=False)
    writer_image=models.ImageField(upload_to="weblog/",default="weblog/image_file/p2.jpg",verbose_name="عکس نویسنده:")
    writer_linkedin_account=models.URLField(default="https://www.linkedin.com/in/kian-almasi-0a4016256/",verbose_name="آدرس حساب کاربری لینکدین نویسنده:")
    writer_summary=models.TextField(verbose_name="درباره نویسنده:")
    published_date=models.DateTimeField(default=timezone.now,verbose_name="تاریخ نشر پست:")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ساخت پست:")
    updated_date=models.DateTimeField(auto_now=True,verbose_name="تاریخ بروزرسانی پست:")
    def __str__(self) :
        return "title : {} - id : {}".format(self.title,self.id)
    
    class Meta:
        ordering = ["-created_date", "updated_date"]
        verbose_name="پست مورد"
        verbose_name_plural="پست ها"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('weblog:blog_single',kwargs={'pid':self.id})
    
class Comments(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="اسم پست:")
    name=models.CharField(max_length=255,verbose_name="اسم:")
    email=models.EmailField(verbose_name="ایمیل:")
    subject=models.CharField(max_length=255,verbose_name="موضوع:")
    message=models.TextField(verbose_name="پیام:")
    approved=models.BooleanField(default=False,verbose_name="تایید شده است:")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ساخت:")
    updated_date=models.DateTimeField(auto_now=True,verbose_name="تاریخ بروزرسانی:")
    
    def __str__(self) :
        return self.name
    
    class Meta:
        ordering=['-created_date']
        verbose_name="نظر مورد"
        verbose_name_plural="نظر ها"
    
    
    
