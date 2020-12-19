from django.shortcuts import render
import sys
sys.path.append(r"EDIZ")
from blog.models import GonderiModel

def anasayfaBilgi(request):
    gonderiler =  GonderiModel.objects.all()
    return render(request,"anasayfa.html",{"gonderis":gonderiler})