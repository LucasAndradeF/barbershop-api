from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # Rotas da Documentação gerada através da lib "drf-spectacular"
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Rota admin para acesso ao painel de administração do DJANGO
    path('admin/', admin.site.urls),

    # Todas as rotas do app clients
    path('api/', include('clients.urls')),

    # Todas as rotas do app barbers
    path('api/', include('barbers.urls')),
    
    # Todas as rotas do app barbers
    path('api/', include('services.urls')),

    # Rotas de login e refresh token da aplicação
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
