from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.locations.models import AbstractAddress


class User(AbstractUser):
    picture = models.URLField(null=True, blank=True)
    mobile_number = models.CharField(max_length=11, verbose_name=_('mobile number'), blank=True, null=True)
    nid_no = models.CharField(max_length=200, verbose_name=_('nid no'), blank=True, null=True)
    date_of_birth = models.CharField(max_length=200, verbose_name=_('date of birth'), blank=True, null=True)
    birth_no = models.CharField(max_length=200, verbose_name=_('birth no'), blank=True, null=True)
    father_name = models.CharField(max_length=200, verbose_name=_('father name'), blank=True, null=True)
    father_nid_no = models.CharField(max_length=200, verbose_name=_('father nid no'), blank=True, null=True)
    mother_name = models.CharField(max_length=200, verbose_name=_('mother name'), blank=True, null=True)
    mother_nid_no = models.CharField(max_length=200, verbose_name=_('mother nid no'), blank=True, null=True)
    class Gender(models.TextChoices):
        male = "male"
        female = "female"
        others = "others"

    gender = models.CharField(
        max_length=10, choices=Gender.choices,verbose_name=_('gender'), null=True, blank=True
    )
    religion = models.CharField(max_length=10,verbose_name=_('relgion'), null=True, blank=True)
    



    # Status fields
    email_verified = models.BooleanField(verbose_name=_('email verified'), default=False)
    mobile_verified = models.BooleanField(verbose_name=_('mobile verified'), default=False)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        constraints = [
            models.UniqueConstraint(fields=('mobile_number',), name='unique_user_mobile_number'),
        ]

    @property
    def profile_created(self):
        return hasattr(self, 'permanent_address')


class UserPermanentAddress(AbstractAddress):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='permanent_address')

    class Meta(AbstractAddress.Meta):
        verbose_name = _('user permanent address')
        verbose_name_plural = _('user permanent addresses')
