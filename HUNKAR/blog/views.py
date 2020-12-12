from django.shortcuts import render

def gonderiListe(request):
    return render(request,'blog/liste.html',{})
