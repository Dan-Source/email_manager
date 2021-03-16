from rest_framework.serializers import ModelSerializer
from email_manager.contact_email.api.serializers import ContactEmailSerializer
from email_manager.email_list.models import EmailList


class EmailListSerializer(ModelSerializer):
    emails = ContactEmailSerializer(many=True)

    class Meta:
        model = EmailList
        fields = (
           'id', 'name', 'emails', 'description'
        )
