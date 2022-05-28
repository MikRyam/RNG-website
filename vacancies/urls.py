from django.urls import path
from . import views
from vacancies.views import * 
# VacanciesListView, VacancyDetailView, DashboardView, DashboardDetailView, AddVacancyView, UpdateVacancyView, DeleteVacancyView, MessagesListView, MessagesDeleteView, ApplicationsListView, ApplicationDeleteView, ApplicationDetailView, AddApplicationView

app_name = 'vacancies'


urlpatterns = [
    # get_absolute_url
    path('', VacanciesListView.as_view(), name = 'vacancies_list'),
    # path('absolute-path/<int:id>/detail/', PageDetailGetAbsoluteUrl.as_view(), name = 'detail_absolute_path'),
    # path('<int:pk>/<str:slug>/', VacancyDetailView.as_view(), name = 'vacancy_detail'),  # вместо него теперь 'add_application'
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/<int:pk>/<str:slug>/', DashboardDetailView.as_view(), name = 'dashboard_detail'),
    path('dashboard/new/', AddVacancyView.as_view(), name='vacancy_new'),
    path('dashboard/edit/<int:pk>/<str:slug>/', UpdateVacancyView.as_view(), name='dashboard_update'),
    path('dashboard/<int:pk>/<str:slug>/remove/', DeleteVacancyView.as_view(), name='dashboard_delete'),
    path('dashboard/<int:pk>/<str:slug>/publish/', views.publish_vacancy, name='to_publish'),
    path('dashboard/messages/', MessagesListView.as_view(), name='messages'),
    path('dashboard/message/<int:pk>/remove/', MessagesDeleteView.as_view(), name='message_delete'),
    path('dashboard/applications/', ApplicationsListView.as_view(), name='applications'),
    path('dashboard/application/<int:pk>/', ApplicationDetailView.as_view(), name='application_detail'),
    path('dashboard/application/<int:pk>/remove/', ApplicationDeleteView.as_view(), name='application_delete'),
    path('<int:pk>/<str:slug>/', AddApplicationView.as_view(), name='add_application'),
    # path('<int:pk>/<str:slug>/application/success/', views.application_success, name='application_success'), 
    path('<int:pk>/<str:slug>/application/success/', ApplicationSuccessDetailView.as_view(), name='application_success'),

    
]

# application/

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about', views.about, name='about'),

   
#     path('', HomeView.as_view(), name='home'),
#     path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
# ]
