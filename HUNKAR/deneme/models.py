from django.db import models
from django.utils import timezone

class DenemeModel(models.Model):
    #yazar = models.models.ForeignKey("auth.user", on_delete=models.CASCADE)
    isim = models.CharField(max_length = 100,verbose_name="İsim")
    soyisim = models.TextField(max_length = 100,verbose_name="Soyisim")
    telefon = models.TextField(verbose_name="Telefon", max_length=11)
    tarih = models.DateField(null=True,blank=True,verbose_name="Tarih")
    
    def kaydet(self):
        self.tarih = timezone.now()
        self.save()

    def __str__(self):
        return self.telefon
