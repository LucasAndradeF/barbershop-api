from rest_framework import routers
from .views import ClientView, RegisterClient
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'clients', ClientView)

urlpatterns = [
    path('clients/register/',
         RegisterClient.as_view({'post': 'create'}), name='register_user'),
    path('', include(router.urls)),
]
