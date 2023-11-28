from django.db import models


class Fechas(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
   

    def __str__(self):
        return f'Inicio: {self.fecha_inicio}, Fin: {self.fecha_final}'