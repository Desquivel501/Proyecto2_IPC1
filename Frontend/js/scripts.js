function go_to_page(user_name, type){
    localStorage.setItem("logged_user", user_name)
    localStorage.setItem("logged", "true")
    switch(type){
        case "Doctor":
            console.log("Doctor")
            localStorage.setItem("type", "doctor")
            location.href= "doctor.html"
            break;
        case "Enfermera":
            console.log("Enfermera")
            localStorage.setItem("type", "enfermera")
            location.href= "enfermera.html"
            break;
        case "Paciente":
            console.log("Paciente")
            localStorage.setItem("type", "paciente")
            location.href= "user.html"
            break;
        case "admin":
            console.log("Admin")
            localStorage.setItem("type", "admin")
            location.href= "admin.html"
    }
}


function check_if_logged(){
    var status = localStorage.getItem("logged")
    if(status == "true"){
        var type =  localStorage.getItem("type")
        switch(type){
            case "doctor":
                location.href = "doctor.html"
                break;
            case "enfermera":
                location.href = "enfermera.html"
                break;
            case "paciente":
                location.href = "user.html"
                break;
            case "admin":
                location.href = "admin.html"
        }
    }else{
        location.href = "login.html"
    }
}

function cerrar_sesion(){
    localStorage.setItem("logged_user","")
    localStorage.setItem("logged","false")
    location.href="login.html"
}

function mod_perfil(){
    var status = localStorage.getItem("logged")
    var logged = localStorage.getItem("logged_user")
    localStorage.setItem("user", logged)
    
    if(status == "true"){
        var type =  localStorage.getItem("type")
        switch(type){
            case "doctor":
                location.href = "modificar-doctor.html"
                break;
            case "enfermera":
                location.href = "modificar-enfermera.html"
                break;
            case "paciente":
                location.href = "modificar_usuario.html"
                break;
            case "admin":
                location.href = "modificar_admin"
        }
    }else{
        location.href = "login.html"
    }
}