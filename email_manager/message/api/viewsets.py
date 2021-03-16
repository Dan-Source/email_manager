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

    @action(methods=['post'], detail=False)
    def send_email_message(self, request):
        subject = request.POST.get('subject', None)
        body = request.POST.get('body', None)
        to = request.POST.get('sender_email', None)
        email_list = request.POST.get('email_list', {})
        print(email_list)
        send_mail(
            subject,
            body,
            to,
            ['daniel.dluis.dl@gmail.com'],
            fail_silently=False,
        )
