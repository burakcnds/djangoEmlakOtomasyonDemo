# Generated by Django 5.0 on 2024-10-07 13:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ilan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilan_basligi', models.CharField(max_length=255)),
                ('mahalle', models.CharField(choices=[('Aksoy', 'Aksoy'), ('Alaybey', 'Alaybey'), ('Atakent', 'Atakent'), ('Bahariye', 'Bahariye'), ('Bahçelievler', 'Bahçelievler'), ('Bahriye Üçok', 'Bahriye Üçok'), ('Bostanlı', 'Bostanlı'), ('Cumhuriyet', 'Cumhuriyet'), ('Dedebaşı', 'Dedebaşı'), ('Demirköprü', 'Demirköprü'), ('Donanmacı', 'Donanmacı'), ('Fikri Altay', 'Fikri Altay'), ('Goncalar', 'Goncalar'), ('İmbatlı', 'İmbatlı'), ('İnönü', 'İnönü'), ('Latife Hanım', 'Latife Hanım'), ('Mavişehir', 'Mavişehir'), ('Mustafa Kemal', 'Mustafa Kemal'), ('Nergiz', 'Nergiz'), ('Örnekköy', 'Örnekköy'), ('Sancaklı', 'Sancaklı'), ('Şemikler', 'Şemikler'), ('Tersane', 'Tersane'), ('Tuna', 'Tuna'), ('Yalı', 'Yalı'), ('Yamanlar', 'Yamanlar'), ('Zübeyde Hanım', 'Zübeyde Hanım')], max_length=50)),
                ('m2_brut', models.PositiveIntegerField()),
                ('oda_sayisi', models.CharField(choices=[('1+0', '1+0'), ('1+1', '1+1'), ('2+0', '2+0'), ('2+1', '2+1'), ('2+2', '2+2'), ('3+1', '3+1'), ('3+2', '3+2'), ('4+1', '4+1'), ('4+2', '4+2'), ('4+3', '4+3'), ('4+4', '4+4'), ('5+1', '5+1'), ('5+2', '5+2')], max_length=10)),
                ('bina_yasi', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('5-10', '5-10 Arası'), ('11-15', '11-15 Arası'), ('16-20', '16-20 Arası'), ('21-25', '21-25 Arası'), ('25+', '25 ve üzeri')], max_length=20)),
                ('bulunduğu_kat', models.PositiveIntegerField()),
                ('kat_sayisi', models.PositiveIntegerField()),
                ('isitma_turu', models.CharField(choices=[('Yok', 'Yok'), ('Soba', 'Soba'), ('Doğalgaz', 'Doğalgaz'), ('Merkezi', 'Merkezi'), ('Kombi (Doğalgaz)', 'Kombi (Doğalgaz)'), ('Kombi (Elektrik)', 'Kombi (Elektrik)'), ('Yerden ısıtma', 'Yerden ısıtma'), ('Klima', 'Klima')], max_length=50)),
                ('banyo_sayisi', models.CharField(choices=[('Yok', 'Yok'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10)),
                ('balkon', models.BooleanField(default=False)),
                ('asansor', models.BooleanField(default=False)),
                ('esya_durumu', models.CharField(choices=[('Eşyalı', 'Eşyalı'), ('Eşyasız', 'Eşyasız')], max_length=10)),
                ('kullanim_durumu', models.CharField(choices=[('Boş', 'Boş'), ('Kiracılı', 'Kiracılı'), ('Mülk sahibi', 'Mülk sahibi')], max_length=20)),
                ('kimden', models.CharField(choices=[('Sahibinden', 'Sahibinden'), ('Emlak ofisinden', 'Emlak ofisinden'), ('Bankadan', 'Bankadan'), ('İnşaat firmasından', 'İnşaat firmasından')], max_length=50)),
                ('ilan_tarihi', models.DateField()),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto1', models.ImageField(upload_to='ilan_fotoğrafları/')),
                ('foto2', models.ImageField(blank=True, null=True, upload_to='ilan_fotoğrafları/')),
                ('foto3', models.ImageField(blank=True, null=True, upload_to='ilan_fotoğrafları/')),
                ('foto4', models.ImageField(blank=True, null=True, upload_to='ilan_fotoğrafları/')),
                ('foto5', models.ImageField(blank=True, null=True, upload_to='ilan_fotoğrafları/')),
                ('foto6', models.ImageField(blank=True, null=True, upload_to='ilan_fotoğrafları/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ilanlar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Musteri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('konusulanTarih', models.DateField()),
                ('musteriAdi', models.CharField(max_length=255)),
                ('musteriNo', models.CharField(max_length=50)),
                ('gorduMu', models.BooleanField(choices=[(True, 'Gördü'), (False, 'Görmedi')], default=False)),
                ('teklif', models.BooleanField(choices=[(True, 'Verdi'), (False, 'Vermedi')], default=False)),
                ('mesaj', models.TextField()),
                ('songuncellemeTarihi', models.DateTimeField(auto_now=True)),
                ('ilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emlakapp.ilan')),
            ],
        ),
    ]
