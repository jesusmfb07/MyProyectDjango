from django.shortcuts import render, redirect
from .models import Usuario
from .forms import Usuario

def crear_usuario(request):
    if request.method == 'POST':
        form = Usuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = Usuario()
    return render(request, 'crear_usuario.html', {'form': form})
