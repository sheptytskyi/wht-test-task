from django.db import models
from django.utils.translation import gettext_lazy as _

from teams.models.person import PersonModel


class TeamModel(models.Model):
    name = models.CharField(verbose_name=_('Team Name'), max_length=128, unique=True)
    members = models.ManyToManyField(
        verbose_name=_('Members'),
        to=PersonModel,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'team'
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __str__(self) -> str:
        return f'{self.name}'
