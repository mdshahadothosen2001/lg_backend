from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.utils.models import TimestampModel
from engage.accounts.models import User
from engage.local_govt.models import Member
from engage.locations.models import  Union


class Request(TimestampModel):
    requested_citizen = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('request'), related_name='+', help_text=_('Who sent the request to solve the issue'))
    union = models.ForeignKey(Union, on_delete=models.PROTECT, verbose_name=_('union'), related_name='+', null=True, blank=True)
    taken_member = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name=_('taken member'), related_name='+', null=True, blank=True,  help_text=_('Who is taking the responsibility to solve the issue'))
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)
    file = models.URLField(null=True, blank=True)

    requested_to = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    is_best = models.BooleanField(default=False)
    
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


class RespondImage(models.Model):
    respond = models.ForeignKey(
        Request, 
        on_delete=models.PROTECT, 
        verbose_name=_('image'), 
        related_name='respond_images',
        help_text=_('respond images')
    )
    image = models.ImageField(upload_to='respond_images/')

    class Meta:
        verbose_name = _('respond_img')
        verbose_name_plural = _('respond_imgs')

    def __str__(self):
        return self.respond.title



class Solution(TimestampModel):
    request = models.ForeignKey(
        Request,
        on_delete=models.CASCADE,
        related_name="solutions",
        verbose_name=_("request")
    )
    suggested_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="solutions",
        verbose_name=_("suggested by")
    )
    description = models.TextField(verbose_name=_("solution description"))
    file = models.URLField(null=True, blank=True)

    is_best = models.BooleanField(default=False, help_text=_("Marked as best by admin"))
    is_open_for_vote = models.BooleanField(default=False, help_text=_("Admin opened voting for this solution"))

    class Meta:
        verbose_name = _("solution")
        verbose_name_plural = _("solutions")

    def __str__(self):
        short_desc = (self.description[:30] + "...") if len(self.description) > 30 else self.description
        return f"{self.request.title} - {self.suggested_by.username} - {short_desc}"


class SolutionVote(TimestampModel):
    solution = models.ForeignKey(
        Solution,
        on_delete=models.CASCADE,
        related_name="votes",
        verbose_name=_("solution")
    )
    voted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="solution_votes",
        verbose_name=_("voted by")
    )
    value = models.BooleanField(
        default=True,
        help_text=_("True = upvote, False = downvote")
    )

    class Meta:
        verbose_name = _("solution vote")
        verbose_name_plural = _("solution votes")
        unique_together = ("solution", "voted_by")  # prevent duplicate vote

    def __str__(self):
        return f"{self.solution} → {self.voted_by.username}"