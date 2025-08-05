from django.urls import path
from . import views

app_name = 'lead'

urlpatterns = [
    path('add-lead/', views.add_lead, name='add_lead'),
    path('list-lead/', views.list_lead, name='list_lead'),
    path('<int:lead_id>/', views.lead_detail, name='lead_detail'),
    path('<int:lead_id>/edit/', views.lead_edit, name='lead_edit'),
    path('<int:lead_id>/delete/', views.lead_delete, name='lead_delete'),
    path('<int:lead_id>/convert/', views.convert_to_client, name='lead_convert'),
]
