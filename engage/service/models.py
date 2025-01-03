from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.local_govt.models import Localgovt


class ServiceType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=50)
    service_type = models.ForeignKey(ServiceType,  models.DO_NOTHING, null=True, blank=True, verbose_name='service type')
    icon = models.URLField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    localgovt = models.ForeignKey(Localgovt, on_delete=models.PROTECT, verbose_name=_('local goverment'), related_name='+', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return self.title
