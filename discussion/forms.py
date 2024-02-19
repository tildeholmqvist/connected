from django import forms
from .models import DiscussionPost
from django_summernote.widgets import SummernoteWidget

class DiscussionPostForm(forms.ModelForm):
    class Meta:
        model = DiscussionPost
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }
