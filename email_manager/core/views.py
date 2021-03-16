from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from message.models import Message
from contact_email.models import ContactEmail
from django.core.mail import send_mail


class SendFormEmail(APIView):

    def get(self, request, format=None):
        pass