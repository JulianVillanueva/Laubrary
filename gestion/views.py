from django.shortcuts import render
from django.contrib import admin
from rest_framework import viewsets
from .models import Libro, Prestamo, RecordatorioDevolucion, Reporte
from .serializers import LibroSerializers, PrestamoSerializers, RecordatorioDevolucionSerializers

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializers

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializers

class RecordatorioDevolucionViewSet(viewsets.ModelViewSet):
    queryset = RecordatorioDevolucion.objects.all()
    serializer_class = RecordatorioDevolucionSerializers
# Create your views here.
