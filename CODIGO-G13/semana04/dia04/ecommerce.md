Creo entorno virtual
Activo entorno virtual
Creo .gitignore y pego lo del link 
Creo requirements.txt y coloco django==3.2   mysqlclient
Luego pip install -r requirements.txt
django-admin startproject shop .  es diferente porque cres el shop
recuerdas que antes no ponias punto y te creaba shop
con . en la misma carpeta dopnde estoy me crea la otra csarpeta, 

python manage.py startapp web

En settigngs de shop  
    INSTALLED_APPS = [
    'web',

Hacer models.py las clases categoria y productos

Al final del settings
import os
MEDIA_ROOT = os.path.join(BASE_DIR,'media')      detecta la ubicacion fisica de la  imagen 
MEDIA_URL = '/media/'       detecta la ruta  de la imagen

Creo carpeta media a la altura generica

EN urls de shop
importo 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   esta ultima linea la agrego no va dentro porque no va a una vista

CONECTAR A MI BASE DE DATOS
Laragon
Mi cilindro , ya estaba conecatada añado con + db_shop

En settings de shop 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_shop',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

comandos para INSTALAR NUEVAS LIBRERIAS:
Agrego la nueva libreria Pillow en requiments.txt 
pip install -r requirements.txt
pip freeze

pasos para MIGRAR TABLAS
python manage.py makemigrations    me creo categoria y producto
python manage.py migrate

CREAR USUARIO ADMINISTRADOR y PASSWORD
python manage.py createsuperuser
de username puse admin, luego mi correo,en password puse admin, de nuevo admin de password(veras que no aparece es transparente) y marco y que lo cree igual


Ir a usuario admin.py de web
from .models import Categoria,Producto

admin.site.register(Categoria)
admin.site.register(Producto)

y ya tengo un administrador completoooo!! 

------.-------
creo carpeta templates en web, ahi le creo index.html y layout.html

pongo h1 en index de templates
en views de web 
# Create your views here.
def index(request):
    return render(request,'index.html')

Crear urls.py en web 
from django.urls import  path 

from . import views 

app_name = 'web' 

urlpatterns = [
    path('',views.index,name='index')
]

urls del proyecto shop
from django.contrib import admin
from django.urls import path,include

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',include('web.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

en layout de templates > web 
abrir con vsc catalog gallery, copio con control + a copio todo y lo pego en layout.html
Voy a heredar esta plantilla general en mi index.html
{% extends "layout.html" %}
hacerle un runserver para ver y aparecera pero feito 

copio en una carpeta static que creo en web y pego los archivos estaticos, que estaban en mi plantilla copio el css fonts img js y less

En la primera fila de layout poner eso , para que importe los estaticos
{% load static %}

En layout  a los css les agrergo el % como este
<link rel="stylesheet" href="{% static 'css/font-awesome.min.css' %}">
{% static '         ' %}">
y al final en js 
<script src="{% static 'js/jquery-1.12.4.min.js' %}"
ejecutar el runserver y ya tendra estilos

Vamos a segmentar separar el codigo, en layout tengo todo el codigo de corrido, yo voy a quedarme en layout solo con la cabecera y con footer, porque eso se repite en todas las futuras paginas que puedo tener, entonces para no repetir a cada rato.
entonces ubico el cont maincont , abajo el section-top ese minimizo linea 308 y el 366 section-wrap.. lo minimizo y control x a todo eso y lo llevo al index, 
en el espacio que me quedo en layout ahi pongo
{% block content %}
{% endblock %}

eso mismo lo copio y pego en la parte supérior del index, debajo de la linea 1 y corto lo que tenia abajo y lo pego adentro del 
{% block content %}
{% endblock %}
entonces ahora vere que mi codigo esta separado y en la pagina se ve completo como antes .

Me quedo con un solo article, borro los otros articles

en views.py de web
from django.shortcuts import render

from .models import Categoria,Producto

# Create your views here.
def index(request):
    listaProductos = Producto.objects.all()
    context = {
        'productos':listaProductos
    }
    return render(request,'index.html',context)

Vuelvo al unico article que tentgo y le pongo al iniciar 
{% }