from django import forms
from .models import Lead

class AddLeadForm(forms.ModelForm):
    """
    Formulario para agregar una nueva lead.
    """
    class Meta:
        model = Lead
        fields = ['name', 'email', 'description', 'priority', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-md', 'rows': 3}),
            'priority': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
            'status': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
        }
