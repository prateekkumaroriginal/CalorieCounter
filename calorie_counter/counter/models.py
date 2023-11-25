from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    carbs = models.DecimalField(max_digits=10, decimal_places=1)
    protein = models.DecimalField(max_digits=10, decimal_places=1)
    fats = models.DecimalField(max_digits=10, decimal_places=1)
    calories = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name
    