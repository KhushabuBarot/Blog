from django import forms
from django .forms import ModelForm
from .models import Post


class AddPostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title', 'title_tag','author', 'body']

        widgets ={
               'title' : forms.TextInput(attrs={'class': 'form-control'}),
                'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
                'author' : forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'UserId' ,'type':'hidden'}),
                #'author' : forms.Select(attrs={'class': 'form-control'}),
                'body' : forms.Textarea(attrs={'class': 'form-control'}),
        
        }