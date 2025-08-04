from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AddLeadForm
from .models import Lead

@login_required
def list_lead(request):
    """
    Vista para listar todas las leads del usuario.
    """
    leads = Lead.objects.filter(created_by=request.user)
    return render(request, 'lead/list_lead.html', {'leads': leads})

@login_required
def leads_delete(request, id):
    lead = Lead.objects.filter(id=id, created_by=request.user).first()
    if lead:
        lead.delete()
    return redirect('lead:list_lead')

@login_required
def leads_detail(request, lead_id):
    """
    Vista para mostrar los detalles de una lead.
    """
    lead = Lead.objects.filter(id=lead_id, created_by=request.user).first()
    if not lead:
        return redirect('lead:list_lead')
    return render(request, 'lead/leads_detail.html', {'lead': lead})

@login_required
def add_lead(request):
    """
    Vista para agregar una nueva lead.
    """
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            return redirect('lead:list_lead')
    else:
        form = AddLeadForm()
    return render(request, 'lead/add_lead.html', {'form': form})
