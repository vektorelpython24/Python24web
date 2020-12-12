from django.db import models
from django.utils import timezone

class GonderiModel(models.model):
    # yazar = model.ForeingKey('auth.user',on_delete=models.CASCADE)
    title = models.Charfield(max_length=100) 
    text = models.TextField()
    kayit_zaman = models.DateTimeField(default=timezone.now)
    yayim_tarihi=models.DateTimeField(null=True,blank=True)

    def yayimla(self):
        self.yayim_tarihi = timezone.now()
        self.save()