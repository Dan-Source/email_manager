from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from email_manager.contact_email.api.viewsets import ContactEmailViewSet
from email_manager.email_list.api.viewsets import EmailListViewSet
from email_manager.message.api.viewsets import MessageViewSet

router = routers.DefaultRouter()
router.register(r'contact-email', ContactEmailViewSet, basename='ContatoEmail')
router.register(r'email-list', EmailListViewSet, basename='EmailList')
router.register(r'message', MessageViewSet, basename='Message')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
