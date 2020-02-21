from django.db import models

# Create your models here.

imagen = models.ImageField(upload_to="pic",null=True),

class Consolas(models.Model):
    nombre=models.CharField(max_length=15)
    modelo=models.CharField(max_length=15)
    precio=models.IntegerField(max_length=15)
    def __str__(self):
        return self.modelo
