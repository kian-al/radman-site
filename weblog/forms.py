from django import forms
from weblog.models import Comments
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm): 
    captcha = CaptchaField()
    class Meta:
        model = Comments
        fields = ['post','name','email','subject','message', 'captcha']
        