from django.db import models
from django.urls import reverse

# Модель Message
class Message(models.Model):
    name = models.CharField(max_length=128, verbose_name="")
    email = models.EmailField(max_length=128, verbose_name="")
    subject = models.CharField(max_length=128, null=True, blank=True, verbose_name="")
    message = models.TextField(max_length=2800, verbose_name="")
    date = models.DateTimeField(auto_now_add=True)
    
    # Метод preview() модели Message, который возвращает начало статьи (предварительный просмотр)
    # длиной 124 символа и добавляет многоточие в конце.
    def preview(self):
        return f'{self.postText[:124]} ...'

    def __str__(self):
        # получить название поста
        return f'{self.name}..... {self.subject}..... {self.date}..... {self.message[:80]} .....'

    # def get_absolute_url(self):
    #     return f'http://127.0.0.1:8080'
    #     # return f'/news/{self.id}'
    def get_absolute_url(self):
        return reverse('website:home')  
