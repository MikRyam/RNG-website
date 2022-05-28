import smtplib
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.core.mail import send_mail
from decouple import config

from website.models import Message


@receiver(post_save, sender=Message)
def new_message_notify(sender, instance, created, **kwargs):
    ''' Signal to notify admins about new message from site '''
    
    print("Starts sending email-message from RNG site")
    print('--------------- \\ --------------')

    try:         
        send_mail( 
                subject=f'Message from: {instance.name}. - {instance.subject}',
                message=f'Subject: {instance.subject}\n \n{instance.message}\n \nContact email: {instance.email}\nName: {instance.name}',
                from_email=config('from_email'), # здесь указываете почту, с которой будете отправлять        
                recipient_list=[config('recipient_1'), config('recipient_2'), config('recipient_4'), config('recipient_4')]    
            )
    except smtplib.SMTPDataError:
        print("Something went wrong")
        print("------  500  -------")
        pass  # ignore email errors 
    else:
        print("Status code: 200 or 302")
        print('-------200-------- \\ -------302-------')
