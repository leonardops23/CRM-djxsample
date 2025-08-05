from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path('<int:client_id>/', views.clients_detail, name='client_detail'),

]
