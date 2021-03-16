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
        ordering = ['name']
    
