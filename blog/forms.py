from django import forms
from blog.models import contact,Newsletter
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm): 
    captcha = CaptchaField()
    class Meta:
        model = contact
        fields = ['name', 'email','subject', 'message']
        
class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter 
        fields = ['email'] 