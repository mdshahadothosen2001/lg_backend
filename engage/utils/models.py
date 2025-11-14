from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampModel(models.Model):
    """
    An abstract model that provides self-updating fields 'created_at' and 'modified_at'
    to track the creation and modification timestamps of a model instance.
    """
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name=_('modified at'), auto_now=True)

    class Meta:
        abstract = True
