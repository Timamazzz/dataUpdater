# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменную окружения для настройки Celery из файла настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataUpdater.settings')

# Создаем экземпляр Celery
app = Celery('dataUpdater')

# Загружаем настройки из файла настроек Django, используя префикс 'CELERY'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим и регистрируем все файлы tasks.py в приложениях Django
app.autodiscover_tasks()
