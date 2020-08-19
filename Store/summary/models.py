from django.db import models


class SumItems(models.Model):
    user_name = models.CharField(max_length=50)
    selected_items = models.TextField(null=True)
    items_cost = models.TextField(null=True, default=0)
    items_weight = models.TextField(null=True, default=0)
    items_price = models.TextField(null=True, default=0)
    total_cost = models.FloatField(null=True, default=0)
    date_created = models.DateField(null=True)



