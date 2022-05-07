HACER EL TEMPLATES DE PRODUCTO
Hago plantilla
Crear en templates producto.html

{% extends "layout.html" %}
{% block content %}
<h1> Productos </h1>
{% endblock %}

Hago vista voy a views.py de web 
def producto(request):
    return render(request,'producto.html')

Hago urls.py de web 
urlpatterns = [
    path('',views.index,name='index'),
    path('producto',views.producto,name='producto')    
]
-----
Antes de las 20:35  revisa la repeticion para tener claro lo que hace

En views.py
En la funcion producto, estoy conectandome a la tabla producto, a traves de su clase modelo producto, con onbject es paara traerme un solo producto, luego con el diccionario context lo estoy pasando a mi template 
def producto(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    context = {
        'producto':objProducto
    }
    return render(request,'producto.html',context)

En producto.html  pongo <p> {{ producto.nombre }</p> dentro del block content a modo ejemplo ver que funcione
En realidad me traigo el pedazo de codigo de layout y coloco 
{{ producto.categoria.nombre }
{{ producto.precio}}

urls.py
    path('producto/<int:producto_id',views.producto,name='producto')
va hacer que se almanacene en mi variale id 

Luego del layout sacar una parte del codigo y ponerlo en producto.html ese pedazo de codigo y en el hueco que quedo del layout ahi coloco

Y en el producto.html que tengo el codigo que acabo de pegar coloco 
<h1>producto.nombre<h1>

a la parte de imagen la llamo con {{ producto.imagen.url }}


DAR CLICK A IMAGEN Y ME LLEVE A PRODUCTO
En index.html ponerle el link del producto
href="{% url 'web:producto' producto.id}
url completa apliacion web vist producto, el parametro es el producto.id dentro de producto su propiedad id tiene el id del propducto

MOSTRAR CATEGORIAS EN INDEX
en views.py poner
listaCategorias = Categoria.objects.all()
    context = {
        'categorias':listaCategorias
    }

En index.html 
borro un pedazo de codigo 76 a 94 lo borro y pongo 

PRODUCTOS POR CATEGORIA, FILTRAR POR CATEGORIA
para crear los productos por categoria,

producto_set  
tengo ua clase categoria va contener dentro de si un a lista de productos, para acceder es con set 
producto_ set
producto_set.all me trae todos

def productosPorCategoria(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()
    context = {      
        'productos':listaProductos,
    }
    return render(request,'index.html',context)
la lista que me trae es solo de esa categoria

En urls.py 
urlpatterns = [
    path('',views.index,name='index'),
    path('producto/<int:producto_id>',views.producto,name='producto')
    path('productosPorCategoria/<int:categoria_id>',views.productosPorCategoria,name='productosPorCategoria')
]

En el index.html 
cambia algo  {{ categoria.nombre}}

PONER CANTIDAD DE PRODUCTOS EN CADA CATEGORIA, el
En el html.
{{ categoria.producto_set.all.count}}
count es como una funcion para que me aparezca solo la cantidad el numero de cantidad



















