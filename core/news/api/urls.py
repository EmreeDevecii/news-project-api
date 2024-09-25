from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.api.views import MakaleViewSet, YorumViewSet, FavoriViewSet

# Router ile otomatik URL oluşturma
router = DefaultRouter()
router.register(r'makaleler', MakaleViewSet)  # Makaleler için endpoint
router.register(r'yorumlar', YorumViewSet)    # Yorumlar için endpoint
router.register(r'favoriler', FavoriViewSet)  # Favoriler için endpoint

urlpatterns = [
    # API endpoint'leri
    path('', include(router.urls)),
]