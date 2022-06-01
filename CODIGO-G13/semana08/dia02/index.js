mysqlConnection.connect(function (err){
    if(err){
        console.error(err);
        return;
    }
    else{
        console.log('conectado a la base de datos')
    }
});
module.exports = mysqlConnection;