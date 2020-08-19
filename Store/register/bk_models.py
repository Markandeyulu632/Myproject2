from django.db import models


class StoreUsers(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    userid = models.CharField(max_length=50, primary_key=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.TextField()





