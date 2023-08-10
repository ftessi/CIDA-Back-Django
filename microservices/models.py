from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    privileges = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    refreshtoken = models.CharField(max_length=500, unique=True)

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username

class Product(models.Model):
    codigo = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    ean = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    pvp = models.CharField(max_length=50)

    class Meta:
        db_table = 'products'