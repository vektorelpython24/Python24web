from django.urls import path
from . import views

urlpatterns = [
    path('liste/',views.gonderiListe,name="gonderiListe"),
    path('detay/<int:pk>/',views.gonderiDetay,name="gonderiDetay"),
]
