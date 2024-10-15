from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from rest_framework import routers
from .views import TaskView

# api vers
router = routers.DefaultRouter()
router.register(r'tasks', TaskView, 'tasks')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Tasks API'))
]

"""
GET
POST
PUT
DELETE
"""
