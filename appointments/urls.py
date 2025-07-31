from rest_framework import routers
from .views import ClientAppointmentView, BarberAppointmentView
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'client-appointments', ClientAppointmentView,
                basename='client-appointments')
router.register(r'barber-appointments', BarberAppointmentView,
                basename='barber-appointments')

urlpatterns = [
    path("", include(router.urls))
]
