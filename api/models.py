from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)


