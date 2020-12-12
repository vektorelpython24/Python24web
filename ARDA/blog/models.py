from django.db import models
from django.utils import timezone


class GonderiModel(models.model):
    #yazar=models.models.ForeignKey('auth.user', on_delete=models.CASCADE
    baslik=models.models.CharField(max_length=100)
    yazi=models.TextField()
    kayit_zaman=models.models.DateTimeField(default=timezone.now)
    yayim_tarihi=models.DateTimeField(null=True,blank=True)