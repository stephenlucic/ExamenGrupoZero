from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__" 
        
class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postular
        fields = "__all__"  
        
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
        }        
        
class ArtistaForm(forms.ModelForm):
    class Meta:
        model= Artista
        fields= "__all__"
        
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
        }   
        
class ObraForm(forms.ModelForm):
    class Meta:
        model= Obra
        fields= ["codigo","nombre","descripcion","fecha_ingresado","precio","foto"]
        
        widgets = {
            "fecha_ingresado": forms.DateInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
        }  
        
class ObraFormAdmin(forms.ModelForm):
    class Meta:
        model= Obra
        fields= ["codigo","nombre","descripcion","fecha_ingresado","precio","foto","estado_obra"]
        
        widgets = {
            "fecha_ingresado": forms.DateInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
        }          