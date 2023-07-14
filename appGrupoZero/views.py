from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required



def home(request):
    
    data={
        "artistas": Obra.objects.all()
    }
    
    return render(request,"home.html",data)

def contacto(request):
    
    data={
        "form_contacto": ContactoForm,
        "mensaje": ""
    }
    
    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)
        
        if formulario.is_valid():
            
            formulario.save()
            data["mensaje"]= "Formulario enviado"
        else:
            data["mensaje"]= "Error" 
            data["form_contacto"] = formulario   
    
    return render(request,"contacto.html", data)

def artista(request):
    
    if request.user.is_authenticated:
    
        usuariofiltrado = request.user
    
        art = Artista.objects.filter(usuario = usuariofiltrado )
        
    else:
        art = Artista.objects.all()
    data = {
            'mis_artistas': art  
    } 
    
    if request.method == "POST":
        
        valor_buscado = request.POST.get("valor_buscado")
        if valor_buscado !="":
            print(valor_buscado)
            art = Artista.objects.filter(nombre=valor_buscado, rut=valor_buscado)
            data["mis_artistas"] = art
        else:
            data["mis_artistas"]= Artista.objects.all()  
                
    return render(request,"artista.html",data)

def galeria(request):
    
    if request.user.is_authenticated:
        
        usuario_autenticado=request.user
        obras=Obra.objects.filter(usuario__username= usuario_autenticado)
    
    
        data={
        'mis_obraas':obras
        }
    else:
        obras=Obra.objects.filter(estado_obra=1)
        data={
        'mis_obraas':obras
        }
    
  
    
    return render(request, "galeria.html",data)

def postular(request):
    
    data ={
        "formPostulacion":PostulacionForm,
        "mensaje":""
    }
    if request.method=="POST":
        formulario=PostulacionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Postulación enviada")
            data["mensaje"]= "Formulario enviado"
        else:
            data["mensaje"]= "Error" 
            data["formPostulacion"]=formulario
            messages.success(request,"No se pudo enviar")
            
           
            
    return render(request, "postular.html",data)

def obras(request,pk):
    det_obr=get_object_or_404(Obra, pk=pk)
    data={
        'o':det_obr
    }  
    
    return render(request, "obras.html",data)

def desartista(request):
    
    if request.user.is_authenticated:
    
        usuariofiltrado = request.user
    
        art = Artista.objects.filter(usuario = usuariofiltrado )
        
    else:
        art = Artista.objects.all()
    data = {
            'mis_artistas': art  
    } 
    
    if request.method == "POST":
        
        valor_buscado = request.POST.get("valor_buscado")
        if valor_buscado !="":
            art = Artista.objects.filter(nombre=valor_buscado, rut=valor_buscado)
            data["mis_artistas"] = art
        else:
            data["mis_artistas"]= Artista.objects.all() 
    
   
    return render(request, "desartista.html",data)


def agregar_artista(request):
    data = {
        'form' : ArtistaForm,
    }
    
    if request.method == 'POST':
        formulario = ArtistaForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            art=formulario.save(commit=False)
            art.usuario=request.user
            
            art.save()
            data["mensaje"]="Artista creado"
            
        else:
            data["mensaje"]="No se pudo crear artista"
            data["form"]= formulario
                  
    return render(request, "mantenedor/artista/agregar.html", data)

def listar_artista(request):
    
    
    artistas = Artista.objects.all()
    data = {
            'mis_artistas': artistas 
    } 
    
    
    
    return render(request, "mantenedor/artista/listar.html",data)

