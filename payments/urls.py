from rest_framework import routers
from .views import PaymentView
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'payments', PaymentView, basename='payments')

urlpatterns = [
    path("", include(router.urls))
]
