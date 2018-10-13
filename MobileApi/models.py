from django.db import models

# Create your models here.

class RecommendedItems(models.Model):
    ProductId=models.CharField(max_length=1000)
 

    def __str__(self):
        return self.ProductId


