from django.shortcuts import render
from .models import Client
from django.contrib.auth.decorators import login_required
from .forms import ClientForm
from django.shortcuts import redirect
from django.contrib import messages

@login_required
def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'client/clients_list.html', {'clients': clients})

@login_required
def clients_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'client/clients_detail.html', {'client': client})

@login_required
def clients_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm()

    messages.success(request, 'Cliente agregado correctamente')
    return render(request, 'client/clients_add.html', {'form': form})

@login_required
def client_delete(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    messages.success(request, 'Cliente eliminado correctamente')
    return redirect('clients_list')

@login_required
def client_update(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado correctamente')
            return redirect('clients_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/clients_update.html', {'form': form})