def modificar_artista(request,rutbuscado):
    
    artista = get_object_or_404(Artista, rut=rutbuscado)
    
    data ={
        'form': ArtistaForm(instance=artista)
    }
    
    if request.method == "POST":
        formulario = ArtistaForm(data=request.POST, instance=artista, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(to ="listar_artista")
        else:
            data["mensaje"]="Ups, algo salio mal"
            data["form"]= formulario
    
    
    return render(request,"mantenedor/artista/modificar.html",data)

def eliminar_artista(request, rutbuscado):
    
    artista =get_object_or_404(Artista, rut=rutbuscado)
    
    artista.delete()
    
    
    
    
    return redirect(to="listar_artista")

def login_usuario(request):
    
    print("bienvenido: "+ request.user.username)
    
    if request.user.groups.filter(name='artista'):
        request.session["tipo"]="artista"
        print("Es un artista")
    else:
        request.session["tipo"]="administrador"
        print("es un administrador")    
        
    return redirect(to='home') 

def registro(request):
    
    data ={
        "mensaje": ""
    }
    
    if request.method == "POST":
        
        rut=request.POST.get("rut")
        
        nombre= request.POST.get("nombre")
        apellido= request.POST.get("apellido")
        correo= request.POST.get("correo")
        password= request.POST.get("password")
        tipo = request.POST.get("tipo")
        
        usu = User()
        usu.set_password(password)
        usu.username = nombre
        usu.email = correo
        usu.first_name = nombre
        usu.last_name = apellido
        
        grupoart = Group.objects.get(name=tipo)
        
        
        try:
            
            if User.objects.filter(username=nombre).exists():
                data["mensaje"] = "El nombre de usuario ya está en uso. Por favor, elija otro nombre de usuario."
            else:
        # Código para crear y guardar el usuario y el artista
                usu.save()
                usu.groups.add(grupoart)
                
                
                art = Artista()
                
                art.rut= rut
                art.nombre = nombre
                art.apellido = apellido
                art.usuario = usu
                
                art.save()
                data["mensaje"]="Registrado correctamente"
            
            
            
            
        
        
        except Exception as e:
            print(f"Error: {str(e)}")
            data["mensaje"] = "Ups, ocurrió un error" 
           
    return render(request, "registration/registro.html", data)

def agregar_obra(request):
    data = {
        'form_obra' : ObraForm,
    }
    
    if request.method == 'POST':
        formulario = ObraForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            obr=formulario.save(commit=False)
            obr.usuario=request.user
            
            
            obr.save()
            data["mensaje"]="Obra creada"
            
        else:
            data["mensaje"]="No se pudo crear Obra"
            data["form_obra"]= formulario
                  
    return render(request, "mantenedor/obra/agregarobra.html", data)

def listar_obra(request):
    
    if request.user.username=="admin":
        obras=Obra.objects.all()
        data={
        'mis_obras':obras
        }
    
        
    
    elif request.user.is_authenticated:
        
        usuario_autenticado=request.user
        obras=Obra.objects.filter(usuario__username= usuario_autenticado)
    
    
        data={
        'mis_obras':obras
        }
    else:
        obras=Obra.objects.all()
        data={
        'mis_obras':obras
        }
        
    
    
    return render(request, "mantenedor/obra/listarobra.html",data)

def modificar_obra(request,codigobuscado):
    
    obra = get_object_or_404(Obra, codigo=codigobuscado)
    if request.user.username=="admin":
        data ={
            'form': ObraFormAdmin(instance=obra)
        }
        
        if request.method == "POST":
            formulario = ObraFormAdmin(data=request.POST, instance=obra, files=request.FILES)
            
            if formulario.is_valid():
                formulario.save()
                return redirect(to ="listar_obra")
            else:
                data["mensaje"]="Ups, algo salio mal"
                data["form"]= formulario
    else:    
        data ={
            'form': ObraForm(instance=obra)
        }
        
        if request.method == "POST":
            formulario = ObraForm(data=request.POST, instance=obra, files=request.FILES)
            
            if formulario.is_valid():
                formulario.save()
                return redirect(to ="listar_obra")
            else:
                data["mensaje"]="Ups, algo salio mal"
                data["form"]= formulario
    
    
    return render(request,"mantenedor/obra/modificarobra.html",data)

def eliminar_obra(request, codigobuscado):
    
    obra=get_object_or_404(Obra, codigo=codigobuscado)
    obra.delete()
    
    return redirect(to="listar_obra")

def listar_postulantes(request):
    
    
    postulantes = Postular.objects.all()
    data = {
            'mis_postulantes': postulantes
    } 
    
    
    
    return render(request, "mantenedor/postulacion/listar_postulantes.html",data)

def eliminar_postulante(request, rutbuscado):
    
    postulante=get_object_or_404(Postular, rut=rutbuscado)
    postulante.delete()
    
    return redirect(to="listar_postulantes")