from rest_framework import routers
from .views import ClientServiceView, BarberServiceView
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'client/services', ClientServiceView,
                basename='client-services')
router.register(r'barber/services', BarberServiceView,
                basename='barber-services')

urlpatterns = [
    path('', include(router.urls))
]
