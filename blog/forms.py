from django import forms
from blog.models import contact,Newsletter
    
class ContactForm(forms.ModelForm): 
    class Meta:
        model = contact
        fields = ['name', 'email','subject', 'message']
        
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter 
        fields = ['email'] 