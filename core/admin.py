from django.contrib import admin
from .models import Cliente, Oportunidad, Tarea, Contacto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'empresa', 'tipo', 'estado', 'fecha_registro']
    list_filter = ['tipo', 'estado', 'fecha_registro']
    search_fields = ['nombre', 'email', 'empresa']
    list_editable = ['estado']

@admin.register(Oportunidad)
class OportunidadAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'cliente', 'valor', 'probabilidad', 'estado', 'fecha_creacion']
    list_filter = ['estado', 'prioridad', 'fecha_creacion']
    search_fields = ['titulo', 'cliente__nombre']
    list_editable = ['estado', 'probabilidad']

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'cliente', 'tipo', 'estado', 'fecha_vencimiento', 'asignado_a']
    list_filter = ['tipo', 'estado', 'fecha_vencimiento']
    search_fields = ['titulo', 'cliente__nombre']
    list_editable = ['estado']

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'tipo', 'asunto', 'fecha', 'usuario']
    list_filter = ['tipo', 'fecha']
    search_fields = ['cliente__nombre', 'asunto']
