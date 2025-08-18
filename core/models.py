from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Cliente(models.Model):
    TIPO_CHOICES = [
        ('persona', 'Persona Natural'),
        ('empresa', 'Empresa'),
    ]
    
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('prospecto', 'Prospecto'),
    ]
    
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    empresa = models.CharField(max_length=200, blank=True)
    direccion = models.TextField(blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='persona')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='prospecto')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True)
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return f"{self.nombre} ({self.email})"
    
    def get_absolute_url(self):
        return reverse('cliente_detalle', kwargs={'pk': self.pk})

class Oportunidad(models.Model):
    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('contactado', 'Contactado'),
        ('calificado', 'Calificado'),
        ('propuesta', 'Propuesta Enviada'),
        ('negociacion', 'En Negociación'),
        ('ganado', 'Ganado'),
        ('perdido', 'Perdido'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]
    
    titulo = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='oportunidades')
    descripcion = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    probabilidad = models.IntegerField(default=10, help_text="Probabilidad de cierre (%)")
    estado = models.CharField(max_length=12, choices=ESTADO_CHOICES, default='nuevo')
    prioridad = models.CharField(max_length=5, choices=PRIORIDAD_CHOICES, default='media')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre_estimada = models.DateField()
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Oportunidad'
        verbose_name_plural = 'Oportunidades'
    
    def __str__(self):
        return f"{self.titulo} - {self.cliente.nombre}"
    
    def get_absolute_url(self):
        return reverse('oportunidad_detalle', kwargs={'pk': self.pk})
    
    @property
    def valor_ponderado(self):
        return self.valor * (self.probabilidad / 100)

class Tarea(models.Model):
    TIPO_CHOICES = [
        ('llamada', 'Llamada'),
        ('email', 'Email'),
        ('reunion', 'Reunión'),
        ('seguimiento', 'Seguimiento'),
        ('otro', 'Otro'),
    ]
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=12, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='tareas')
    oportunidad = models.ForeignKey(Oportunidad, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_vencimiento = models.DateTimeField()
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_completada = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['fecha_vencimiento']
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
    
    def __str__(self):
        return f"{self.titulo} - {self.cliente.nombre}"
    
    def get_absolute_url(self):
        return reverse('tarea_detalle', kwargs={'pk': self.pk})

class Contacto(models.Model):
    TIPO_CHOICES = [
        ('llamada', 'Llamada'),
        ('email', 'Email'),
        ('reunion', 'Reunión'),
        ('mensaje', 'Mensaje'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contactos')
    oportunidad = models.ForeignKey(Oportunidad, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
    
    def __str__(self):
        return f"{self.tipo} - {self.cliente.nombre} - {self.fecha.strftime('%d/%m/%Y')}"
