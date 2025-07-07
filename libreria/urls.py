from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # ruta para nosotros
    path('nosotros/', views.nosotros, name='nosotros'),
    # ruta para libros
    path('libros/', views.libros, name='libros'),
    # ruta para crear libro
    path('libros/crear/', views.crear, name='crear'),
    # ruta para editar libro
    path('libros/editar/<int:id>/', views.editar, name='editar'),
]
