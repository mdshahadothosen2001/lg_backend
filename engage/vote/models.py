from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.utils.models import TimestampModel
from engage.accounts.models import User
from engage.locations.models import  Union


class VotingPoll(TimestampModel):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('created member'), related_name='+')
    union = models.ForeignKey(Union, on_delete=models.PROTECT, verbose_name=_('union'), related_name='+', null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)
    total_voter = models.PositiveSmallIntegerField(default=0)
    file = models.FileField(upload_to='voting_polls/', null=True, blank=True, verbose_name=_('file'))
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name=_('link'))
    start_date = models.DateTimeField(verbose_name=_('start date'), null=True, blank=True)
    end_date = models.DateTimeField(verbose_name=_('end date'), null=True, blank=True)
    is_public = models.BooleanField(default=True, verbose_name=_('is public'))
    is_voting = models.BooleanField(default=False, verbose_name=_('is voting'))
    is_result_published = models.BooleanField(default=False, verbose_name=_('is result published'))
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
