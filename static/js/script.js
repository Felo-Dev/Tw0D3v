$("#btn-iniiciar").click(function () {
    const password = $("#password").val();
    const userName = $("#userName").val();

    // Crear un objeto que contenga los datos del usuario
    const datosUsuario = {
        usuario: userName,
        password: password
    };

    // Enviar la solicitud POST con los datos del usuario
    $.post('/consultar_usuario', JSON.stringify(datosUsuario), function(respuesta) {
        console.log(respuesta);
    });
});
