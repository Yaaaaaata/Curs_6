from django import forms

from blog.models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('slug', 'is_published', 'views')
