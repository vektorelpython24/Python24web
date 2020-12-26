from django.shortcuts import render,get_object_or_404,redirect
from .models import GonderiModel
from .forms import GonderiForm
from django.utils import timezone

def gonderiListe(request):
    gonderiler =  GonderiModel.objects.all()
    return render(request,"blog/liste.html",{"gonderis":gonderiler})


def gonderiDetay(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    return render(request,"blog/gonderiDetay.html",{"gonderi":gonderi})


def yeniGonderi(request):
    if request.method == "POST"
       form = GonderiForm(request.POST)
       if form.is_valid():
           gonderi = form.save(commit=False)
           gonderi.yayim_tarihi = timezone.now()
           gonderi.save()
           return redirect("gonderiDetay",pk=gonderi.pk)
    else:
        form = GonderiForm()
    return render(request,'blog/yenigonderi.html',{"form":form})

def gonderiDuzenle(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    if request.method == "POST":
        form = GonderiForm(request.POST,instance=gonderi)
        if form.is_valid():
            gonderi = form.save(commit=False)
            gonderi.yayim_tarihi = timezone.now()
            gonderi.save()
            return redirect("gonderiDetay",pk=gonderi.pk)
    else:
        form = GonderiForm(instance=gonderi)
    return render(request,'blog/yenigonderi.html',{"form":form})
