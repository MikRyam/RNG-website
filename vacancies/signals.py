import smtplib
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from django.core.mail import send_mail
from decouple import config

from .models import JobApplication



@receiver(post_save, sender=JobApplication)
def application_notify(sender, instance, created, **kwargs):
    ''' Signal to notify admins about new job application'''
    subject = f'Hello, new job application for {instance.vacancy.title}!' 
    body = f'Hello, new job application for {instance.vacancy.title}!\n\nName: {instance.first_name} {instance.last_name}\nContact email: {instance.email}'
    
    print("Starts sending email-application from RNG site")
    print(subject)
    print('--------------- \\ --------------')

    try:         
        send_mail( 
            subject=subject,
            message=body,
            from_email=config('from_email'), # здесь указываете почту, с которой будете отправлять        
            recipient_list=[config('recipient_1'), config('recipient_2'), config('recipient_4'), config('recipient_4')]  # здесь список получателей. Например, секретарь, сам врач и т. д.
        )
    except smtplib.SMTPDataError:
        print("Something went wrong")
        print("------  500  -------")
        pass  # ignore email errors 
    else:
        print("Status code: 200 or 302")
        print('-------200-------- \\ -------302-------')





    # msg = EmailMultiAlternatives(
    #     subject=subject,
    #     body=body,
    #     from_email='subscribecategory@yandex.ru',
    #     to=[email]  # это то же, что и recipients_list
    # )
    
    # # получаем наш html
    # html_content = render_to_string(
    #     'registration/profile_email.html',
    #     {
    #         'application': instance,
    #         # 'body': body
    #     }
    # )

    # msg.attach_alternative(html_content, "text/html")  # добавляем html

    # msg.send()  # отсылаем

    print(subject)
    print('-----200------ \\ ------200-----')


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