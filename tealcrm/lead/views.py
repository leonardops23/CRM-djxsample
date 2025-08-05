from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from client.models import Client, models

from .forms import AddLeadForm
from .models import Lead

@login_required
def list_lead(request):
    """
    Vista para listar todas las leads del usuario.
    """
    leads = Lead.objects.filter(created_by=request.user, convert_to_client=False)

    return render(request, 'lead/list_lead.html', {'leads': leads})

@login_required
def lead_delete(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id, created_by=request.user)

    if lead:
        lead.delete()
        messages.success(request, 'Lead eliminada correctamente.')
    else:
        messages.error(request, 'No se pudo eliminar la lead.')
    return redirect('lead:list_lead')

@login_required
def lead_detail(request, lead_id):
    """
    Vista para mostrar los detalles de una lead.
    """
    lead = get_object_or_404(Lead, id=lead_id, created_by=request.user)
    if not lead:
        return redirect('lead:list_lead')
    return render(request, 'lead/lead_detail.html', {'lead': lead})

@login_required
def lead_edit(request, lead_id):
    """
    Vista para editar una lead existente.
    """
    lead = get_object_or_404(Lead, id=lead_id, created_by=request.user)
    if not lead:
        return redirect('lead:list_lead')
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lead actualizada correctamente.')
            return redirect('lead:list_lead')
    else:
        form = AddLeadForm(instance=lead)
    return render(request, 'lead/lead_edit.html', {'form': form})

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
            messages.success(request, 'Lead agregada correctamente.')
            return redirect('lead:list_lead')
    else:
        form = AddLeadForm()
    return render(request, 'lead/add_lead.html', {'form': form})

@login_required
def convert_to_client(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id, created_by=request.user)
    if lead.convert_to_client:
        messages.error(request, 'La lead ya ha sido convertida a cliente.')
        return redirect('lead:list_lead')

    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        created_by=request.user,
        created_at=lead.created_at,
        modified_at=lead.modified_at
    )
    
    lead.convert_to_client = True
    lead.save()

    messages.success(request, 'Lead convertida a cliente correctamente.')
    return redirect('lead:list_lead')
