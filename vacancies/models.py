from datetime import datetime
import datetime
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core import validators

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from .formatChecker import ContentTypeRestrictedFileField



class Vacancy(models.Model):
    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    class Image(models.IntegerChoices):
        BLOG1 = 1
        BLOG2 = 2
        BLOG3 = 3
        BLOG4 = 4
        BLOG5 = 5
        BLOG6 = 6
        BLOG7 = 7
        BLOG8 = 8
        BLOG9 = 9

    title = models.CharField(max_length=160, verbose_name="Название")
    # slug = models.SlugField(max_length=50, db_index=True, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.IntegerField(choices=Image.choices, default=1, verbose_name="Выбор картинки для вакансии")
    location = models.CharField(max_length=30, blank=True, verbose_name="город - офис / удалённо")
    salary = models.CharField(max_length=30, blank=True)
    format = models.CharField(max_length=30, blank=True, verbose_name="Занятость / в штат")    
    entryСontent = RichTextField(blank=True, verbose_name="Краткое описание вакансии, проекта или клиента. / Превью.")
    body = RichTextField(blank=True, verbose_name="Полное описание вакансии: обязанности, требования, условия.")
    tags = models.TextField(blank=True)    
    date_created = models.DateTimeField(auto_now_add=True)    
    date_published = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    contacts = models.BooleanField(default=True, verbose_name="Указать контакты рекрутера")
    is_on_top = models.BooleanField(default=False, verbose_name="На главной странице")
    
    def __str__(self):
        return f'{self.title}  |  {self.author}  |  {self.date_created}  |  {self.date_published}  |  {self.is_published} |  {self.is_on_top}'

    def get_image(self):
        return f'website/assets/img/blog/blog-{self.image}.jpg'

    def publish(self):
        # self.date_published = datetime.now()
        self.is_published = True
        self.save()

    def save(self, *args, **kwargs):
        my_slug = self.title.translate(str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"))               
        self.slug = slugify(my_slug)    
        super(Vacancy, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('vacancies:dashboard_detail', kwargs={'pk': self.pk, 'slug': self.slug})  


# job application


class JobApplication(models.Model):
    class Meta:
        verbose_name = "Отклик на вакансию"
        verbose_name_plural = "Отклики на вакансию"

    vacancy = models.ForeignKey(Vacancy, related_name='job_applications', on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=30, null=True, blank=True)
    telegram_url = models.CharField(max_length=120, null=True, blank=True)
    whatsapp_url = models.CharField(max_length=120, null=True, blank=True)
    linkedin_url = models.CharField(max_length=120, null=True, blank=True)
    github_url = models.CharField(max_length=120, null=True, blank=True)
    cover_letter = models.TextField("Cover letter", null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=30, null=True, blank=True)
    # resume = models.FileField(upload_to='resumes/', verbose_name="Загрузить резюме*", help_text="Загрузить резюме в формате txt, doc, docx, pdf")
    resume = ContentTypeRestrictedFileField(upload_to='resumes/', 
                                            content_types=[
                                                'text/plain', 
                                                'application/pdf', 
                                                'application/msword', 
                                                'application/vnd.openxmlformats-officedocument.wordprocessingml.document' 
                                                ],
                                                max_upload_size=1310720,  
                                                verbose_name="Загрузить резюме*", 
                                                help_text="Загрузить резюме в формате txt, doc, docx, pdf") 
    # myfile = models.FileField(upload_to="uploads/", 
    #        validators=[validators.FileExtensionValidator(['txt', 'pdf', 'doc', 'docx'],
	#       message = 'myfile должен быть txt, doc, docx, pdf файл')], blank=True, null=True)  # Валидатор расширения файла(проверяет расширение, но не контент)

    def __str__(self):
        return f'{self.vacancy.title} - {self.first_name}- {self.last_name} - {self.date_added} - {self.email}'

    def get_fullName(self):
        return f'{self.first_name} {self.last_name}'
    
    # def approve(self):
    #     ''' approve response/comment '''
    #     self.approved_comment = True
    #     self.save()

    # def disapprove(self):
    #     ''' disapprove response/comment '''
    #     self.approved_comment = False
    #     self.save()

    # def get_absolute_url(self):
    #     return reverse('vacancies:vacancy_detail', kwargs={'pk': self.vacancy.pk, 'slug': self.vacancy.slug})  

    # def get_absolute_url(self):
    #     return reverse('vacancies:application_detail', kwargs={'pk': self.pk})  

    def get_absolute_url(self):
        # return reverse('vacancies:application_success', kwargs={'pk': self.pk})
        return reverse('vacancies:application_success', kwargs={'pk': self.vacancy.pk, 'slug': self.vacancy.slug})