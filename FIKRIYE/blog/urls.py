from django.urls import path
from . import views

urlpatterns = [
    path('liste/',views.gonderiListe,name="gonderiListe")
]
