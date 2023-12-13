import json
import uuid

from django.db import models

from users_app.models import User


# Create your models here.
class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Родительская категория")
    name = models.CharField(max_length=500, null=True, unique=False, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        app_label = 'wildberries_app'


class Param(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    type = models.IntegerField(null=True, verbose_name="Тип")
    max_count = models.IntegerField(null=True, verbose_name="Максимальное количество")
    unit = models.CharField(max_length=50, null=True, verbose_name="Единица измерения")
    popular = models.BooleanField(default=False, verbose_name="Популярный")
    required = models.BooleanField(default=False, verbose_name="Обязательный")
    name = models.CharField(max_length=500, null=True, verbose_name="Название")

    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name="Категория")

    def __str__(self):
        return self.name if self.name else f"Param-{self.id}"

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'
        app_label = 'wildberries_app'


class FilesStorage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    version = models.IntegerField(verbose_name="Версия")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    is_main = models.BooleanField(default=True, verbose_name="Основной")
    blob = models.BinaryField(null=True, verbose_name="Данные")
    size = models.BigIntegerField(null=True, verbose_name="Размер")
    name = models.CharField(max_length=500, null=True, verbose_name="Имя")
    mime_type = models.CharField(max_length=250, null=True, verbose_name="MIME-тип")

    def __str__(self):
        return self.name if self.name else f"File-{self.id}"

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        app_label = 'wildberries_app'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    version = models.IntegerField(verbose_name="Версия")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    sku_wb = models.BigIntegerField(null=True, verbose_name="SKU WB")
    number_wb = models.BigIntegerField(null=True, verbose_name="Номер WB")
    sku = models.CharField(max_length=50, null=True, verbose_name="SKU")
    name = models.CharField(max_length=500, null=True, verbose_name="Название")
    brand = models.CharField(max_length=500, null=True, verbose_name="Бренд")
    description = models.CharField(max_length=2000, null=True, verbose_name="Описание")
    uploaded = models.BooleanField(default=False, verbose_name="Загружено")
    params = models.TextField(max_length=5000, null=True, verbose_name="Параметры")

    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name="Категория")

    images = models.ManyToManyField(FilesStorage, related_name='products', blank=True, verbose_name="Изображения")

    def get_params(self):
        return json.loads(self.params) if self.params else []

    def __str__(self):
        return self.name if self.name else f"Product-{self.id}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        app_label = 'wildberries_app'


class Warehouse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    name = models.CharField(max_length=500, null=True, verbose_name="Название")
    address = models.CharField(max_length=1000, null=True, verbose_name="Адрес")
    is_main = models.BooleanField(default=False, verbose_name="Основной")

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"
        app_label = 'wildberries_app'

