from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import *
from emlakapp import views
from emlakapp.views import main  # main görünümünü buraya ekleyin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', index, name='index'),
    path('', main, name='main'),  # main fonksiyonunu çağırın
    path('logout/', userLogout, name='userLogout'),
    path('ilan-ekle',ilanEkle,name='ilanEkle'),
    path('delete-ilans/', delete_ilans, name='delete_ilans'),
    path('ilan/<int:ilan_id>/edit/', edit_ilan, name='edit_ilan'),
    path('musteri/', musteri, name='musteri'),
    path('musteriler/', musteriler_list, name='musteriler_list'),
    path('delete_musteriler/', delete_musteriler, name='delete_musteriler'),
    path('get_musteri/<int:musteri_id>/', get_musteri, name='get_musteri'),  # Düzgün bir şekilde tanımlandı
    path('edit_musteri/<int:musteri_id>/', edit_musteri, name='edit_musteri'),
    path('musteri-ekle',musteri_ekle,name='musteri_ekle'),
    path('ilan/<int:id>/',ilanDetay,name='ilan_detay')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
