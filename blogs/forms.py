from django import forms
from .models import BlogPost



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '帖子主题', 'text': '帖子内容'}
        widgets = {'title': forms.Textarea(attrs={'cols': 40, 'rows': 1}), 'text': forms.Textarea(attrs={'cols': 80})}