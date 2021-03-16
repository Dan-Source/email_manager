from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from email_manager.email_list.models import EmailList
from .serializers import EmailListSerializer


class EmailListViewSet(ModelViewSet):
    serializer_class = EmailListSerializer
    queryset = EmailList.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'emails']