from rest_framework import status, mixins, generics
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from news.models import Makale, Yorum, Favori
from news.api.serializers import MakaleSerializer, YorumSerializer, FavoriSerializer
from news.api.permissions import KendiMakalesiYaDaReadOnly

# Makale ViewSet
class MakaleViewSet(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet):
    
    # queryset = Makale.objects.all()
    queryset = Makale.objects.all().select_related('yazar').prefetch_related('yorumlar', 'favoriler')
    serializer_class = MakaleSerializer
    permission_classes = [IsAuthenticated, KendiMakalesiYaDaReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['baslik']

# Yorum ViewSet
class YorumViewSet(ModelViewSet):
    # queryset = Yorum.objects.all()
    queryset = Yorum.objects.all().select_related('yorum_sahibi', 'makale')
    serializer_class = YorumSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # queryset = Yorum.objects.all()
        queryset = Yorum.objects.all().select_related('yorum_sahibi', 'makale')
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(yorum_sahibi__username=username)
        return queryset

    def perform_create(self, serializer):
        # Yorum sahibini doğrudan request.user'dan alıyoruz
        serializer.save(yorum_sahibi=self.request.user)

# Favori ViewSet
class FavoriViewSet(ModelViewSet):
    # queryset = Favori.objects.all()
    queryset = Favori.objects.all().select_related('favori_sahibi', 'makale')
    serializer_class = FavoriSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # queryset = Favori.objects.all()
        queryset = Favori.objects.all().select_related('favori_sahibi', 'makale')
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(favori_sahibi__username=username)
        return queryset

    def perform_create(self, serializer):
        # Favori sahibini doğrudan request.user'dan alıyoruz
        serializer.save(favori_sahibi=self.request.user)
