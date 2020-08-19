from django.db import models


class Products(models.Model):
    product_code = models.CharField(max_length=10)
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_image = models.ImageField()

