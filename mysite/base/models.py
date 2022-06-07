from django.db import models

class Item(models.Model):
    nombre = models.CharField(max_length=200)
    creado = models.DateField(auto_now_add=True)
