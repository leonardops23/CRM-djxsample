from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('', views.clients_list, name='client_list'),
    path('<int:client_id>/', views.clients_detail, name='client_detail'),
    path('add/', views.clients_add, name='clients_add'),
    path('delete/<int:client_id>/', views.client_delete, name='client_delete'),
    path('update/<int:client_id>/', views.client_update, name='client_update'),
]
