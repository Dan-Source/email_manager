from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from email_manager.message.models import Message
from .serializers import MessageSerializer
from django.core.mail import send_mail


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject', 'message', 'sender_email']

    @action(methods=['put'], detail=True)
    def send_email_message(self, request):
        subject = request.POST.get('subject', None)
        body = request.POST.get('body', None)
        sender = request.POST.get('sender_email', None)
        to = 'dan.dluis.dl@gmail.com'  #request.POST.get('email_list', None)
        
        send_mail(
            subject,
            body,
            sender,
            to,
            fail_silently=False,
        )

    @action(methods=['post'], detail=False)
    def send_test_email(self, request):
        subject = "Testando Envio de E-mail Com Django"
        body = "Que coisas não podermos enviar isso. "
        sender = 'webmaster@teste.com'
        to = ['dan.dluis.dl@gmail.com'] #request.POST.get('email_list', None)
        send_mail(
            subject,
            body,
            sender,
            to,
            fail_silently=False,
        )

