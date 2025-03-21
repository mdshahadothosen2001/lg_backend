from django.db import models

from engage.local_govt.models import Localgovt


class Notice(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    localgovt = models.ForeignKey(Localgovt, on_delete=models.PROTECT, verbose_name='local goverment', related_name='+', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'notice'
        verbose_name_plural = 'notices'
        db_table = 'notice'

    def __str__(self):
        return self.title


class Even(models.Model):
    title = models.CharField(max_length=50)
    start = models.DateTimeField()
    link = models.URLField()
    localgovt = models.ForeignKey(Localgovt, on_delete=models.PROTECT, verbose_name='local goverment', related_name='+', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'even'
        verbose_name_plural = 'evens'
        db_table = 'even'

    def __str__(self):
        return self.title
