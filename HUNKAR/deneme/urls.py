from django.urls import path
from . import views

urlpatterns = [
    path('deneme/',views.denemeListe,name='denemeListe')
]
