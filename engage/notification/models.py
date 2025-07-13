from django.db import models
from django.utils.translation import gettext_lazy as _
from engage.locations.models import  Union

class Notice(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    union = models.ForeignKey(Union, on_delete=models.PROTECT, verbose_name=_('union'), related_name='+', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'notice'
        verbose_name_plural = 'notices'
        db_table = 'notice'

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start = models.TimeField(null=True, blank=True)
    duration = models.SmallIntegerField(null=True, blank=True)
    link = models.URLField()
    union = models.ForeignKey(Union, on_delete=models.PROTECT, verbose_name=_('union'), related_name='+', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'
        db_table = 'event'

    def __str__(self):
        return self.title
