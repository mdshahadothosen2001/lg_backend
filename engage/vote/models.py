from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.utils.models import TimestampModel
from engage.accounts.models import User
from engage.local_govt.models import Localgovt


class VotingPoll(TimestampModel):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('created member'), related_name='+')
    localgovt = models.ForeignKey(Localgovt, on_delete=models.PROTECT, verbose_name=_('local goverment'), related_name='+')
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)
    total_voter = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = _('voting poll')
        verbose_name_plural = _('voting polls')

    def __str__(self):
        return self.title


class Voting(TimestampModel):
    voter = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('voter'), related_name='+')
    votingpoll = models.ForeignKey(VotingPoll, on_delete=models.PROTECT, verbose_name=_('voting poll'), related_name='+')
    opinion = models.BooleanField(default=True)


    class Meta:
        verbose_name = _('voting')
        verbose_name_plural = _('votings')

    def __str__(self):
        return f"{self.voter} {self.opinion}"
