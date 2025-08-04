from django.urls import path
from . import views

app_name = 'lead'

urlpatterns = [
    path('add-lead/', views.add_lead, name='add_lead'),
    path('list-lead/', views.list_lead, name='list_lead'),
    path('<int:lead_id>/', views.leads_detail, name='leads_detail'),
    path('<int:id>/delete/', views.leads_delete, name='leads_delete'),
]
