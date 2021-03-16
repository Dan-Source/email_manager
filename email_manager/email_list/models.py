from django.db import models
from email_manager.contact_email.models import ContactEmail


class EmailList(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')
    emails = models.ManyToManyField(ContactEmail)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Lista de Email'
        verbose_name_plural = 'Listas de Emails'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_list_of_email(self):
        pass
