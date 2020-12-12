from django.shortcuts import render
from .models import GonderiModel

def gonderiListe(request):
    return render(request,"blog/liste.html",{})
