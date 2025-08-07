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
        if self.description:
            description_text = str(self.description)
            return description_text[:100] + '...'
        return 'No description'

    def __str__(self):
        return f"{self.name} ({self.email})"
