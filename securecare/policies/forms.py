from django import forms
from .models import Policy,Quiz

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['title', 'category', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class QuizForm(forms.ModelForm):
    class Meta:
        model  = Quiz
        fields = ['policy', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'option_a': forms.TextInput(attrs={'class': 'form-control'}),
            'option_b': forms.TextInput(attrs={'class': 'form-control'}),
            'option_c': forms.TextInput(attrs={'class': 'form-control'}),
            'option_d': forms.TextInput(attrs={'class': 'form-control'}),
            'correct_option': forms.Select(attrs={'class': 'form-control'}),
            'policy': forms.Select(attrs={'class': 'form-control'}),
        }