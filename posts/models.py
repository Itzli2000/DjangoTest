from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Post(models.Model):
  titulo = models.CharField(max_length=150)
  contenido = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
  actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self): #Python 2 __unicode__ / Python 3 __str__
    return self.titulo