from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from django.db import models
from PIL import Image

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True, related_name='profile')
    profile_image = models.ImageField(default='images/profile/default.jpeg', upload_to='images/profile')
    bio = models.TextField()
    position = models.CharField(max_length=120, null=True, blank=True)
    linkedin_url = models.CharField(max_length=120, null=True, blank=True)
    facebook_url = models.CharField(max_length=120, null=True, blank=True)
    whatsapp_url = models.CharField(max_length=120, null=True, blank=True)
    telegram_url = models.CharField(max_length=120, null=True, blank=True)
    twitter_url = models.CharField(max_length=120, null=True, blank=True)
    instagram_url = models.CharField(max_length=120, null=True, blank=True)   
    
    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_image.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.profile_image.path)

    def get_absolute_url(self):
        return reverse('users:profile')  
