from django.db import models
from django.utils import timezone


class GonderiModel(models.Model):
    #yazar=models.models.ForeignKey('auth.user', on_delete=models.CASCADE
    baslik=models.CharField(max_length=100)
    yazi=models.TextField()
    kayit_zaman= models.DateTimeField(default=timezone.now)
    yayim_zaman= models.DateTimeField(null=True,blank=True)

    def yayimla(self):
        self.yayim_zaman = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik