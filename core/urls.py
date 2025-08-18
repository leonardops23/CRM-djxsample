from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Clientes
    path('clientes/', views.ClienteListView.as_view(), name='cliente_lista'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_crear'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detalle'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_editar'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_eliminar'),
    
    # Oportunidades
    path('oportunidades/', views.OportunidadListView.as_view(), name='oportunidad_lista'),
    path('oportunidades/nueva/', views.OportunidadCreateView.as_view(), name='oportunidad_crear'),
    path('oportunidades/<int:pk>/', views.OportunidadDetailView.as_view(), name='oportunidad_detalle'),
    path('oportunidades/<int:pk>/editar/', views.OportunidadUpdateView.as_view(), name='oportunidad_editar'),
    path('oportunidades/<int:pk>/eliminar/', views.OportunidadDeleteView.as_view(), name='oportunidad_eliminar'),
    
    # Tareas
    path('tareas/', views.TareaListView.as_view(), name='tarea_lista'),
    path('tareas/nueva/', views.TareaCreateView.as_view(), name='tarea_crear'),
    path('tareas/<int:pk>/', views.TareaDetailView.as_view(), name='tarea_detalle'),
    path('tareas/<int:pk>/editar/', views.TareaUpdateView.as_view(), name='tarea_editar'),
    path('tareas/<int:pk>/completar/', views.completar_tarea, name='tarea_completar'),
    
    # Contactos
    path('contactos/nuevo/', views.ContactoCreateView.as_view(), name='contacto_crear'),
    path('clientes/<int:cliente_id>/contacto/', views.crear_contacto_cliente, name='crear_contacto_cliente'),
]
