from django.db import models
from django.utils.translation import gettext_lazy as _


class PersonModel(models.Model):
    first_name = models.CharField(verbose_name=_('First Name'), max_length=128)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=128)
    email = models.EmailField(verbose_name=_('Email'), max_length=128, unique=True)

    class Meta:
        db_table = 'person'
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self) -> str:
        return f'{self.get_fullname} {self.email} '

    @property
    def get_fullname(self) -> str:
        return f'{self.first_name} {self.last_name}'
