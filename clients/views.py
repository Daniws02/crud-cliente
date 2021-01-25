from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

from django.contrib.auth import authenticate, login, logout


def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def create_client(request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_clients')

    return render(request, 'clients-form.html', {'form': form})


def update_client(request, id):
    client = Client.objects.get(id=id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('list_clients')

    return render(request, 'clients-form.html', {'form': form, 'client': client})


def delete_client(request, id):
    client = Client.objects.get(id=id)

    if request.method == 'POST':
        client.delete()
        return redirect('list_clients')

    return render(request, 'client-delete-confirm.html', {'clients': client})