from django.db import models
from django.utils import timezone
class IletiModel(models.Model):
    bilgi = models.CharField(max_length=100,verbose_name="İsim Soyisim")
    eposta = models.EmailField(max_length=100,verbose_name="E Posta")
    mesaj = models.TextField(verbose_name="Mesajınız")
    gonderi_tar = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.bilgi