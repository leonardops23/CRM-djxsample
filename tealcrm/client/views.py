from django.shortcuts import render
from .models import Client
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'client/clients_list.html', {'clients': clients})

@login_required
def clients_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'client/clients_detail.html', {'client': client})
