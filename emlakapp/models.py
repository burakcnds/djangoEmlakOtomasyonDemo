from django.db import models
from django.conf import settings

class Ilan(models.Model):
    # İlan başlığı
    ilan_basligi = models.CharField(max_length=255)
    # Mahalle (Karşıyaka mahalleleri)
    mahalle = models.CharField(max_length=50, choices=[
        ('Aksoy', 'Aksoy'),
        ('Alaybey', 'Alaybey'),
        ('Atakent', 'Atakent'),
        ('Bahariye', 'Bahariye'),
        ('Bahçelievler', 'Bahçelievler'),
        ('Bahriye Üçok', 'Bahriye Üçok'),
        ('Bostanlı', 'Bostanlı'),
        ('Cumhuriyet', 'Cumhuriyet'),
        ('Dedebaşı', 'Dedebaşı'),
        ('Demirköprü', 'Demirköprü'),
        ('Donanmacı', 'Donanmacı'),
        ('Fikri Altay', 'Fikri Altay'),
        ('Goncalar', 'Goncalar'),
        ('İmbatlı', 'İmbatlı'),
        ('İnönü', 'İnönü'),
        ('Latife Hanım', 'Latife Hanım'),
        ('Mavişehir', 'Mavişehir'),
        ('Mustafa Kemal', 'Mustafa Kemal'),
        ('Nergiz', 'Nergiz'),
        ('Örnekköy', 'Örnekköy'),
        ('Sancaklı', 'Sancaklı'),
        ('Şemikler', 'Şemikler'),
        ('Tersane', 'Tersane'),
        ('Tuna', 'Tuna'),
        ('Yalı', 'Yalı'),
        ('Yamanlar', 'Yamanlar'),
        ('Zübeyde Hanım', 'Zübeyde Hanım'),
    ])
    # M2 Brüt
    m2_brut = models.PositiveIntegerField()
    # Oda Sayısı
    oda_sayisi = models.CharField(max_length=10, choices=[
        ('1+0', '1+0'),
        ('1+1', '1+1'),
        ('2+0', '2+0'),
        ('2+1', '2+1'),
        ('2+2', '2+2'),
        ('3+1', '3+1'),
        ('3+2', '3+2'),
        ('4+1', '4+1'),
        ('4+2', '4+2'),
        ('4+3', '4+3'),
        ('4+4', '4+4'),
        ('5+1', '5+1'),
        ('5+2', '5+2'),
    ])
    # Bina Yaşı
    bina_yasi = models.CharField(max_length=20, choices=[
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('5-10', '5-10 Arası'),
        ('11-15', '11-15 Arası'),
        ('16-20', '16-20 Arası'),
        ('21-25', '21-25 Arası'),
        ('25+', '25 ve üzeri'),
    ])
    # Bulunduğu kat
    bulunduğu_kat = models.PositiveIntegerField()
    # Kat sayısı
    kat_sayisi = models.PositiveIntegerField()
    # Isıtma Türü
    isitma_turu = models.CharField(max_length=50, choices=[
        ('Yok', 'Yok'),
        ('Soba', 'Soba'),
        ('Doğalgaz', 'Doğalgaz'),
        ('Merkezi', 'Merkezi'),
        ('Kombi (Doğalgaz)', 'Kombi (Doğalgaz)'),
        ('Kombi (Elektrik)', 'Kombi (Elektrik)'),
        ('Yerden ısıtma', 'Yerden ısıtma'),
        ('Klima', 'Klima'),
    ])
    # Banyo Sayısı
    banyo_sayisi = models.CharField(max_length=10, choices=[
        ('Yok', 'Yok'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ])
    # Balkon
    balkon = models.BooleanField(default=False)  # Var Yok checkbox
    # Asansör
    asansor = models.BooleanField(default=False)  # Var Yok checkbox
    # Eşya Durumu
    esya_durumu = models.CharField(max_length=10, choices=[
        ('Eşyalı', 'Eşyalı'),
        ('Eşyasız', 'Eşyasız'),
    ])
    # Kullanım Durumu
    kullanim_durumu = models.CharField(max_length=20, choices=[
        ('Boş', 'Boş'),
        ('Kiracılı', 'Kiracılı'),
        ('Mülk sahibi', 'Mülk sahibi'),
    ])
    # Kimden
    kimden = models.CharField(max_length=50, choices=[
        ('Sahibinden', 'Sahibinden'),
        ('Emlak ofisinden', 'Emlak ofisinden'),
        ('Bankadan', 'Bankadan'),
        ('İnşaat firmasından', 'İnşaat firmasından'),
    ])
    # İlan tarihi
    ilan_tarihi = models.DateField()
    # Fiyat
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def formatted_fiyat(self):
        if self.fiyat >= 1000000:  # Milyonlar için
            return f"{self.fiyat / 1000000:.2f}M TL"  # 3.5M TL
        elif self.fiyat >= 1000:  # Binler için
            return f"{self.fiyat / 1000:.2f}K TL"  # 3.5K TL
        else:
            return f"{self.fiyat:.0f} TL"  # TL olarak göster
    # Fotoğraflar
    foto1 = models.ImageField(upload_to='ilan_fotoğrafları/', blank=True, null=True)
    foto2 = models.ImageField(upload_to='ilan_fotoğrafları/', blank=True, null=True)
    foto3 = models.ImageField(upload_to='ilan_fotoğrafları/', blank=True, null=True)
    foto4 = models.ImageField(upload_to='ilan_fotoğrafları/', blank=True, null=True)
    foto5 = models.ImageField(upload_to='ilan_fotoğrafları/', blank=True, null=True)
    foto6 = models.ImageField(upload_to='ilan_fotoğrafları/', blank=True, null=True)

    # User ile ilişki
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ilanlar')

    def __str__(self):
        return self.ilan_basligi


from django.db import models
from django.utils import timezone

class Musteri(models.Model):
    ilan = models.ForeignKey('Ilan', on_delete=models.CASCADE)
    konusulanTarih = models.DateField()
    musteriAdi = models.CharField(max_length=255)
    musteriNo = models.CharField(max_length=50)
    gorduMu = models.BooleanField(choices=[(True, 'Gördü'), (False, 'Görmedi')], default=False)
    teklif = models.BooleanField(choices=[(True, 'Verdi'), (False, 'Vermedi')], default=False)
    mesaj = models.TextField()
    songuncellemeTarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.musteriAdi} - {self.ilan}"

