from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .models import User, LessonProgress, ChatLog

class ChatLogInline(admin.TabularInline):
    model = ChatLog
    extra = 0
    fields = ("role", "content", "timestamp")
    readonly_fields = ("role", "content", "timestamp")
    can_delete = False
    show_change_link = False

class LessonProgressInline(admin.TabularInline):
    model = LessonProgress
    extra = 0
    fields = ("title", "page", "date")
    readonly_fields = ("title", "page", "date")
    can_delete = False
    show_change_link = False

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [ChatLogInline, LessonProgressInline]

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username')
    ordering = ('email',)

@admin.register(ChatLog)
class ChatLogAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "content", "timestamp")
    list_filter = ("role", "timestamp")
    search_fields = ("user__email", "content")
    ordering = ("-timestamp",)

@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "page", "date")
    list_filter = ("date",)
    search_fields = ("user__email", "title")
    ordering = ("-date",)
