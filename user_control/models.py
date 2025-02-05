from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.conf import settings


class User(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class TaskPhoto(models.Model):
    task = models.ForeignKey(
        'Task', # Используем строковое имя модели, чтобы избежать циклической зависимости
        on_delete=models.CASCADE,
        related_name='photos' # Важно для обратной ссылки
    )
    image = models.ImageField(upload_to='task_photos/')
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for task {self.task.title}" # Более информативное строковое представление


class Task(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    initiator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='initiated_tasks',
        null=True,
        blank=True
    )
    address = models.CharField(max_length=100)
    responsible = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='responsible_tasks',
        null=True,
        blank=True
    )
    executors = models.ManyToManyField(
        User,
        related_name='executed_tasks',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TaskDocuments(models.Model):
    task = models.ForeignKey(
        'Task',  # Связь с моделью Task
        on_delete=models.CASCADE,  # Удаление документов при удалении задачи
        related_name='documents'  # Обратная связь для доступа к документам задачи
    )
    file = models.FileField(upload_to='files/')  # Поле для хранения файла
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Дата добавления файла
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Связь с моделью пользователя
        on_delete=models.SET_NULL,  # Если пользователь удален, поле станет NULL
        null=True,
        blank=True
    )
    description = models.CharField(max_length=255, blank=True)  # Описание файла

    def __str__(self):
        return f"Document for task {self.task.title} (uploaded by {self.uploaded_by})"
