from rest_framework import routers
from .views import BarberView, RegisterBarberView, BarberConfigView
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'barbers', BarberView, basename='barbers')
router.register(r'barber-config', BarberConfigView, basename='barber-config')

urlpatterns = [
    path('barbers/register/',
         RegisterBarberView.as_view({'post': 'create'}), name='register_barber'),
    path('', include(router.urls))
]
