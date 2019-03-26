from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message=forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5,'placeholder':'what is on your mind'}
        ),
        max_length=4000,
        help_text='The max length is 4000'   #It also handles help texts, which can be defined both in a Form class or in a Model class:
        )

    class Meta:
        model=Topic
        fields=['subject','message']