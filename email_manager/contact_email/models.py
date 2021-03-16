from django.db import models


class ContactEmail(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    is_active = models.BooleanField('Ativo', default=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(' ')[0]
