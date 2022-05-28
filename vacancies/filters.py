from django import forms
from django.forms import DateInput, SelectDateWidget
from django_filters import FilterSet, DateFromToRangeFilter,CharFilter, BooleanFilter    # импортируем filterset 
from django_filters.widgets import RangeWidget
from django.forms.widgets import TextInput 

from .models import Vacancy
 


class VacancyFilter(FilterSet):
    
    body = CharFilter(lookup_expr='icontains', widget=TextInput(attrs={'class':'form-control'}))

    # is_published = BooleanFilter(label='Опубликовано', widget=forms.CheckboxInput)
    # is_on_top = BooleanFilter(label='На главной странице', widget=forms.CheckboxInput)
    # body = CharFilter(field_name="Описание вакансии", lookup_expr='icontains', label='Описание вакансии', widget=TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Vacancy
        fields = ['body']





# создаём фильтр
class DashboardFilter(FilterSet):
    date_created = DateFromToRangeFilter(label='Даты создания вакансии', widget=RangeWidget(attrs={'type': 'date'}))
    title = CharFilter(lookup_expr='icontains', label='Название вакансии', widget=TextInput(attrs={'class':'form-control'}))
    body = CharFilter(lookup_expr='icontains', label='Описание вакансии', widget=TextInput(attrs={'class':'form-control'}))

    # is_published = BooleanFilter(label='Опубликовано', widget=forms.CheckboxInput)
    # is_on_top = BooleanFilter(label='На главной странице', widget=forms.CheckboxInput)
    # body = CharFilter(field_name="Описание вакансии", lookup_expr='icontains', label='Описание вакансии', widget=TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Vacancy
        fields = ['is_published', 'is_on_top']
        
        # fields = {
        #     'is_published': ['exact'], 
        #     'is_on_top': ['exact'],
        #     'title': ['icontains'],  # по названию публикации            
        #     'body': ['icontains'],  # по категории
        # }



# class BlogFilter(FilterSet):
#     start_date = DateFilter(field_name="created_at",lookup_expr='gte',label='From date',
#         widget=DateFromToRangeFilter(attrs={
#             'placeholder':'YYYY/MM/DD',
#             'class':'form-control'
#             })
#     )
#     end_date = DateFilter(field_name="created_at",lookup_expr='lte',label='To date')

#     blog_name = CharFilter(field_name="blog_name",lookup_expr='icontains',label='Blog Name',
#         widget=TextWidgets(attrs={
#             'class':'form-control'
#         })
#     )
#     class Meta:
#         model = Blog
#         fields = ('category','status','user')














    # is_published = BooleanFilter()
    
    # class Meta:
    #     model = Vacancy
    #     # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
    #     fields = {            
    #         'title': ['icontains'],  # по названию публикации            
    #         # 'is_published': ['exact'],  # по категории
    #     }
    

        

    # widgets = {
    #         'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'required': 'True'}),            
    #         'image': forms.Select(attrs={'class': 'form-control'}),
    #         'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}), 
    #         'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}), 
    #         'format': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Format'}), 
    #         'entryСontent': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entry Сontent'}),             
    #         'body': forms.Textarea(attrs={'class': 'form-control'}),
    #         'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags'})            
    #     }