function hola(nombre){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            console.log('Hola ' + nombre);
            resolve(nombre)
            reject('hay un error');

        },500)
    })
}

function hablar(nombre){
    return new Promise((res,rej) =>{
        setTimeout(function(){
            console.log('como te va ' + nombre);
            res(console);
            rej('no te entiendo')

        },500)
    })
}

let nom = 'Karina';

hola(nom)
.then(hablar)
.then(() => {
    console.log('adios')
})