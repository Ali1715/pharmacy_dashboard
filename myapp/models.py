from django.db import models


class Factura(models.Model):
    nit = models.BigIntegerField()
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    nota = models.CharField(max_length=255)
    tipo = models.CharField(max_length=1)
    clienteID = models.IntegerField()
    usuarioID = models.IntegerField()

    def __str__(self):
        return f'Factura {self.id}'