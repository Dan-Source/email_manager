from django.db import models
from email_manager.email_list.models import EmailList


class Message(models.Model):
    subject = models.CharField('Assunto', max_length=200, blank=False)
    body = models.TextField('Mensagem')
    sender_email = models.EmailField("De ")
    email_list = models.ForeignKey(EmailList, on_delete=models.CASCADE)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"

    def __str__(self):
        return self.subject
