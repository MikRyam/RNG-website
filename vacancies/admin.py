from django.contrib import admin
from .models import Vacancy, JobApplication


# admin.site.register(Vacancy) JobApplication


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'date_created', 'date_published', 'is_published', 'is_on_top']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(JobApplication) 