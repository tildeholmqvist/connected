from django import forms
from .models import DiscussionPost, Category, DiscussionComment 
from django_summernote.widgets import SummernoteWidget

class DiscussionPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = DiscussionPost
        fields = ['title', 'content', 'category']
        widgets = {
            'content': SummernoteWidget(),
        }


class DiscussionCommentForm(forms.Form):
    model = DiscussionComment
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )