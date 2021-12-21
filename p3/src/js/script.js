
//var input = document.getElementById('idname')
var resultadosbusqueda = document.getElementById('resultados_busqueda')
var formulario = document.getElementById("form_user")
var useruuid

function registraruser(){
    var formusername = document.getElementById('formusername')
    var formpasswd = document.getElementById('formpasswd')
    var formname = document.getElementById('formname')
    var formsurname = document.getElementById('formsurname')
    var formmail = document.getElementById('formmail')
    var formphone = document.getElementById('formphone')
    var formvacinated = document.getElementsByName('formvac')
    var formdata = new FormData()
    formdata.append("username", formusername.value)
    formdata.append("password", formpasswd.value)
    formdata.append("name", formname.value)
    formdata.append("surname", formsurname.value)
    formdata.append("phone", formphone.value)
    formdata.append("email", formmail.value)
    formdata.append("is_vaccinated", (formvacinated[0].checked=="y"? 'true':'false'))
    var a = formvacinated.checked==true? 'true':'false'
    var headers = new Headers()
    headers.append('x-hasura-admin-secret','myadminsecretkey')
    fetch('http://localhost:8080/api/rest/user',{
        headers:headers,
        method:'POST',
        body:formdata
    })
    .then(response=>{
        switch(response.status){
            case 200:
                return response.json()
            case 404:
                console.log("Error 404 NOT FOUND")
                throw Error('not found')
            case 500:
                console.log("Error 500 Problems with server")
                throw Error('server')
            case 400:
                console.log("Error, el nombre de usuario ya existe")
                throw Error('insert user')    
            default:
                console.log("Error")
                throw Error('error')
        }
    })
    .then(json=>{
        closeform()
        document.getElementById('registrook').style.display = "block"

    })
    .catch(error =>{
        console.log('Error: ' + error.message)
        switch(error.message){
            case 'not found':
                document.getElementById("error_creandouser").style.display = "block"
            case 'server':
                document.getElementById("error_server").style.display = "block"
            case 'error':
                document.getElementById("error_creandouser").style.display = "block"
            case 'insert user':
                document.getElementById("error_creandouser").style.display = "block"

        }
    })
}
function trylog() {
    document.getElementById('registrook').style.display = "none"
    var user = document.getElementById('namelog').value
    var pass = document.getElementById('passlog').value

    if(user.length > 1 && pass.length > 1) {
        var headers = new Headers()
        headers.append('x-hasura-admin-secret','myadminsecretkey')
        fetch('http://localhost:8080/api/rest/login?username='+ user +'&password=' + pass,{
           headers:headers,
           method:'POST',
       })
       .then(response=>{
            switch(response.status){
                case 200: 
                    return response.json()
                case 404:
                    console.log("Error 404 NOT FOUND")
                    throw Error('not found')
                case 500:
                    console.log("Error 500 Problems with server")
                    throw Error('server')
                default:
                    console.log("Error")
                    throw Error('error')
            }
        })
        .then(json=>{
            if(json.users.length==1){
                window.useruuid = json.users[0].uuid
                showinfo()
                showsites()
                document.getElementById("logok").style.display = "block"
                document.getElementById("logger").style.display="none"
                document.getElementById("result_user").style.display = "block"
                document.getElementById("error_server").style.display = "none"
                document.getElementById("error_log").style.display = "none"
  
            } else{
                throw Error('error')
            }
        })
        .catch(error => {
            console.log('Error: ' + error.message)
            switch(error.message){
                case 'not found':
                    document.getElementById("error_log").style.display = "block" 
                case 'server':
                    document.getElementById("error_server").style.display = "block" 
                case 'error':
                    document.getElementById("error_log").style.display = "block" 
                }
        })
    }
}

