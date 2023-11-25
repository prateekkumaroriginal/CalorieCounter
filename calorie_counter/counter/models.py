from django.db import models
from django.contrib.auth.models import User

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
    
class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} --> {self.food_consumed}"