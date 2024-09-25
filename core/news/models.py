from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Makale(models.Model):
    baslik = models.CharField(max_length=255)
    yazar = models.CharField(max_length=255)
    icerik = models.TextField(blank=True, null=True)
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi = models.DateTimeField(auto_now=True)
    yayin_tarihi = models.DateTimeField()

    makale_resmi = models.ImageField(upload_to='makale_resimleri/', blank=True, null=True)

    def __str__(self):
        return f'{self.baslik} - {self.yazar}'
    
    class Meta:
        verbose_name_plural = "Makaleler"
    

class Yorum(models.Model):
    makale = models.ForeignKey(Makale, on_delete=models.CASCADE, related_name='yorumlar')
    yorum_sahibi = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kullanici_yorumlari')
    yorum = models.TextField(blank=True, null=True)
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi = models.DateTimeField(auto_now=True)
    degerlendirme = models.PositiveIntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return f'{self.makale} - {self.yorum_sahibi} - {self.degerlendirme}'
    
    class Meta:
        verbose_name_plural = "Yorumlar"
    
class Favori(models.Model):
    favori_sahibi = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kullanici_favorileri')
    makale = models.ForeignKey(Makale, on_delete=models.CASCADE, related_name='favoriler')

    def __str__(self):
        return f'{self.makale} - {self.favori_sahibi}'
    
    class Meta:
        verbose_name_plural = "Favoriler"