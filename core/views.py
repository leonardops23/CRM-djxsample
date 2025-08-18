
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum, Q, Count
from django.utils import timezone
from datetime import timedelta

from .models import Cliente, Oportunidad, Tarea, Contacto
from .forms import ClienteForm, OportunidadForm, TareaForm, ContactoForm

@login_required
def dashboard(request):
    # Estadísticas generales
    total_clientes = Cliente.objects.count()
    total_oportunidades = Oportunidad.objects.count()
    tareas_pendientes = Tarea.objects.filter(estado='pendiente').count()
    
    # Valor total de oportunidades
    valor_total = Oportunidad.objects.aggregate(
        total=Sum('valor')
    )['total'] or 0
    
    # Oportunidades por estado
    oportunidades_por_estado = Oportunidad.objects.values('estado').annotate(
        count=Count('id')
    )
    
    # Tareas próximas a vencer
    proximas_tareas = Tarea.objects.filter(
        estado='pendiente',
        fecha_vencimiento__lte=timezone.now() + timedelta(days=7)
    ).order_by('fecha_vencimiento')[:5]
    
    # Oportunidades recientes
    oportunidades_recientes = Oportunidad.objects.all()[:5]
    
    context = {
        'total_clientes': total_clientes,
        'total_oportunidades': total_oportunidades,
        'tareas_pendientes': tareas_pendientes,
        'valor_total': valor_total,
        'oportunidades_por_estado': oportunidades_por_estado,
        'proximas_tareas': proximas_tareas,
        'oportunidades_recientes': oportunidades_recientes,
    }
    
    return render(request, 'crm/dashboard.html', context)

# Vistas para Clientes
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'crm/cliente_lista.html'
    context_object_name = 'clientes'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Cliente.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(nombre__icontains=search) |
                Q(email__icontains=search) |
                Q(empresa__icontains=search)
            )
        return queryset

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'crm/cliente_detalle.html'
    context_object_name = 'cliente'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['oportunidades'] = self.object.oportunidades.all()
        context['tareas'] = self.object.tareas.filter(estado='pendiente')
        context['contactos'] = self.object.contactos.all()[:10]
        return context

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'crm/cliente_form.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente creado exitosamente.')
        return super().form_valid(form)

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'crm/cliente_form.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Cliente actualizado exitosamente.')
        return super().form_valid(form)

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'crm/cliente_confirmar_eliminacion.html'
    success_url = reverse_lazy('cliente_lista')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Cliente eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vistas para Oportunidades
class OportunidadListView(LoginRequiredMixin, ListView):
    model = Oportunidad
    template_name = 'crm/oportunidad_lista.html'
    context_object_name = 'oportunidades'
    paginate_by = 20

class OportunidadDetailView(LoginRequiredMixin, DetailView):
    model = Oportunidad
    template_name = 'crm/oportunidad_detalle.html'
    context_object_name = 'oportunidad'

class OportunidadCreateView(LoginRequiredMixin, CreateView):
    model = Oportunidad
    form_class = OportunidadForm
    template_name = 'crm/oportunidad_form.html'
    
    def form_valid(self, form):
        form.instance.asignado_a = self.request.user
        messages.success(self.request, 'Oportunidad creada exitosamente.')
        return super().form_valid(form)

class OportunidadUpdateView(LoginRequiredMixin, UpdateView):
    model = Oportunidad
    form_class = OportunidadForm
    template_name = 'crm/oportunidad_form.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Oportunidad actualizada exitosamente.')
        return super().form_valid(form)

class OportunidadDeleteView(LoginRequiredMixin, DeleteView):
    model = Oportunidad
    template_name = 'crm/oportunidad_confirmar_eliminacion.html'
    success_url = reverse_lazy('oportunidad_lista')

# Vistas para Tareas
class TareaListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'crm/tarea_lista.html'
    context_object_name = 'tareas'
    paginate_by = 20
    
    def get_queryset(self):
        return Tarea.objects.filter(asignado_a=self.request.user)

class TareaDetailView(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'crm/tarea_detalle.html'
    context_object_name = 'tarea'

class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'crm/tarea_form.html'
    
    def form_valid(self, form):
        form.instance.asignado_a = self.request.user
        messages.success(self.request, 'Tarea creada exitosamente.')
        return super().form_valid(form)

class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'crm/tarea_form.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Tarea actualizada exitosamente.')
        return super().form_valid(form)

@login_required
def completar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.estado = 'completada'
    tarea.fecha_completada = timezone.now()
    tarea.save()
    messages.success(request, 'Tarea marcada como completada.')
    return redirect('tarea_lista')

# Vistas para Contactos
class ContactoCreateView(LoginRequiredMixin, CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'crm/contacto_form.html'
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, 'Contacto registrado exitosamente.')
        return super().form_valid(form)

@login_required
def crear_contacto_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.cliente = cliente
            contacto.usuario = request.user
            contacto.save()
            messages.success(request, 'Contacto registrado exitosamente.')
            return redirect('cliente_detalle', pk=cliente.pk)
    else:
        form = ContactoForm(initial={'cliente': cliente})
    
    return render(request, 'crm/contacto_form.html', {
        'form': form,
        'cliente': cliente
    })
