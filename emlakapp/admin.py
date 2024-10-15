from django.contrib import admin
from .models import Ilan, Musteri

# İlan modelini admin panelinde basit bir şekilde kaydediyoruz
admin.site.register(Ilan)

# Müşteri modelini de aynı şekilde kaydediyoruz
admin.site.register(Musteri)
