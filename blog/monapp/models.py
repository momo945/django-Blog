from django.db import models


class Livre(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='livres/')
    
    def __str__(self):
        return self.titre

# Create your models here.
