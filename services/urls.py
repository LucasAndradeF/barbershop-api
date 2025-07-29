from rest_framework import routers
from .views import ServiceView
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'services', ServiceView, basename='services')

urlpatterns = [
    path('', include(router.urls))
]
