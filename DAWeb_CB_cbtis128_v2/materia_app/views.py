from django.shortcuts import render
from .models import materia

# Create your views here.

def inicio_vista(request):
    ListadoMaterias=materia.objects.all()
    return render(request,'gestionarMaterias.html',{"lasmaterias":ListadoMaterias})