function hola(nombre,primercallback){
    setTimeout(function(){
        console.log('Hola ' + nombre);
        primercallback(nombre);

    },500);
}

function hablar(nombre,segundocallback){
    setTimeout(() => {
        
    }, timeout);
    console.log("como te va " + nombre);

}

let nom = 'Karina';
hola(nom,function(nombre){
    hablar(nombre)
});
//hablar(nom)