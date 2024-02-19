from django import forms
from .models import DiscussionPost
from django_summernote.widgets import SummernoteWidget

# Same form as in the blog form 

class DiscussionPostForm(forms.ModelForm):
    class Meta:
        model = DiscussionPost
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }
