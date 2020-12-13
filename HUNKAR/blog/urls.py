from django.urls import path
from . import views

urlpatterns = [
    path('gonderi/',views.gonderiListe,name='gonderiListe')
]
