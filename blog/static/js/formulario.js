    function validateForm() {
        var x = document.forms["myForm"]["Nombre"].value;
        if (x == "") {
        alert("Tiene que ingresar un nombre");
        return false;
        }
    }

    function validateMail(mail){ 
    object=document.getElementById(mail);
    valueForm=object.value;

    var patron=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
    if(valueForm.search(patron)==0)
    {
        //Correo bien
        object.style.color="#000";
        return;
    }
        //Correo malo
        object.style.color="#f00";
    }

    var p1 = document.getElementById("password").value;
    var p2 = document.getElementById("password").value;
    var espacios = false;
    var cont = 0;
    
    while (!espacios && (cont < p1.length)) {
    if (p1.charAt(cont) == " ")
        espacios = true;
    cont++;
    }
    
    if (espacios) {
    alert ("La contraseña no puede contener espacios en blanco");
    return false;
    }