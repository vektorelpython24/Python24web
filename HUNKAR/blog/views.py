from django.shortcuts import render
from .models import GonderiModel

def gonderiListe(request):
    gonderiler = GonderiModel.objects.all()
    return render(request,'blog/liste.html',{"gonderis": gonderiler})
    
# 1. Uygulama oluştur
# 2. Proje ile ilişkilendir
# 3. Model Oluştur.
# 4. Modeli veritabanına aktar
# 5. Modeli admin paneli ile ilişkilendir
# 6. Commit Et
