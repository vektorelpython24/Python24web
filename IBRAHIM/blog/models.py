from django.db import models
from django.utils import timezone

class GonderiModel(models.Model):
    # yazar = models.ForeingKey('auth.user',on_delete=models.CASCADE)
    baslik = models.CharField(max_length=100,verbose_name="Başlık") 
    yazi = models.TextField(verbose_name="Yazı")
    eposta=models.EmailField(verbose_name="E-Mail", max_length=254,default="aa@aa.com")
    kayit_zaman = models.DateTimeField(default=timezone.now,verbose_name="Kayıt Zamanı")
    yayim_zaman = models.DateTimeField(null=True,blank=True,verbose_name="Yayım Zamanı")
    telefonnno = models.BigIntegerField(verbose_name="Telefon numaranız",max_length=10,default="05000000000")

    def yayimla(self):
        self.yayim_zaman = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik