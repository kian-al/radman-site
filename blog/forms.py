from django import forms
from blog.models import contact

class NameForm(forms.Form):
    name = forms.CharField( max_length=255 )
    email=forms.EmailField()
    subject=forms.CharField(max_length=255)
    massage=forms.CharField(widget=forms.Textarea)
    
class ContactForm(forms.ModelForm): 
    class Meta:
        model = contact
        fields = ['name', 'email','subject', 'message']
        