from django import forms

from .models import ContactRequest, BlogPost

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = [
            'first_name', 'last_name', 'last_4_SSN', 'phone', 'email', 'comment'
            ]
        labels = {
            'first_name': 'First name', 'last_name': 'Last name', 
            'last_4_SSN': 'Last 4 digits of your SSN', 'phone': 'Phone', 
            'email': 'Email', 'comment': 'Comment'
            }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 80})
            }
        help_texts = {
            'email': 'A valid email address, please.',
            'comment': "Please briefly explain your issue, question, or concern."}

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Text'}
        widgets = {
            'title': forms.TextInput(attrs={'size': 60}),
            'text': forms.Textarea(attrs={'cols': 80})
            }