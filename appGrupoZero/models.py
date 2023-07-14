from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Artista(models.Model):
    rut= models.CharField(max_length=10,null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento= models.DateField(null=True)
    descripcion= models.CharField(max_length=400,null=True)
    tipo= models.ForeignKey(Tipo, on_delete=models.CASCADE,null=True) 
    foto = models.ImageField(upload_to="artista", null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre

tipo_contacto=[
    [0,"sugerencias"],
    [1,"reclamos"],
    [2,"consultas"]
    ]    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    tipo_contacto= models.IntegerField(choices=tipo_contacto)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre +" "+ self.email   


estado_obra=[
    [0,"Creada"],
    [1,"Aprobada"],
    [2, "Rechazada"]
]        
class Obra(models.Model):
    
    codigo= models.CharField(max_length=10)
    #artista= models.ForeignKey(Artista, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100,null=True)
    fecha_ingresado= models.DateField(null=True)
    precio=models.CharField(max_length=100,null=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    foto = models.ImageField(upload_to="obra", null=True)
    estado_obra= models.IntegerField(choices=estado_obra, default=0)
    
    def __str__(self):
        return self.codigo  
    
    
class Postular(models.Model):
    rut= models.CharField(max_length=10,null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento= models.DateField(null=True)
    descripcion= models.CharField(max_length=400,null=True)
    direccion = models.CharField(max_length=100)
    tipo= models.ForeignKey(Tipo, on_delete=models.CASCADE,null=True) 
    foto = models.ImageField(upload_to="postulacion", default=" ",null=True)
    cv=models.FileField(upload_to="postulacion",default=" ", null=True)
    
    def __str__(self):
        return self.rut+" "+self.nombre+" "+self.apellido