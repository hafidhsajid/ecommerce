from django.db import models

# Create your models here.

class barang(models.Model):
    name = models.CharField(max_length=255)
    qty = models.IntegerField()
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}({self.qty}left)-${self.price} - last update {self.updated_at}'
