from django.db import models
from django.contrib import admin


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        abstract = True

    # написал этот параметр в ice_cream/admin
    # admin.site.empty_value_display = 'не указано'
