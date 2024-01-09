from django import forms
from models import User, Articles, Categories


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content', 'categories']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']