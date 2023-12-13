from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        app_label = 'users_app'


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    version = models.IntegerField(verbose_name="Версия")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    is_active = models.BooleanField(default=True, verbose_name="Активно")
    name = models.CharField(max_length=500, unique=True, verbose_name="Наименование")
    inn = models.CharField(max_length=50, null=True, verbose_name="ИНН")
    kpp = models.CharField(max_length=50, null=True, verbose_name="КПП")
    ogrn = models.CharField(max_length=150, null=True, verbose_name="ОГРН")
    okved = models.CharField(max_length=250, null=True, verbose_name="ОКВЭД")

    users = models.ManyToManyField(User, related_name='organizations', blank=True, verbose_name="Пользователи")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        app_label = 'users_app'

