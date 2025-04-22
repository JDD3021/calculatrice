from django.db import models

# Create your models here.

class Calcul(models.Model):
    """Model representing an Calcul."""
    expression = models.CharField(max_length=255, default='')
    resultat = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expression}: {self.resultat}"
