from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.utils.models import TimestampModel
from engage.accounts.models import User
from engage.local_govt.models import Localgovt


class Request(TimestampModel):
    requested_citizen = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('request'), related_name='+')
    localgovt = models.ForeignKey(Localgovt, on_delete=models.PROTECT, verbose_name=_('local goverment'), related_name='+')
    taken_member = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('taken member'), related_name='+', null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)
    file = models.URLField(null=True, blank=True)
    
    class Status(models.TextChoices):
        pending = "pending"
        acepted = "acepted"
        canceled = "canceled"
        on_progress = "on_progress"
        done = 'done'

    status = models.CharField(
        max_length=11, choices=Status.choices,verbose_name=_('status'), default='pending'
        )
    possibility_amount = models.FloatField(default=0)
    possibility_time_required = models.DateField(null=True, blank=True)


    class Meta:
        verbose_name = _('request')
        verbose_name_plural = _('requests')

    def __str__(self):
        return self.title
