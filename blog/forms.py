from django import forms
from django import forms
from .models import Applications

class ApplicationsForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['mail', 'name', 'comment', 'subject']

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
