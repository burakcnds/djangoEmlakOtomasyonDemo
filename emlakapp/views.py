from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ilan
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Ilan
from .forms import IlanForm

@login_required  # Bu dekoratör, kullanıcı oturum açmamışsa yönlendirme yapar

def main(request):
    # Kullanıcının ilanlarını al
    ilanlar = Ilan.objects.filter(user=request.user)

    # Filtre parametrelerini istekten al
    location = request.GET.get('mahalle')  
    rooms = request.GET.get('oda_sayisi')  
    heating = request.GET.get('isitma_turu')  
    sort = request.GET.get('sort')
    kullanimDurumu = request.GET.get('kullanim_durumu')
    kimden = request.GET.get('kimden')

    # Debug bilgilerini yazdır
    print("Location:", location)
    print("Rooms:", rooms)
    print("Heating:", heating)
    print("Sort:", sort)
    print("Kullanım Durumu:", kullanimDurumu)
    print("Kimden:", kimden)

    # Filtreleri uygula
    if location or rooms or heating or kullanimDurumu or kimden:
        if location:
            ilanlar = ilanlar.filter(mahalle=location)
            print("Filtered by location:", location)
        if rooms:
            ilanlar = ilanlar.filter(oda_sayisi=rooms)
            print("Filtered by rooms:", rooms)
        if heating:
            ilanlar = ilanlar.filter(isitma_turu=heating)
            print("Filtered by heating:", heating)
        if kullanimDurumu:
            ilanlar = ilanlar.filter(kullanim_durumu=kullanimDurumu)
            print("Filtered by kullanim durumu:", kullanimDurumu)
        if kimden:
            ilanlar = ilanlar.filter(kimden=kimden)
            print("Filtered by kimden:", kimden)

    # Sıralama uygula
    if sort:
        if sort == 'fiyat-asc':
            ilanlar = ilanlar.order_by('fiyat')
        elif sort == 'fiyat-desc':
            ilanlar = ilanlar.order_by('-fiyat')
        elif sort == 'tarih-asc':
            ilanlar = ilanlar.order_by('ilan_tarihi')
        elif sort == 'tarih-desc':
            ilanlar = ilanlar.order_by('-ilan_tarihi')

    print("Filtered results:", ilanlar)  # Sonuçları yazdır

    # Seçenekleri içeren context'i hazırla
    context = {
        'ilanlar': ilanlar,
        'mahalle_choices': Ilan._meta.get_field('mahalle').choices,
        'oda_sayisi_choices': Ilan._meta.get_field('oda_sayisi').choices,
        'bina_yasi_choices': Ilan._meta.get_field('bina_yasi').choices,
        'isitma_turu_choices': Ilan._meta.get_field('isitma_turu').choices,
        'banyo_sayisi_choices': Ilan._meta.get_field('banyo_sayisi').choices,
        'esya_durumu_choices': Ilan._meta.get_field('esya_durumu').choices,
        'kullanim_durumu_choices': Ilan._meta.get_field('kullanim_durumu').choices,
        'kimden_choices': Ilan._meta.get_field('kimden').choices,
        'current_filters': {
            'mahalle': location,
            'oda_sayisi': rooms,
            'isitma_turu': heating,
            'kullanim_durumu': kullanimDurumu,
            'kimden': kimden,
            'sort': sort,
        }
    }
    return render(request, 'main.html', context)




def ilanEkle(request):
    if request.method == "POST":
        form = IlanForm(request.POST, request.FILES)
        if form.is_valid():
            yeni_ilan = form.save(commit=False)
            yeni_ilan.user = request.user  # Kullanıcıyı ata
            yeni_ilan.save()  # İlanı kaydet
            return redirect('main')  # Başarılı ekleme sonrası yönlendirme
        else:
            print(form.errors)  # Hataları yazdırarak kontrol et
    else:
        form = IlanForm()  # İlk yüklemede boş form

    # Choices'ları context'e ekle
    context = {
        'form': form,
        'mahalle_choices': Ilan._meta.get_field('mahalle').choices,
        'oda_sayisi_choices': Ilan._meta.get_field('oda_sayisi').choices,
        'bina_yasi_choices': Ilan._meta.get_field('bina_yasi').choices,
        'isitma_turu_choices': Ilan._meta.get_field('isitma_turu').choices,
        'banyo_sayisi_choices': Ilan._meta.get_field('banyo_sayisi').choices,
        'esya_durumu_choices': Ilan._meta.get_field('esya_durumu').choices,
        'kullanim_durumu_choices': Ilan._meta.get_field('kullanim_durumu').choices,
        'kimden_choices': Ilan._meta.get_field('kimden').choices,
    }

    return render(request, 'ilanEkle.html', context)  # Formu render et


# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Ilan
import json
@csrf_exempt  # CSRF korumasını geçici olarak devre dışı bırak
def delete_ilans(request):
    if request.method == "POST":
        # JSON gövdesinden ilan ID'lerini al
        try:
            ilan_ids = request.body.decode('utf-8')  # JSON gövdesini al
            ilan_ids = json.loads(ilan_ids).get('ilan_ids', [])  # ID'leri çıkar
            # Seçilen ilanları sil
            Ilan.objects.filter(id__in=ilan_ids).delete()
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
    return JsonResponse({"success": False}, status=400)




from django.shortcuts import render, get_object_or_404, redirect
from .models import Ilan
from .forms import IlanForm

def edit_ilan(request, ilan_id):
    ilan = get_object_or_404(Ilan, id=ilan_id)
    
    if request.method == "POST":
        form = IlanForm(request.POST, request.FILES, instance=ilan)
        if form.is_valid():
            form.save()
            return redirect('main')  # Redirect to the listings page after saving
    else:
        form = IlanForm(instance=ilan)

    return render(request, 'ilanDuzenle.html', {'form': form, 'ilan': ilan})

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Musteri  # Musteri modelini içeri aktarıyoruz

def musteri(request):
    """Tüm müşteri kayıtlarını görüntüler."""
    musteriler = Musteri.objects.all()
    return render(request, 'musteri.html', {'musteriler': musteriler})

def musteriler_list(request):
    """Tüm müşteri kayıtlarını bir liste halinde görüntüler."""
    musteriler = Musteri.objects.all()
    return render(request, 'your_template.html', {'musteriler': musteriler})

@csrf_exempt  # CSRF korumasını devre dışı bırakıyoruz
def delete_musteriler(request):
    """Seçilen müşteri kayıtlarını siler."""
    if request.method == 'POST':
        data = json.loads(request.body)
        musteri_ids = data.get('musteri_ids', [])
        if musteri_ids:
            Musteri.objects.filter(id__in=musteri_ids).delete()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def get_musteri(request, musteri_id):
    """Belirli bir müşterinin bilgilerini döner."""
    musteri = get_object_or_404(Musteri, id=musteri_id)
    return JsonResponse({
        'id': musteri.id,
        'musteriAdi': musteri.musteriAdi,
        'musteriNo': musteri.musteriNo,
        'gorduMu': musteri.gorduMu,
        'teklif': musteri.teklif,
        'mesaj': musteri.mesaj,
        'songuncellemeTarihi': musteri.songuncellemeTarihi.isoformat(),  # İsteğe bağlı
    })

@csrf_exempt  # CSRF korumasını devre dışı bırakıyoruz
def edit_musteri(request, musteri_id):
    """Belirli bir müşterinin bilgilerini günceller."""
    if request.method == 'POST':
        data = json.loads(request.body)
        musteri = get_object_or_404(Musteri, id=musteri_id)

        # Verileri güncelle
        musteri.musteriAdi = data.get('musteriAdi', musteri.musteriAdi)  # Eski değeri koru
        musteri.musteriNo = data.get('musteriNo', musteri.musteriNo)  # Eski değeri koru
        musteri.gorduMu = data.get('gorduMu', musteri.gorduMu) == 'True'
        musteri.teklif = data.get('teklif', musteri.teklif) == 'True'
        musteri.mesaj = data.get('mesaj', musteri.mesaj)  # Eski değeri koru
        musteri.save()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
# MÜŞTERİ FORMU 


from django.shortcuts import render, get_object_or_404, redirect
from .models import Ilan  # İlan modelini import edin
from .forms import MusteriForm  # Formu import edin

def musteri_ekle(request):
    ilan = None  # İlan başlangıçta None

    # GET isteği ile ilan ID'sini al
    ilan_id = request.GET.get('ilan_id')
    if ilan_id:
        ilan = get_object_or_404(Ilan, id=ilan_id)  # İlanı al

    if request.method == 'POST':
        form = MusteriForm(request.POST)
        if form.is_valid():
            musteri = form.save(commit=False)  # Müşteriyi kaydetmeden önce oluştur
            if ilan:
                musteri.ilan = ilan  # Müşteriyi ilan ile ilişkilendir
            musteri.save()  # Müşteriyi kaydet
            print("Müşteri başarıyla eklendi!")
            return redirect('musteri')  # 'musteri' URL'sine yönlendir
        else:
            print(form.errors)  # Hata varsa yazdır

    else:
        form = MusteriForm()  # Formu oluştur

    return render(request, 'musteriEkle.html', {'form': form, 'ilan': ilan})  # Şablona ilanı gönder


def ilanDetay(request, id):
    ilan = get_object_or_404(Ilan, id=id)
    return render(request, 'ilanDetay.html', {'ilan': ilan})



