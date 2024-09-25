from django.contrib import admin
from django.urls import path, include  # include fonksiyonunu ekleyin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger ayarları
schema_view = get_schema_view(
    openapi.Info(
        title="Spor Haberleri API",
        default_version='v1',
        description="Spor Haberleri API için dokümantasyon",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@sporhaberleri.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # JWT Token alma
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # JWT Token yenileme
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # JWT Token doğrulama
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Swagger UI ve ReDoc için URL'ler
    path('api_documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api_documentation/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Haberler uygulamasının URL'lerini include ediyoruz
    path('api/', include('news.api.urls')),  # 'haberler' uygulamasındaki tüm URL'leri buraya dahil edin
]