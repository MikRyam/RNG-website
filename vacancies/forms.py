from django import forms
from django.forms import ModelForm

from .models import Vacancy, JobApplication
from .formatChecker import ContentTypeRestrictedFileField


class VacancyForm(ModelForm):   
    ''' Form for creation Vacancy ''' 
    class Meta:
        model = Vacancy
        fields = ['title', 'image', 'location', 'salary', 'format', 'entryСontent', 'body', 'tags', 'contacts', 'is_on_top']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'required': 'True'}),            
            'image': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}), 
            'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}), 
            'format': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Format'}), 
            'entryСontent': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entry Сontent'}),             
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags'})            
        }

 
    
class VacancyEditForm(ModelForm):
    ''' Form for editing Vacancy ''' 
    class Meta:
        model = Vacancy
        fields = '__all__'

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),            
        #     'category': forms.Select(attrs={'class': 'form-control'}),       
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),            
        # }


class JobApplicationForm(ModelForm):
    ''' Form for creation response/comment '''     
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone', 'telegram_url', 'whatsapp_url', 'linkedin_url', 'github_url', 'resume', 'cover_letter', 'salary']
        # fields = '__all__' 

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя*', 'required': 'True'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия*', 'required': 'True'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': "email", 'placeholder': 'Email*', 'required': 'True'}), 
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон*', 'required': 'True'}), 
            'telegram_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telegram'}), 
            'whatsapp_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Whatsapp'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Профиль LinkedIn URL'}), 
            'github_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Профиль GitHub URL'}),             
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Комментарий'}),
            'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Уровень желаемой заработной платы'}),      
        }

# 'resume': forms.FileField(label='Загрузить резюме*'),   label='Загрузить резюме*'
# resume = forms.FileField(label='Загрузить резюме*', help_text = 'Загрузить резюме*')
# resume = forms.FileField(label='Загрузить резюме*', help_text = 'Загрузить резюме*', accept=".pdf,.doc")

            # 'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}), 
            # 'format': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Format'}), 
            # 'entryСontent': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entry Сontent'}),             
            # 'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags'})  
            # EmailField          attrs={'class': 'form-control', 'placeholder': 'Email*', 'required': 'True'}


        # widgets = {
        #     'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type comment text here ...'}),                        
        # }