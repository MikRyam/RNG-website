from django.http import request, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# from .tasks import subscribe_confirmation_message

from vacancies.models import Vacancy, JobApplication
from vacancies.forms import VacancyForm, VacancyEditForm, JobApplicationForm
from vacancies.filters import DashboardFilter, VacancyFilter
from website.models import Message

@login_required
def publish_vacancy(request, pk, slug):
    ''' Кнопка "Опубликовать" - Button on 'dashboard_detail' and 'dashboard' pages'''
    vacancy  = get_object_or_404(Vacancy, pk=pk)
    vacancy.publish()
    return redirect('vacancies:dashboard_detail', pk=pk, slug=slug)


class VacanciesListView(ListView):
    ''' List of all published vacancies '''
    model = Vacancy    
    paginate_by = 6
    template_name = "vacancies/vacancies_list.html"
    # ordering = ['-date_published']  # вывод списка публикаций в обратном порядке, от более новых к более старым
    context_object_name = 'published_vacancies_list'
     
    def get_queryset(self):
        return Vacancy.objects.filter(is_published=True).order_by('-date_published') 

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса 
        context = super().get_context_data(**kwargs)        
        published_vacancies_list = Vacancy.objects.filter(is_published=True).order_by('-date_published')        
        context['published_vacancies_list'] = published_vacancies_list
        context['filter'] = VacancyFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


class DashboardView(LoginRequiredMixin, ListView):
    ''' List of all created vacancies '''
    ''' Also applied filter '''
    model = Vacancy
    template_name = 'vacancies/dashboard.html'
    context_object_name = 'all_vacancies_list'
    # paginate_by = 3
    ordering = ['-date_published']  # вывод списка публикаций в обратном порядке, от более новых к более старым

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = DashboardFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        get_copy = self.request.GET.copy()
        if get_copy.get('page'):
            get_copy.pop('page')
        context['get_copy'] = get_copy
        return context

    # def get_queryset(self):
    #     return Vacancy.objects.order_by('-date_published') 

    # def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса 
    #     context = super().get_context_data(**kwargs)        
    #     published_vacancies_list = Vacancy.objects.filter(is_published=True).order_by('-date_published')        
    #     context['published_vacancies_list'] = published_vacancies_list
    #     context['filter'] = DashboardFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
    #     return context


class DashboardDetailView(LoginRequiredMixin, DetailView):
    ''' Show vacancy with job_applications '''
    model = Vacancy    
    template_name = "vacancies/dashboard_detail.html"

    def get_context_data(self, *args, **kwargs):        
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        current_vacancy = get_object_or_404(Vacancy, id=self.kwargs['pk'])
        vacancy_applications = current_vacancy.job_applications.order_by('-date_added')  # job_applications - 'related name' in models.py
        vacancy_applications_count = current_vacancy.job_applications.count()               
        context['vacancy_applications_count'] = vacancy_applications_count
        context['vacancy_applications'] = vacancy_applications               
        return context


class AddVacancyView(LoginRequiredMixin, CreateView):
    ''' Creation of a new vacancy by logged-in user '''
    model = Vacancy
    form_class = VacancyForm
    template_name = 'vacancies/dashboard_edit.html'
    # success_url = reverse_lazy('vacancies/dashboard_detail.html')
    
    def form_valid(self, form):
        ''' Autosaving current logged-in user as author after creating new post '''
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateVacancyView(LoginRequiredMixin, UpdateView):
    ''' Vacancy editing by author '''
    model = Vacancy
    template_name = 'vacancies/dashboard_edit.html'
    form_class = VacancyForm
    

class DeleteVacancyView(LoginRequiredMixin, DeleteView):
    ''' Vacancy deleting by author '''
    model = Vacancy
    template_name = 'vacancies/dashboard_delete.html'
    success_url = reverse_lazy('vacancies:dashboard')


class MessagesListView(LoginRequiredMixin, ListView):
    ''' List of all recieved messages from the site '''
    model = Message    
    paginate_by = 10
    template_name = "vacancies/messages_list.html"
    ordering = ['-date']  # вывод списка публикаций в обратном порядке, от более новых к более старым
    context_object_name = 'messages_list'

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса 
        context = super().get_context_data(**kwargs)        
        num_of_all_messages = Message.objects.all().count()        
        context['num_of_all_messages'] = num_of_all_messages
        # context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context
     

class MessagesDeleteView(LoginRequiredMixin, DeleteView):
    ''' Messages deleting '''
    model = Message
    template_name = 'vacancies/message_delete.html'
    success_url = reverse_lazy('vacancies:messages')


class AddApplicationView(CreateView):
    ''' Creation of a new job application & vacancy detail too'''
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'vacancies/application_form.html'

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса 
        context = super().get_context_data(**kwargs)
        context['application_form'] = JobApplicationForm
        context['vacancy'] = Vacancy.objects.get(pk=self.kwargs['pk'])
        return context

    
    def form_valid(self, form):
        ''' Autosaving current vacancy after creating this new application '''
        # form.instance.author = self.request.user
        # obj = form.save(commit=False)
        # obj.vacancy = Vacancy.objects.get(pk=self.kwargs['pk'])
        # obj.save()
        # form.instance.vacancy_id = self.kwargs['pk']  # забираем pk текущей вакансии
        form.instance.vacancy = Vacancy.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('vacancies:vacancy_detail', kwargs={'pk': self.kwargs['pk']})


# def application_success(request):
#     # vacancy = Vacancy.objects.get(pk=self.kwargs['pk'])     , {'vacancy': vacancy}
#     return render(request, 'vacancies/application_success.html')


class ApplicationsListView(LoginRequiredMixin, ListView):
    ''' List of all recieved job applications from the site '''
    model = JobApplication    
    paginate_by = 10
    template_name = "vacancies/applications_list.html"
    ordering = ['-date_added']  # вывод списка публикаций в обратном порядке, от более новых к более старым
    context_object_name = 'applications_list'

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса 
        context = super().get_context_data(**kwargs)        
        num_of_all_applications = JobApplication.objects.all().count()        
        context['num_of_all_applications'] = num_of_all_applications
        # context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

     
class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = JobApplication   
    template_name = "vacancies/application_detail.html"


class ApplicationSuccessDetailView(DetailView):
    model = Vacancy  
    template_name = "vacancies/application_success.html"

    # def get_context_data(self, **kwargs):  
    #     context = super().get_context_data(**kwargs)
    #     context['vacancy'] = Vacancy.objects.get(pk=self.kwargs['pk'])
    #     return context

    

class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    ''' Job application deleting '''
    model = JobApplication
    template_name = 'vacancies/application_delete.html'
    success_url = reverse_lazy('vacancies:applications')

