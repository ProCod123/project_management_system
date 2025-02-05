from django.contrib import admin
from .models import Task, TaskPhoto, User


@admin.register(User) 
class UserAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'phone_number', 'email', 'position', 'department', 'created_at', 'updated_at') # Поля, отображаемые в списке
    # list_filter = ('created_at', 'responsible') # Фильтры для списка
    # search_fields = ('title', 'description') # Поля для поиска

@admin.register(Task) 
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'initiator', 'responsible', 'created_at') # Поля, отображаемые в списке
    list_filter = ('created_at', 'responsible') # Фильтры для списка
    search_fields = ('title', 'description') # Поля для поиска

@admin.register(TaskPhoto) 
class TaskPhotoAdmin(admin.ModelAdmin):
    list_display = ('task', 'description', 'created_at')
    list_filter = ('created_at', 'task')
    search_fields = ('description',)
