from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    author= models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self) :
        return f"{self.title} ({self.rating})"