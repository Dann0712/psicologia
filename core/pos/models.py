from django.db import models
from django.forms.models import model_to_dict

class Cita(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    telefono = models.CharField(max_length=10, null=True, blank=True, verbose_name='Teléfono')
    correo_electronico = models.CharField(max_length=50, null=True, blank=True, verbose_name='Correo electrónico')
    fecha_cita = models.DateField(verbose_name='Fecha de la cita')
    hora_cita = models.TimeField(verbose_name='Hora de la cita')
    psicologo = models.CharField(max_length=150, verbose_name='Psicólogo')
    proposito = models.TextField(verbose_name='Propósito de la cita')

    def __str__(self):
        return self.get_full_cita()

    def get_full_cita(self):
        return f'Cita para {self.nombres} con {self.psicologo} el {self.fecha_cita.strftime("%Y-%m-%d")} a las {self.hora_cita.strftime("%H:%M")}'

    def fecha_cita_format(self):
        return self.fecha_cita.strftime('%Y-%m-%d')

    def hora_cita_format(self):
        return self.hora_cita.strftime('%H:%M')

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha_cita'] = self.fecha_cita_format()
        item['hora_cita'] = self.hora_cita_format()
        return item

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
