from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['profile_photo', 'name', 'where_do_you_work', 'what_do_you_do', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'John Doe'}),
            'where_do_you_work': forms.TextInput(attrs={'placeholder': 'Google Inc. (optional)'}),
            'what_do_you_do': forms.TextInput(attrs={'placeholder': 'Software Engineer'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Enter your comment'}),
        }
