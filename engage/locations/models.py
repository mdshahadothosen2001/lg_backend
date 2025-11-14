from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.utils.models import TimestampModel


class Division(models.Model):
    name = models.CharField(unique=True ,verbose_name=_('division'), max_length=50)

    class Meta:
        verbose_name = _('division')
        verbose_name_plural = _('divisions')

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(verbose_name=_('district'), max_length=50)
    division = models.ForeignKey(
        to=Division,
        on_delete=models.CASCADE,
        verbose_name=_('division'),
        related_name='districts',
    )

    class Meta:
        verbose_name = _('district')
        verbose_name_plural = _('districts')

    def __str__(self):
        return self.name


class Upazila(models.Model):
    name = models.CharField(verbose_name=_('upazila'), max_length=50)
    district = models.ForeignKey(
        to=District,
        on_delete=models.CASCADE,
        verbose_name=_('district'),
        related_name='upazilas',
    )

    class Meta:
        verbose_name = _('upazila')
        verbose_name_plural = _('upazilas')

    def __str__(self):
        return self.name


class Union(models.Model):
    name = models.CharField(verbose_name=_('union'), max_length=50)
    upazila = models.ForeignKey(
        to=Upazila,
        on_delete=models.CASCADE,
        verbose_name=_('upazila'),
        related_name='unions',
    )

    class Meta:
        verbose_name = _('union')
        verbose_name_plural = _('unions')

    def __str__(self):
        return f"{self.name} ({self.id})"


class AbstractAddress(TimestampModel):
    """Base model for storing address information."""
    division = models.ForeignKey(Division, on_delete=models.PROTECT, verbose_name=_('division'), related_name='+')
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name=_('district'), related_name='+')
    upazila = models.ForeignKey(Upazila, on_delete=models.PROTECT, verbose_name=_('upazila'), related_name='+', null=True, blank=True)
    union = models.ForeignKey(Union, on_delete=models.PROTECT, verbose_name=_('union'), related_name='+', null=True, blank=True)
    living_place = models.CharField(verbose_name=_('living place'), max_length=200)
    holding_no = models.CharField(verbose_name=_('holding no'), max_length=200, null=True, blank=True)
    ward_no = models.CharField(verbose_name=_('ward no'), max_length=200, null=True, blank=True)
    road_no = models.CharField(verbose_name=_('road no'), max_length=200, null=True, blank=True)
    location = models.CharField(verbose_name=_('location'), max_length=200)

    class Located(models.TextChoices):
        city_corporation = 'city corporation'
        zila_parishad = 'zila parishad'
        upzila_parishad = 'upazila parishad'
        union_parishad = 'union parishad'
    located = models.CharField(
        max_length=20, verbose_name=_('connected'), choices=Located.choices
    )

    class Meta(TimestampModel.Meta):
        abstract = True
