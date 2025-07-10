from rest_framework import routers
from .views import ClientView, RegisterClientView, ClientConfigView
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'clients', ClientView, basename='clients')
router.register(r'client-config', ClientConfigView, basename='client-config')

urlpatterns = [
    path('clients/register/',
         RegisterClientView.as_view({'post': 'create'}), name='register_user'),
    path('', include(router.urls)),

]