function showinfo(){
    document.getElementById("result_user").style.display = "block"
    let http = new XMLHttpRequest()
    useruuid
    http.open("GET", 'http://localhost:8080/api/rest/users/' + window.useruuid)
    http.setRequestHeader("x-hasura-admin-secret","myadminsecretkey")
    http.send()
    http.onreadystatechange=function() {
        if (this.readyState==4 && this.status==200) {
            var userinfo = JSON.parse(this.responseText)
            userinfo = userinfo['users'][0]
            var body = document.getElementById("wrapper")
            var username = document.getElementById("buscanuser")
            var name = document.getElementById("buscaname")
            var apellido = document.getElementById("buscapellid")
            var vacunado = document.getElementById("buscavacunado")
            var telf = document.getElementById("buscatf")
            var email = document.getElementById("buscamail")
            username.innerHTML = "<b>Nombre de usuario: </b>" + userinfo["username"]
            name.innerHTML = "<b>Nombre: </b>" + userinfo["name"]
            apellido.innerHTML = "<b>Apellido(s):</b> " + userinfo["surname"]
            if(userinfo["is_vaccinated"]==true) {
                vacunado.innerHTML = "<b>¿Vacunado?:</b> Sí"
            } else vacunado.innerHTML = "<b>¿Vacunado?:</b> No"
            telf.innerHTML = "<b>Teléfono: </b>" + userinfo["phone"]
            email.innerHTML = "<b>Email: </b>" + userinfo["email"]
            var typeNumber = 25;
            var errorCorrectionLevel = 'L';
            var qr = qrcode(typeNumber, errorCorrectionLevel);
            qr.addData('{' + userinfo["name"] + '},' + '{' + userinfo["surname"] + '},' + '{' + userinfo["uuid"] + '}');
            qr.make();
            document.getElementById('placeHolder').innerHTML = qr.createImgTag();
        } else {
            var username = document.getElementById("buscanuser")
            username.innerHTML = "Error"
        }
    }
    
}
function showsites () {
    var headers = new Headers()
        headers.append('x-hasura-admin-secret','myadminsecretkey')
        fetch('http://localhost:8080/api/rest/user_access_log/'+ window.useruuid+ '?limit=10',{
           headers:headers,
           method:'GET',
       })
       .then(response=>{
            switch(response.status){
                case 200: 
                    return response.json()
                case 404:
                    console.log("Error 404 NOT FOUND")
                    throw Error('not found')
                case 500:
                    console.log("Error 500 Problems with server")
                    throw Error('server')
                default:
                    console.log("Error")
                    throw Error('error')
            }
        })
        .then(json=>{
            var sitios = document.getElementById('buscasitios')
            sitios.innerHTML = "<p><b>Últimos 5 sitios visitados.<br><br></b></p>"
            if (json.access_log.length==0){
                sitios.innerHTML += "<p>Todavía no hay registro de sitios para este usuario</p>"
            } else{
                for(let sitio of json.access_log){
                    sitios.innerHTML += "<p><b><br>Nombre de la instalación:</b>"+sitio.facility.name+"</p>"
                    sitios.innerHTML += "<p><b>Dirección:</b>"+sitio.facility.address+"</p>"
                    sitios.innerHTML += "<p><b>Temperatura: </b>"+sitio.temperature+"</p>"
                    var fecha = sitio.timestamp.split("T")
                    var horas = fecha[1].split(":")
                    var dma = fecha[0].split("-")
                    sitios.innerHTML += "<p><b>Fecha y hora: </b>" + dma[2] + "-" + dma[1] + "-" + dma[0]+"  "+horas[0] + ":" + horas[1] + "</p>"
                    if (sitio.type=="IN"){
                        sitios.innerHTML += "<p><b>Tipo: ENTRADA</p>"
                    } else sitios.innerHTML += "<p><b>Tipo: SALIDA</p>"

                }
            }
        })
        .catch(error => {
            console.log('Error: ' + error.message)
            switch(error.message){
                case 'not found':
                    document.getElementById("error_log").style.display = "block" 
                case 'server':
                    document.getElementById("error_server").style.display = "block" 
                case 'error':
                    document.getElementById("error_log").style.display = "block" 
                }
        })
    
}
const showregistrer = () => {
    document.getElementById('form_user').style.display = "block"
    document.getElementById('logger').style.display = "none"
    document.getElementById('error_server').style.display = "none"
    document.getElementById('error_log').style.display = "none"
    document.getElementById('registrook').style.display = "none"


}
const closeform = () => {
    document.getElementById('form_user').style.display = "none"
    document.getElementById('logger').style.display = "block"
    document.getElementById('error_creandouser').style.display = "none"
    document.getElementById('error_server').style.display = "none"
    document.getElementById('registrook').style.display = "none"
}
const closesesion = () => {
    document.getElementById('logger').style.display = "block"
    document.getElementById('error_server').style.display = "none"
    document.getElementById('result_user').style.display = "none"
    document.getElementById("logok").style.display = "none"

}

const formusername = document.getElementById("formusername")
const formpasswd = document.getElementById("formpasswd")
const formname = document.getElementById("formname")
const formsurname = document.getElementById("formsurname")
const formmail = document.getElementById("formmail")
const formphone = document.getElementById("formphone")
const namelog = document.getElementById("namelog")
const passlog = document.getElementById("passlog")

namelog.addEventListener('input', function(event) {
    if(namelog.validity.valid) {
        namelog.style.borderColor = 'black';
    } else {
        namelog.style.borderColor = 'red';
    }
})
passlog.addEventListener('input', function(event) {
    if(passlog.validity.valid) {
        passlog.style.borderColor = 'black';
    } else {
        passlog.style.borderColor = 'red';
    }
})
formusername.addEventListener('input', function(event) {
    if(formusername.validity.valid) {
        formusername.style.borderColor = 'black';
    } else {
        formusername.style.borderColor = 'red';
    }
})
formpasswd.addEventListener('input', function(event) {
    if(formpasswd.validity.valid) {
        formpasswd.style.borderColor = 'black';
    } else {
        formpasswd.style.borderColor = 'red';
    }
})
formname.addEventListener('input', function(event) {
    if(formname.validity.valid) {
        formname.style.borderColor = 'black';
    } else {
        formname.style.borderColor = 'red';
    }
})
formsurname.addEventListener('input', function(event) {
    if(formsurname.validity.valid) {
        formsurname.style.borderColor = 'black';
    } else {
        formsurname.style.borderColor = 'red';
    }
})
formmail.addEventListener('input', function(event) {
    if(formmail.validity.valid) {
        formmail.style.borderColor = 'black';
    } else {
        formmail.style.borderColor = 'red';
    }
})
formphone.addEventListener('input', function(event) {
    if(formphone.validity.valid) {
        formphone.style.borderColor = 'black';
    } else {
        formphone.style.borderColor = 'red';
    }
})
const formregvalidator = () => {
    var aux = true
    var inputs = document.getElementsByName('forminputs')
    for(let input of inputs){
        if (!input.validity.valid)
            aux = false
    }
    if(aux)
        return registraruser()
            
}
const formlogvalidator = () => {
    var aux = true
    var inputs = document.getElementsByName('inputlog')
    for(let input of inputs){
        if (!input.validity.valid)
            aux = false
    }
    if(aux)
        return trylog()
        
}
document.getElementById('registrarnuevo').addEventListener('click', showregistrer)
document.getElementById('closeform').addEventListener('click', closeform)
document.getElementById('buttonok').addEventListener('click', formregvalidator)
document.getElementById('buttonlog').addEventListener('click',formlogvalidator)
document.getElementById('backinfo').addEventListener('click',closesesion)