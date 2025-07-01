from django.contrib import admin
from .models import Lesson, Page

class PageInline(admin.TabularInline):
    model = Page
    extra = 1
    fields = ['page', 'title', 'filename', 'file_url']
    readonly_fields = ['file_url']

    def get_readonly_fields(self, request, obj=None):
        return ['file_url']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    ordering = ['title']
    inlines = [PageInline]

admin.site.register(Lesson, LessonAdmin)
