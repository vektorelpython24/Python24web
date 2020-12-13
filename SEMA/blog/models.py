from django.db import models
from django.utils import timezone

class GonderiModel(models.Model):
    # yazar = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    baslik = models.CharField(max_length=200,verbose_name="Başlık")
    yazi = models.TextField(verbose_name="Yazı")
    kayit_zaman = models.DateTimeField(default=timezone.now,verbose_name="Kayıt Zamanı")
    yayim_tarihi = models.DateTimeField(null=True,blank=True,verbose_name="Yayım Zamanı")

    def yayimla(self):
        self.yayim_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik
