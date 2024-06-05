from django import forms

from .models import *
from datetime import datetime

class CitaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese su teléfono'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electrónico'}),
            'fecha_cita': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'fecha_cita',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-toggle': 'datetimepicker',
                'data-target': '#fecha_cita'
            }),
            'hora_cita': forms.TimeInput(format='%H:%M', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'hora_cita',
                'value': datetime.now().strftime('%H:%M'),
                'data-toggle': 'datetimepicker',
                'data-target': '#hora_cita'
            }),
                       'psicologo': forms.Select(choices=[
                ('Psicologo 1','Juan Carlos Ortega Ruiz (Psicología de la salud)'),
                ('Psicologa 2','Fernanda Ramirez Gonzalez (Psicología de pareja)'),
                ('Psicologa 3','Julia Isabel Hernandez (Psicología de familia)'),
                ('Psicologo 4','Raul Jimenez Bartolo (Sexologo)')]),
            'proposito': forms.Textarea(attrs={'placeholder': 'Ingrese el propósito de la cita', 'rows': 3}),
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                data = super().save().toJSON()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
