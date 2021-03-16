from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .serializers import ContactEmailSerializer
from email_manager.contact_email.models import ContactEmail


class ContactEmailViewSet(ModelViewSet):

    serializer_class = ContactEmailSerializer
    queryset = ContactEmail.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']
