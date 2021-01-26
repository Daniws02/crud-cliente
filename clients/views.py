from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required()
def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

@login_required()
def create_client(request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_clients')

    return render(request, 'clients-form.html', {'form': form})

@login_required()
def update_client(request, id):
    client = Client.objects.get(id=id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('list_clients')

    return render(request, 'clients-form.html', {'form': form, 'client': client})

@login_required()
def delete_client(request, id):
    client = Client.objects.get(id=id)

    if request.method == 'POST':
        client.delete()
        return redirect('list_clients')

    return render(request, 'client-delete-confirm.html', {'clients': client})