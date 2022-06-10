from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
# from decouple import config

from website.models import Message
from website.forms import MessageForm 
from vacancies.models import Vacancy


def home(request):
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            # message_form.save()
            message = message_form.save()
            message.save()
            name = message.name[:30]

            # messages.add_message(request, messages.SUCCESS, f'Thanks {name}! I received your message and will respond shortly...')

        # Все отправления писем через website.signals

        # Отправка обычного письма:
        #     send_mail( 
        #     subject=f'Message from: {message.name}. - {message.subject}',
        #     message=f'Subject: {message.subject}\n \n{message.message}\n \nContact email: {message.email}\nName: {message.name}',
        #     from_email='subscribecategory@yandex.ru', # здесь указываете почту, с которой будете отправлять (об этом попозже)
        #     recipient_list=['mr@rng-services.com']  # здесь список получателей. Например, секретарь, сам врач и т. д.
        # )
        
        # Отправка письма с HTML шаблоном:
            # #  отправляем на почту HTML-шаблон:

            # # получаем наш html
            # html_content = render_to_string('website/message_created.html', {'message': message})
            
            # msg = EmailMultiAlternatives(
            #     subject=f'Message from: {message.name}. - {message.subject}',
            #     body=f'Subject: {message.subject}\n \n{message.message}\n \nContact email: {message.email}\nName: {message.name}',  #  это то же, что и message
            #     from_email='subscribecategory@yandex.ru',
            #     to=['mikkapost@gmail.com'], 
            #     # from_email=config('from_email'),
            #     # to=[config('recipient_1'), config('recipient_2')], 
            # )
            # msg.attach_alternative(html_content, "text/html")  # добавляем html

            # msg.send()  # отсылаем
            
            return redirect('website:home')
    else:
        message_form = MessageForm()

    topVacancies_list = Vacancy.objects.filter(is_published=True).filter(is_on_top=True).order_by('-date_published')[:3]

    context_dict = {'topVacancies_list': topVacancies_list, 'message_form': message_form}     
    return render(request, 'website/home.html', context_dict)

    # context_dict = {'projects': projects, 'form': form, 'blog_1': blog_1, 'blog_2': blog_2, 'blog_3': blog_3} 
    # return render(request, 'portfolio/home.html', context_dict)
