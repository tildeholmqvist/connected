from django import forms
from .models import DiscussionPost, Category 
from django_summernote.widgets import SummernoteWidget

class DiscussionPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = DiscussionPost
        fields = ['title', 'content', 'category']
        widgets = {
            'content': SummernoteWidget(),
        }
