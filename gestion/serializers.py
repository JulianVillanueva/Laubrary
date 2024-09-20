from rest_framework import serializers
from .models import Libro, Prestamo, RecordatorioDevolucion, Reporte



class LibroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = "__all__"

class PrestamoSerializers(serializers.ModelSerializer):

    

    class Meta:
        model = Prestamo
        fields = "__all__"

        def create(self, validated_data):
            Libro = validated_data.pop('paciente')
            prestamo = Prestamo.objects.create(libro=Libro **validated_data)
            return prestamo
        
class RecordatorioDevolucionSerializers(serializers.ModelSerializer):

    

    class Meta:
        model = Prestamo
        fields = "__all__"

        def create(self, validated_data):
            Libro = validated_data.pop('paciente')
            prestamo = Prestamo.objects.create(libro=Libro **validated_data)
            return prestamo