from rest_framework.serializers import ModelSerializer
from email_manager.contact_email.models import ContactEmail


class ContactEmailSerializer(ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = (
            'id', 'name', 'email'
        )
