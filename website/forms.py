from django import forms
from django.forms import ModelForm, BooleanField, widgets  # Импортируем true-false поле
from .models import Message

# Создаём модельную форму
class MessageForm(ModelForm):    
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. 
    class Meta:
        model = Message
        fields = ['name', 'phone', 'email', 'message'] 

        widgets = {
            'name': forms.TextInput(attrs={'type': "text", 'name': "name", 'class': "form-control", 'id': "name", 'placeholder': "Your Name", 'required': 'required'}),
            'phone': forms.TextInput(attrs={'type': "text", 'name': "phone", 'class': "form-control", 'id': "phone", 'placeholder': "Your Phone", 'required': 'required'}), 
            'email': forms.TextInput(attrs={'type': "email", 'name': "email", 'class': "form-control", 'id': "email", 'placeholder': "Your Email", 'required': 'required'}),
            'message': forms.Textarea(attrs={'name': "message", 'class': "form-control", 'rows': "5", 'placeholder': "Message"}),
        }

