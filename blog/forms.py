from django.shortcuts import get_object_or_404, redirect
from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        widgets = {
            'content': SummernoteWidget(),
        }


class CommentForm(forms.Form):
    # author = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "Your Name"}
    #     ),
    # )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )