el carrito vive dentro de la sesion nada mas, diferentes carritos por cada sesion, una sesion cuando se abre un navegador
carrito se guarda dentro de la sesion del navegador

variable de sesion
existira dentro de la sesion, se usa en login de usuario por ejempló.

DISEÑO CARRITO
creo en templates  carrito.html 
{% extends "layout.html" %}
{% block content %}
copio una parte del codigo de cart.html que venia en la plantilla
{% endblock %} 

Hago views   
def carrito(request):
    return render(request,'carrito.html')

urls       
path('carrito',views.carrito,name='carrito')

index

creo carrito.py en web 
class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart 


AÑADIR PRODUCTOS AL CARRITO
    def add(self,producto,qty):
        self.cart[producto.id] = {
            "producto_id" : producto.id,
            "nombre" : producto.nombre,
            "cantidad" : qty,
            "precio" : str(producto.precio),
            "imagen" : producto.imagen.url,
            "total" : str(qty * producto.precio)
        }      

        self.save()         para que lo guarde en la sesion

        
GUARDAR CARRITO
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True


En views.py
def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

urls.py
    path('agregarCarrito/<int:producto_id>',views.agregarCarrito)

En templates carrito.html
hare un for
        {% for key, value in request.session.cart.items %}
dentro de sesion navegador tengo un carrito y voy a recorrer sus itwms,  key y value         

COMO FUNCIONA EL CARRITO DE COMPRAS
el carrito imaginamos que es un objeto, en este caso una clase llamada CART y esta clase va a atener atributos y va tener en si produc tos, va tener una lista de productos, pero las va tener en forma de diccionario, donde voy a tner una llave donde el id 1 va estar en una llave como un json algo asi

el carruitoi  va guardar nombre precio

CART
{
    1:
    {"nombre":"pantalon",
    "precio":"100"}
    2:

}
AGREGAR PRODUCTO CANT
va agregar

VIEWS.PY 
dentro creo metodo una vista llamada agregar carrito, que me creA una instancia de la clase cart
la sesiom es una memoria de navegador
los productos que estan dentro del carrito los mete dentro de la sesion

save actualiza la sesion pero q ya tiene un producto
el carrito html lo lee de la sesion, recorre hace un for 
---------

VARIABLE DE SESION
cuando abro el navegador si presiono f12 en apliaciones hay datos que puedo almacenar, tambien tengo local y session storage
La variable de sesion va vivir dentro del navegador
En views
def index(request):
    request.session['titulo'] = 'MODA DJANGO'









