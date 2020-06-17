from django import forms
from .models import Article_2

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article_2
        fields = ['title','content',]
        