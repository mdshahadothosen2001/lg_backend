from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.utils.models import TimestampModel
from engage.accounts.models import User
from engage.local_govt.models import Member
from engage.locations.models import  Union


class Service(models.Model):
    union = models.ForeignKey(Union, on_delete=models.PROTECT, verbose_name=_('union'), related_name='+', null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return self.title
