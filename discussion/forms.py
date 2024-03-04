from django import forms
from .models import DiscussionPost, DiscussionComment
from django_summernote.widgets import SummernoteWidget


class DiscussionPostForm(forms.ModelForm):
    class Meta:
        model = DiscussionPost
        fields = ['title', 'content', ]
        widgets = {
            'content': SummernoteWidget(),
        }


class DiscussionCommentForm(forms.ModelForm):
    class Meta:
        model = DiscussionComment
        fields = ['body']
        widgets = {
                'body': forms.Textarea(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Leave a comment!"})}
