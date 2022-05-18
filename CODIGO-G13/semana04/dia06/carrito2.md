clase carrito
atributos:
-canasta = {}     esta vacia la canasta inicialmente

funcionalidades
mover
agregar productos
canasta = {
    detergente,1
    detergente,1
}

sacar productos del carrito (producto)
canasta = {
    detergente,1
}

mostrar carrito    ver lo que hay en el carrito
2 detergentes
vaciar carrito
canasta = {}

Entonces creo la clase cart
la canasta se tiene que almacenar dentro de la sesion osea el session storage

class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session  crea la canasta vacia
        cart = self.session.get("cart")
        if not cart:    si no existe creala vacia
            cart = self.session["cart"] = {}
        self.cart = cart
    
    def add(self,producto,qty):
        self.cart[producto.id] = {
            "producto_id" : producto.id,
            "nombre": producto.nombre,
            "cantidad": qty,
            "precio": str(producto.precio),
            "imagen" : producto.imagen.url,
            "total" : str(qty * producto.precio)
        }
        self.save()
    producto es un objeto de mi clase models,


    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

son dos canastas, una interna cuando se define creo y otra en save cuando se guarda ahi pasa los cambios q he hecho en mi clase hacia mi sesion,  

def add de class cart
            "categoria" : producto.categoria.nombre
        }
en carrito.html
 <a href="#">{{ value.categoria }}</a>
linea 15 <img src= {{ value.image }} alt="">

