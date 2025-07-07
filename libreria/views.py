from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    return render(request, 'libros/index.html')

def crear(request):
    return render(request, 'libros/crear.html')

def editar(request, id):
    return render(request, 'libros/editar.html')