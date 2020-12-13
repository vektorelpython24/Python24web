from django.shortcuts import render
from .models import GonderiModel

def gonderiListe(request):
    gonderiler=GonderiModel.objects.all()
    return render(request,"blog/liste.html",{"gonderis":gonderiler})