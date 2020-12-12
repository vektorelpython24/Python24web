from django.db import models
from django.utils import timezone

class GonderiModel(models.Model):
    # yazar = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    kayit_zaman = models.DateTimeField(default=timezone.now)
    yayim_tarihi = models.DateTimeField(null=True,blank=True)

    def yayimla(self):
        self.yayim_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik
