from django import forms
from .models import ContactPageForm

class ContactFormDB(forms.ModelForm):
    class Meta:
        model = ContactPageForm
        fields = ('subject', 'name',  'email', 'message')

        widgets = {
            'subject': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Предмет сообщения'
            }),
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Имя'
            }),
        
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Сообщение'
            }), 
        }