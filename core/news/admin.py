from django.contrib import admin
from news.models import Makale, Yorum, Favori

# Register your models here.

admin.site.register(Makale)
admin.site.register(Yorum)
admin.site.register(Favori)