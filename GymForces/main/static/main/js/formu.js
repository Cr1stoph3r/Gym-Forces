$(function(){
    $("#formulario").validate({
        rules: {
            user: {
                required: true,
            },
            email: {
                required: true,
                email: true
            },
            password: "required",
            password2: {
                required: true,
                equalTo: "#password"
            }
        },
        messages: {
            user:{
                required: 'El campo no puede estar vacío'
            },
            email:{
                required: 'Ingresa un email por favor!',
                email: 'El correo tiene un formato erroneo'
            },
            password:{
                required: "La contraseña no puede ir vacia"
            },
            password2: {
                required: "Debe reingresar la contraseña",
                equalTo: "Las contraseñas ingresadas no coinciden"
            }
        }
    });
});