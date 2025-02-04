from django.db import models


class User(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    position = models.CharField(100)
    department = models.CharField(max_length=200)

    # Добавляем метки времени
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    initiator = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)