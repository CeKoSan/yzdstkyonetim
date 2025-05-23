
from django.db import models

class Kayit(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.ad} {self.soyad}"
