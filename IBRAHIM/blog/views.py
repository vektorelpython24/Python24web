from django.shortcuts import render,get_object_or_404
from .models import GonderiModel

def gonderiListe(request):
    gonderiler =  GonderiModel.objects.all()
    return render(request,"blog/liste.html",{"gonderis":gonderiler})


def gonderiDetay(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    return render(request,"blog/gonderiDetay.html",{"gonderi":gonderi})
