from rest_framework import permissions

# Makaleler için izin: Kullanıcı sadece kendi makalelerini düzenleyebilir
class KendiMakalesiYaDaReadOnly(permissions.BasePermission):
    """
    Kullanıcı yalnızca kendi makalelerini güncelleyebilir ya da silebilir,
    diğer makaleleri sadece görüntüleyebilir.
    """
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS gibi okuma izni olan isteklerde her kullanıcıya izin verilir
        if request.method in permissions.SAFE_METHODS:
            return True
        # Yalnızca makalenin yazarı olan kullanıcı güncelleme ve silme yapabilir
        return obj.yazar == request.user.username

# Yorumlar için izin: Kullanıcı sadece kendi yorumlarını düzenleyebilir
class KendiYorumuYaDaReadOnly(permissions.BasePermission):
    """
    Kullanıcı yalnızca kendi yazdığı yorumları güncelleyebilir ya da silebilir,
    diğer yorumları sadece görüntüleyebilir.
    """
    def has_object_permission(self, request, view, obj):
        # Okuma izinlerine her kullanıcı erişebilir
        if request.method in permissions.SAFE_METHODS:
            return True
        # Yalnızca yorumun sahibi olan kullanıcı güncelleme ve silme yapabilir
        return obj.yorum_sahibi == request.user

# Favoriler için izin: Kullanıcı sadece kendi favorilerini düzenleyebilir
class KendiFavorisiYaDaReadOnly(permissions.BasePermission):
    """
    Kullanıcı yalnızca kendi favorilerini güncelleyebilir ya da silebilir,
    diğer favorileri sadece görüntüleyebilir.
    """
    def has_object_permission(self, request, view, obj):
        # Okuma izinlerine her kullanıcı erişebilir
        if request.method in permissions.SAFE_METHODS:
            return True
        # Yalnızca favorinin sahibi olan kullanıcı güncelleme ve silme yapabilir
        return obj.favori_sahibi == request.user