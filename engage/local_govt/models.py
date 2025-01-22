from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.utils.models import TimestampModel
from engage.accounts.models import User
from engage.locations.models import Division, District, Upazila, Union


class Localgovt(TimestampModel):
    class TypeOfLocalGovt(models.TextChoices):
        union = "union"
        upazila = "upazila"
        district = "district"
        division = "division"

    type = models.CharField(
        max_length=20, choices=TypeOfLocalGovt.choices,verbose_name=_('Type of Local Govt')
        )

    division = models.ForeignKey(Division, on_delete=models.PROTECT, verbose_name=_('division'), related_name='+')
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name=_('district'), related_name='+', null=True, blank=True)
    upazila = models.ForeignKey(Upazila, on_delete=models.PROTECT, verbose_name=_('upazila'), related_name='+', null=True, blank=True)
    union = models.ForeignKey(Union, on_delete=models.PROTECT, verbose_name=_('union'), related_name='+', null=True, blank=True)
    location = models.CharField(verbose_name=_('location'), max_length=200, null=True, blank=True)
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)


    class Meta:
        verbose_name = _('localgovt')
        verbose_name_plural = _('localgovts')

    def __str__(self):
        localgovt = self.type + ' : ' + self.division.name + '-'
        if self.district:
            localgovt += '-'+ self.district.name
        if self.upazila:
            localgovt += '-'+ self.upazila.name
        if self.union:
            localgovt += '-'+ self.union.name

        return localgovt


class Member(models.Model):
    position = models.CharField(max_length=200, verbose_name=_('position'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('user'), related_name='+')
    localgovt = models.ForeignKey(Localgovt, on_delete=models.PROTECT, verbose_name=_('local govt'), related_name='+')
    areas = models.CharField(max_length=200, verbose_name=_('working areas'))
    start_at = models.DateField(verbose_name=_('working start date'))
    end_at = models.DateField(verbose_name=_('working end date'))
    is_active = models.BooleanField(verbose_name=_('active status'), default=True)
    
    
    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

    def __str__(self):
        return f"{self.position}: {self.user.first_name} {self.user.last_name}"
