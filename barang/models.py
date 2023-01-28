from django.db import models

# Create your models here.

class barang(models.Model):
    name = models.CharField(max_length=255)
    qty = models.IntegerField()
    price = models.IntegerField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
