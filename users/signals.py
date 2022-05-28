from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .models import Profile
from website.models import Message


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def profile_notify(sender, instance, created, **kwargs):
    ''' Signal to notify the user about changes of his profile settings '''
    subject = f'Hello, {instance.username}! Profile settings has been changed on RNG - Dashboard!' 
    body = f'Hello, {instance.username}! Profile settings on RNG - Dashboard has been changed!' 
    email = instance.email

    print("from RNG")
    print('--------------- \\ --------------')

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email='subscribecategory@yandex.ru',
        to=[email]  # это то же, что и recipients_list
    )
    
    # получаем наш html
    html_content = render_to_string(
        'registration/profile_email.html',
        {
            'profile': instance.profile,
            'body': body
        }
    )

    msg.attach_alternative(html_content, "text/html")  # добавляем html

    msg.send()  # отсылаем

    print("222")
    print('-------222-------- \\ -------222-------')


# @receiver(post_save, sender=Message)
# def message_notify(sender, instance, created, **kwargs):
#     ''' Signal to notify admins about new message from the site '''
#     subject = f'Hello, {instance.name}! Thanks for your message on RNG website!' 
#     body = f'Thanks { instance.name }! We received your message and will respond shortly...' 
#     email = instance.email
    
#     # subject=f'Message from: {instance.name}. - {instance.subject} -',
#     # body=f'Subject: {instance.subject} {instance.message}. Contact email: {instance.email}.  Name: {instance.name}',  #  это то же, что и message
#     # email = instance.email

#     print(subject)
#     print('--------------- \\ --------------')

#     #  отправляем на почту HTML-шаблон:
    
#     msg = EmailMultiAlternatives(
#         subject=subject,
#         body=body,
#         from_email='subscribecategory@yandex.ru',
#         to=["mikkapost@gmail.com" ] # это то же, что и recipients_list        
#     )

#     # получаем наш html
#     html_content = render_to_string('website/message_created.html', {'message': instance})
    
#     msg.attach_alternative(html_content, "text/html")  # добавляем html

#     msg.send()  # отсылаем

 





 
# # в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
# @receiver(post_save, sender=Appointment)
# def notify_managers_appointment(sender, instance, created, **kwargs):
#     if created:
#         subject = f'{instance.client_name} {instance.date.strftime("%d %m %Y")}'
#     else:
#         subject = f'Appointment changed for {instance.client_name} {instance.date.strftime("%d %m %Y")}'
 
#     mail_managers(
#         subject=subject,
#         message=instance.message,
#     )