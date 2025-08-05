from django.db import models
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def short_description(self):
        return self.description[:100] + '...' if self.description else 'No description'

    def __str__(self):
        return f"{self.name} ({self.email})"
