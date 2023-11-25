from django.db import models

# Create your models here.
class Order(models.Model):

    product_category = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=10)
    shipping_cost = models.CharField(max_length=10)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        app_label = 'myapp'

        