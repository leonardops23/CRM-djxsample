from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import Cliente, Oportunidad, Tarea, Contacto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'empresa', 'direccion', 'tipo', 'estado', 'notas']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
            'notas': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('telefono', css_class='form-group col-md-6 mb-0'),
                Column('empresa', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('tipo', css_class='form-group col-md-6 mb-0'),
                Column('estado', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'direccion',
            'notas',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = ['titulo', 'cliente', 'descripcion', 'valor', 'probabilidad', 'estado', 'prioridad', 'fecha_cierre_estimada']
        widgets = {
            'fecha_cierre_estimada': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'titulo',
            'cliente',
            'descripcion',
            Row(
                Column('valor', css_class='form-group col-md-4 mb-0'),
                Column('probabilidad', css_class='form-group col-md-4 mb-0'),
                Column('fecha_cierre_estimada', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('estado', css_class='form-group col-md-6 mb-0'),
                Column('prioridad', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'tipo', 'cliente', 'oportunidad', 'fecha_vencimiento']
        widgets = {
            'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'titulo',
            'tipo',
            'descripcion',
            Row(
                Column('cliente', css_class='form-group col-md-6 mb-0'),
                Column('oportunidad', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'fecha_vencimiento',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['cliente', 'oportunidad', 'tipo', 'asunto', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('cliente', css_class='form-group col-md-6 mb-0'),
                Column('oportunidad', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('tipo', css_class='form-group col-md-6 mb-0'),
                Column('asunto', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'descripcion',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )
