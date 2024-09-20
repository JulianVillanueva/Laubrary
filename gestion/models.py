from django.db import models
from django.utils import timezone

# Create your models here.
class Libro(models.Model):
    titulo = models.TextField()
    autor = models.TextField()
    anio_publicacion = models.IntegerField()
    genero = models.CharField(max_length=255)
    num_copias = models.IntegerField()
    estado = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.titulo}- {self.autor}"

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, related_name='prestamo', on_delete=models.CASCADE)
    nombre_prestatario = models.CharField(max_length=255)
    fecha_prestamo = models.DateField
    fecha_devolucion_esperada = models.DateField
    fecha_devolucion_real = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Prestamo de {self.libro.titulo} a {self.nombre_prestatario}"
    
    def marcar_devuelto(self):
        self.libro.estado = 'disponible'
        self.libro.save()
        self.fecha_devolucion_real = timezone.now().date()
        self.save()

class RecordatorioDevolucion(models.Model):
    prestamo = models.ForeignKey(Prestamo, related_name='RecordatorioDevolucion', on_delete=models.CASCADE)
    recordatorio_enviado = models.BooleanField(default=False)

class Reporte(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    libro_mas_solicitado = models.ManyToManyField(Libro, related_name='Reporte')
    prestamos_realizados = models.IntegerField()