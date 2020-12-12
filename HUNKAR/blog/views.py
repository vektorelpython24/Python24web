from django.shortcuts import render
from .model import GonderiModel

def gonderiListe(request):
    return render(request,'blog/liste.html',{})
