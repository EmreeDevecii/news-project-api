from django.contrib import admin
from django.urls import path, include  # include fonksiyonunu ekleyin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

# Swagger ayarları
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Spor Haberleri API",
#         default_version='v1',
#         description="Spor Haberleri API için dokümantasyon",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@sporhaberleri.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # JWT Token alma
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # JWT Token yenileme
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # JWT Token doğrulama
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # api scheması için endpoint
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI ve ReDoc için URL'ler
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Haberler uygulamasının URL'lerini include ediyoruz
    path('api/', include('news.api.urls')),  # 'haberler' uygulamasındaki tüm URL'leri buraya dahil edin
]

urlpatterns += i18n_patterns(
    path('api/', include('news.api.urls')),  # API URL'lerini dil ile ilişkilendirme
)