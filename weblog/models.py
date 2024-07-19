from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class post(models.Model):
    image=models.ImageField(upload_to="weblog/",default="weblog/image_file/p2.jpg")
    image_single_blog=models.ImageField(upload_to="weblog/",default="weblog/image_file/p2.jpg")
    title=models.CharField(max_length=255)
    content= models.TextField()
    #tag
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    counted_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    writer_image=models.ImageField(upload_to="weblog/",default="weblog/image_file/p2.jpg")
    writer_linkedin_account=models.URLField(default="https://www.linkedin.com/in/kian-almasi-0a4016256/")
    writer_summary=models.TextField()
    published_date=models.DateField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    def __str__(self) :
        return "title : {} - id : {}".format(self.title,self.id)
    
    class Meta:
        ordering = ["-created_date", "updated_date"]

    def __str__(self):
        return self.title
    
    
