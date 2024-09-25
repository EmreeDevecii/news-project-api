from news.models import Makale, Yorum, Favori
from rest_framework import serializers


class MakaleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    makale_resmi = serializers.ImageField(read_only=True)

    class Meta:
        model = Makale
        fields = '__all__'


class YorumSerializer(serializers.ModelSerializer):
    yorum_sahibi = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Yorum
        fields = '__all__'


class FavoriSerializer(serializers.ModelSerializer):
    favori_sahibi = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Favori
        fields = '__all__'