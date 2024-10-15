from django import forms
from .models import Ilan,Musteri

class IlanForm(forms.ModelForm):
    class Meta:
        model = Ilan
        fields = ['ilan_basligi', 'mahalle', 'm2_brut', 'oda_sayisi', 'bina_yasi', 'bulunduğu_kat', 'kat_sayisi', 
                  'isitma_turu', 'banyo_sayisi', 'balkon', 'asansor', 'esya_durumu', 'kullanim_durumu', 
                  'kimden', 'ilan_tarihi', 'foto1', 'foto2', 'foto3', 'foto4', 'foto5', 'foto6', 'fiyat']
from django import forms
from .models import Musteri

class MusteriForm(forms.ModelForm):
    class Meta:
        model = Musteri
        fields = ['ilan', 'konusulanTarih', 'musteriAdi', 'musteriNo', 'gorduMu', 'teklif', 'mesaj']
        widgets = {
            'ilan': forms.Select(attrs={'class': 'form-control'}),
            'konusulanTarih': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'musteriAdi': forms.TextInput(attrs={'class': 'form-control'}),
            'musteriNo': forms.TextInput(attrs={'class': 'form-control'}),
            'gorduMu': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'teklif': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mesaj': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(MusteriForm, self).__init__(*args, **kwargs)
        self.fields['teklif'].required = False  # Teklif boş geçilebilir
        self.fields['gorduMu'].required = False  # Gördü Mü boş geçilebilir