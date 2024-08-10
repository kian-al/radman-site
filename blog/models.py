from django.db import models

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
        
    

