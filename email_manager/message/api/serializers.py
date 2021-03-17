from rest_framework.serializers import ModelSerializer
from email_manager.message.models import Message
from email_manager.email_list.api.serializers import EmailListSerializer


class MessageSerializer(ModelSerializer):
    #email_list = EmailListSerializer()
    
    class Meta:
        model = Message
        fields = (
            'id', 'subject', 'body', 'sender_email', 'email_list'
        )

    def update(self, instance, validated_data):
        pass