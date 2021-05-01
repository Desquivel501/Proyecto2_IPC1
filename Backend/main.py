from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import datetime
from Usuario import Usuario, Doctor, Enfermera, Admin
from Medicamento import Medicamento, Comprado 
from  Cita import Cita
from Factura import Factura
import json

x = datetime.datetime.now()

app = Flask(__name__)
CORS(app)

Usuarios = []
Usuarios.append(Usuario(0,"Derek","Esquivel","2002-04-09","M","Desquivel501","password","22000000"))
Usuarios.append(Usuario(1,"Mark","White","2007-06-01","M","MK69","1234","22340002"))
Usuarios.append(Usuario(2,"Michael","Adams","2000-05-10","M","Mike10","1234","22585000"))
Usuarios.append(Usuario(3,"Zoey","Dean","F","1994-08-21","ZzDn123","1234","22534239"))
Usuarios.append(Usuario(4,"Lucy","Goodman","1999-02-02","F","LuGo12","1234","25694782"))

Enfermeras = []
Enfermeras.append(Enfermera(0,"Fatima","Lee","1998-01-01","F","LeFa123","password","22520001"))
Enfermeras.append(Enfermera(1,"Mario","Martinez","1985-08-12","M","Mar2","password","22200078"))
Enfermeras.append(Enfermera(2,"Mary","Vargas","2000-09-20","F","MaVar69","password","22568710"))
Enfermeras.append(Enfermera(3,"Josh","Dominguez","2001-07-05","M","JoDom12","password","22528561"))
Enfermeras.append(Enfermera(4,"Nick","Marx","1999-05-30","F","Commies","password","22529001"))

Doctores = []
Doctores.append(Doctor(0,"Thomas ","Brown","1979-04-11","M","DocBrown","password","22522221","Cardiologo"))
Doctores.append(Doctor(1,"James ","Davis ","1985-01-12","M","J1mmy2","password","23269070",2))
Doctores.append(Doctor(2,"Sophie ","Davis ","1989-12-20","F","Sofi10","password","56236587",0))
Doctores.append(Doctor(3,"William ","Garcia","1990-03-08","M","WillyG","password","55286900",1))
Doctores.append(Doctor(4,"Olivia ","Brown ","1979-09-29","F","Liv3","password","22230010",2))

Medicamentos = []
Medicamentos.append(Medicamento(0,"Panadol","Lorem ipsum dolor sit amet",50,12))
Medicamentos.append(Medicamento(1,"Omeprazol","Lorem ipsum dolor sit amet",30,23))
Medicamentos.append(Medicamento(2,"Dorival","Lorem ipsum dolor sit amet",15,6))
Medicamentos.append(Medicamento(3,"Aspirina","Lorem ipsum dolor sit amet",19,25))

Administrador = Admin("Ariel","Bautista","admin","1234") 


def rolSwitch(i):
    switcher={
        0:"Doctor",
        1:"Enfermero/a",
        2:"Paciente"
    }
    return switcher.get(i)

@app.route("/", methods=["GET"])
def index():
    return str(x)

@app.route("/", methods=["POST"])
def indexPost():
    return "Mensaje desde POST"

@app.route("/hello")
def hello_page():
    #print("Hello World")
    return "<H2>Hello Again!</H2>"


@app.route("/Users", methods=["GET"])
def getUsuarios():
    global Usuarios
    Datos = []
    for Usuario in Usuarios:
        objeto = {
            "Id":Usuario.getId(),
            "Nombre":Usuario.getNombre(),
            "Apellido":Usuario.getApellido(),
            "Cumpleaños": Usuario.getCumpleaños(),
            "Sexo":Usuario.getSexo(),
            "User_name":Usuario.getUser_name(),
            "User_pass":Usuario.getUser_pass(),
            "Telefono":Usuario.getTelefono(),
        }
        Datos.append(objeto)
    return jsonify(Datos)

@app.route("/Users", methods=["POST"])
def agregarUsuario():
    global Usuarios
    global Doctores
    global Enfermeras
    
    user_exist = False
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    cumpleaños = request.json['cumpleaños']
    sexo = request.json['sexo']
    user_name = request.json['user_name']
    user_pass = request.json['user_pass']
    telefono = request.json['telefono']
    nuevo = Usuario(len(Usuarios)+1,nombre,apellido,cumpleaños,sexo,user_name,user_pass,telefono)
    
    newObj={
        "Nombre":nombre,
        "Apellido":apellido,
        "Cumpleaños": cumpleaños,
        "Sexo":sexo,
        "User_name":user_name,
        "User_pass":user_pass,
        "Telefono":telefono
    }
    
    for obj in Usuarios:
        if user_name == obj.getUser_name():
            user_exist = True 
            
    for obj2 in Enfermeras:
         if user_name == obj.getUser_name():
            user_exist = True 
    
    for obj3 in Doctores:
         if user_name == obj.getUser_name():
            user_exist = True
    
    if user_name == "admin":
        user_exist = True
    
    
    if user_exist == True:
        print("User Exist")
        return jsonify({
            "Mensaje":"User alredy exist"
        })
    elif user_exist == False:
        Usuarios.append(nuevo)
        return jsonify(newObj)
    
@app.route("/Users/<string:username>", methods=["POST"])
def cambiarPersona(username):
    global Usuarios
    
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    cumpleaños = request.json['cumpleaños']
    sexo = request.json['sexo']
    user_name = request.json['user_name']
    user_pass = request.json['user_pass']
    telefono = request.json['telefono']
    
    for Usuario in Usuarios:
        if Usuario.getUser_name() == username:
            Usuario.setNombre(nombre)
            Usuario.setApellido(apellido)
            Usuario.setCumpleaños(cumpleaños)
            Usuario.setSexo(sexo)
            Usuario.setUser_name(user_name)
            Usuario.setUser_pass(user_pass)
            Usuario.setTelefono(telefono)
    
    return jsonify({
            "Mensaje":"Se ha cambiado el usuario"
        })
            
@app.route("/Users/<string:username>", methods=["GET"])
def getPersona(username):
    global Usuarios
    user_exist = False
    for Usuario in Usuarios:
        if Usuario.getUser_name() == username:
            objeto = {
                "Id":Usuario.getId(),
                "Nombre":Usuario.getNombre(),
                "Apellido":Usuario.getApellido(),
                "Cumpleaños":Usuario.getCumpleaños(),
                "Sexo":Usuario.getSexo(),
                "User_name":Usuario.getUser_name(),
                "User_pass":Usuario.getUser_pass(),
                "Telefono":Usuario.getTelefono(),
            }
            user_exist = True
            
    if user_exist == True:
        print ("User Exist")
        return jsonify(objeto)
    else:
        print ("User Does Not Exist")
        return jsonify({
            "Mensaje":"Usuario no existe"
        })

@app.route("/Users/<string:username>/borrar", methods=["POST"])
def borrarPersona(username):
    global Usuarios
    
    aux =[]
    
    for Usuario in Usuarios:
        if Usuario.getUser_name() != username:
           aux.append(Usuario)
    
    Usuarios = aux
    
    return jsonify({
            "Mensaje":"Se ha eliminado el usuario"
        })


@app.route("/Doctores", methods=["GET"])
def getDoctores():
    global Doctores
    Datos = []
    for doctor in Doctores:
        objeto = {
            "Id":doctor.getId(),
            "Nombre":doctor.getNombre(),
            "Apellido":doctor.getApellido(),
            "Cumpleaños": doctor.getCumpleaños(),
            "Sexo":doctor.getSexo(),
            "User_name":doctor.getUser_name(),
            "User_pass":doctor.getUser_pass(),
            "Telefono":doctor.getTelefono(),
            "Especialidad":doctor.getEspecialidad()
        }
        Datos.append(objeto)
    return jsonify(Datos)

@app.route("/Doctores/<string:username>", methods=["GET"])
def getDoc(username):
    global Doctores
    user_exist = False
    for doc in Doctores:
        if doc.getUser_name() == username:
            objeto = {
                "Id":doc.getId(),
                "Nombre":doc.getNombre(),
                "Apellido":doc.getApellido(),
                "Cumpleaños":doc.getCumpleaños(),
                "Sexo":doc.getSexo(),
                "User_name":doc.getUser_name(),
                "User_pass":doc.getUser_pass(),
                "Telefono":doc.getTelefono(),
                "Especialidad":doc.getEspecialidad()
            }
            user_exist = True
            
    if user_exist == True:
        print ("User Exist")
        return jsonify(objeto)
    else:
        print(username)
        print ("User Does Not Exist")
        return jsonify({
            "Mensaje":"Usuario no existe"
        })
    
@app.route("/Doctores/<string:username>", methods=["POST"])
def cambiarDoc(username):
    global Doctores
    
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    cumpleaños = request.json['cumpleaños']
    sexo = request.json['sexo']
    user_name = request.json['user_name']
    user_pass = request.json['user_pass']
    telefono = request.json['telefono']
    especialidad = request.json['especialidad']
    
    for doc in Doctores:
        if doc.getUser_name() == username:
            doc.setNombre(nombre)
            doc.setApellido(apellido)
            doc.setCumpleaños(cumpleaños)
            doc.setSexo(sexo)
            doc.setUser_name(user_name)
            doc.setUser_pass(user_pass)
            doc.setTelefono(telefono)
            doc.setEspecialidad(especialidad)
    
    return jsonify({
            "Mensaje":"Se ha cambiado el usuario"
        })

@app.route("/Doctores/<string:username>/borrar", methods=["POST"])
def borrarDoc(username):
    global Doctores
    
    aux =[]
    
    for doc in Doctores:
        if doc.getUser_name() != username:
           aux.append(doc)
    
    Doctores = aux
    
    return jsonify({
            "Mensaje":"Se ha eliminado el usuario"
        })
    
    
       
@app.route("/Enfermeras", methods=["GET"])
def getEnfermeras():
    global Enfermeras
    Datos = []
    for Enfermera in Enfermeras:
        objeto = {
            "Id":Enfermera.getId(),
            "Nombre":Enfermera.getNombre(),
            "Apellido":Enfermera.getApellido(),
            "Cumpleaños": Enfermera.getCumpleaños(),
            "Sexo":Enfermera.getSexo(),
            "User_name":Enfermera.getUser_name(),
            "User_pass":Enfermera.getUser_pass(),
            "Telefono":Enfermera.getTelefono(),
        }
        Datos.append(objeto)
    return jsonify(Datos)

@app.route("/Enfermeras/<string:username>", methods=["POST"])
def cambiarEnf(username):
    global Enfermeras
    
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    cumpleaños = request.json['cumpleaños']
    sexo = request.json['sexo']
    user_name = request.json['user_name']
    user_pass = request.json['user_pass']
    telefono = request.json['telefono']
    
    for Enfermera in Enfermeras:
        if Enfermera.getUser_name() == username:
            Enfermera.setNombre(nombre)
            Enfermera.setApellido(apellido)
            Enfermera.setCumpleaños(cumpleaños)
            Enfermera.setSexo(sexo)
            Enfermera.setUser_name(user_name)
            Enfermera.setUser_pass(user_pass)
            Enfermera.setTelefono(telefono)
    
    return jsonify({
            "Mensaje":"Se ha cambiado el usuario"
        })
            
@app.route("/Enfermeras/<string:username>", methods=["GET"])
def getEnf(username):
    global Enfermeras
    user_exist = False
    for Enfermera in Enfermeras:
        if Enfermera.getUser_name() == username:
            objeto = {
                "Id":Enfermera.getId(),
                "Nombre":Enfermera.getNombre(),
                "Apellido":Enfermera.getApellido(),
                "Cumpleaños":Enfermera.getCumpleaños(),
                "Sexo":Enfermera.getSexo(),
                "User_name":Enfermera.getUser_name(),
                "User_pass":Enfermera.getUser_pass(),
                "Telefono":Enfermera.getTelefono(),
            }
            user_exist = True
            
    if user_exist == True:
        print ("User Exist")
        return jsonify(objeto)
    else:
        print ("User Does Not Exist")
        return jsonify({
            "Mensaje":"Usuario no existe"
        })

@app.route("/Enfermeras/<string:username>/borrar", methods=["POST"])
def borrarEbf(username):
    global Enfermeras
    
    aux =[]
    
    for enf in Enfermeras:
        if enf.getUser_name() != username:
           aux.append(enf)
    
    Enfermeras = aux
    
    return jsonify({
            "Mensaje":"Se ha eliminado el usuario"
        })
 
 
@app.route("/admin/<string:username>", methods=['POST'])
def setAdmin(username):
    global Administrador
    
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    user_name = request.json['user_name']
    user_pass = request.json['user_pass']
    
    Administrador.setNombre(nombre)
    Administrador.setApellido(apellido)
    Administrador.setUser_pass(user_pass)
    
    return jsonify({
                    "Mensaje":"Se ha cambiado el usuario"
                    })

@app.route("/admin/<string:username>", methods=['GET'])
def getAdmin(username):
    global Administrador
    
    objeto = {
        "Nombre":Administrador.getNombre(),
        "Apellido":Administrador.getApellido(),
        "User_name":Administrador.getUser_name(),
        "User_pass":Administrador.getUser_pass(),
    }
    
    return jsonify(objeto)


compra_actual=[]


@app.route("/Med", methods=["GET"])
def getMedicamentos():
    global Medicamentos
    med_array=[]
    for Medicamento in Medicamentos:
        objeto = {
            "Nombre":Medicamento.getNombre(),
            "Descripcion":Medicamento.getDescripcion(),
            "Precio":Medicamento.getPrecio(),
            "Cantidad":Medicamento.getCantidad()
        }
        med_array.append(objeto)
    return jsonify(med_array)


@app.route("/Med", methods=["POST"])
def addMedicamento():
    global Medicamentos
    nombre = request.json["Nombre"]
    descripcion = request.json["Descripcion"]
    precio = request.json["Precio"]
    cantidad = request.json["Cantidad"]
    nuevo = Medicamento(len(Medicamentos)+1,nombre,descripcion,precio,cantidad)
    med_exist = False
    
    for obj in Medicamentos:
        if nombre == obj.getNombre():
            med_exist = True
    
    if med_exist == True:
        return "Med already exist"
    elif med_exist == False:
        Medicamentos.append(nuevo)
        return "Med has been succesfully created"

@app.route("/Med/<string:name>", methods=["GET"])
def getMedicamento(name):
    global Medicamentos
    for Medicamento in Medicamentos:
        if name == Medicamento.getNombre():
            objeto = {
                "Nombre":Medicamento.getNombre(),
                "Descripcion":Medicamento.getDescripcion(),
                "Precio":Medicamento.getPrecio(),
                "Cantidad":Medicamento.getCantidad()
            }
            break
        
    return jsonify(objeto)



@app.route("/Med/<string:name>/agregar", methods=["POST"])
def compraMedicamento(name):
    global Medicamentos
    global compra_actual
    
    user_name = request.json['nombre']
    
    agregado = False
    objeto = {}
    
    for Medicamento in Medicamentos:
        if name == Medicamento.getNombre():
            for compra in compra_actual:
                if compra.id_med == Medicamento.getId():
                    agregado = True
    
    if agregado == True:
        for Medicamento in Medicamentos:
            if name == Medicamento.getNombre():
                for comprado in compra_actual:
                    if comprado.getId_med() == Medicamento.getId():
                        if int(comprado.getCantidad()) < int(Medicamento.getCantidad()):
                            comprado.setCantidad(comprado.getCantidad()+1)
                            
                            objeto={
                                "id": comprado.getId_med(),
                                "Nombre": name,
                                "Precio":Medicamento.getPrecio(),
                                "Cantidad": comprado.getCantidad(),
                                "Subtotal": (Medicamento.getPrecio()*comprado.getCantidad()),
                                "Mensaje": "Agregado "
                            }
                        elif int(comprado.getCantidad()) >= int(Medicamento.getCantidad()):
                            objeto={
                                 "Mensaje": "No hay existencias"
                            }
    elif agregado == False:
        for Medicamento in Medicamentos:
            if name == Medicamento.getNombre():
                nuevo = Comprado(Medicamento.getId(),user_name,1)
                compra_actual.append(nuevo)
                
                objeto={
                    "id": Medicamento.getId(),
                    "Nombre": name,
                    "Precio":Medicamento.getPrecio(),
                    "Cantidad": 1,
                    "Subtotal": Medicamento.getPrecio(),
                    "Mensaje": "Nuevo"
                }
    return jsonify(objeto)

@app.route("/Med/<string:name>/quitar", methods=["POST"])
def quitarMedicamento(name):
    global Medicamentos
    global compra_actual
    
    user_name = request.json['nombre']
    
    agregado = False
    objeto = {}

    for Medicamento in Medicamentos:
        if name == Medicamento.getNombre():
            print("here")
            for comprado in compra_actual:
                if Medicamento.getId() == comprado.getId_med():
                    if int(comprado.getCantidad()) > 1:
                        cant_aux = int(comprado.getCantidad())
                        comprado.setCantidad(cant_aux-1)
                        
                    elif int(comprado.getCantidad()) <= 1:
                        
                        aux =[]
                        for com in compra_actual:
                            if com.getId_med() != comprado.getId_med():
                                aux.append(com)
                        compra_actual = aux

    return jsonify({
                    "Mensaje":"Se ha quitado el producto"
                    })

@app.route("/compra/<string:name>", methods=["POST"])
def compraMed(name):
    global Medicamentos
    for Medicamento in Medicamentos:
        if name == Medicamento.getNombre():
            objeto = {
                "Nombre":Medicamento.getNombre(),
                "Descripcion":Medicamento.getDescripcion(),
                "Precio":Medicamento.getPrecio(),
                "Cantidad":Medicamento.getCantidad()
            }
            break
        
    return jsonify(objeto)


@app.route("/compras", methods=["GET"])
def compras():
    global Medicamentos
    global compra_actual
    
    datos = []
    for compra in compra_actual:
        for Medicamento in Medicamentos:
            if compra.getId_med() == Medicamento.getId():
                objeto = {
                    "Nombre":Medicamento.getNombre(),
                    "Descripcion":Medicamento.getDescripcion(),
                    "Precio": Medicamento.getPrecio(),
                    "Cantidad":compra.getCantidad()
                }
                datos.append(objeto)
        
    return jsonify(datos)


@app.route("/Login",methods=['POST'])
def loginPost():
    global Usuarios
    user_name = request.json['user_name']
    user_pass = request.json['user_pass']
    
    user_exist = False
    pass_exist = False
    admin_exist = False
    check = True
    Id = 0
    username = ""
    
    if user_name == Administrador.getUser_name() and Administrador.getUser_pass() == user_pass:
        admin_exist = True
        check = False
            
    if check == True:
        for Usuario in Usuarios:
            if user_name == Usuario.getUser_name():
                full_name = Usuario.getNombre() + " " + Usuario.getApellido()
                user_type = "Paciente"
                user_exist = True
                check = False
                username = Usuario.getUser_name()
                
                if user_pass == Usuario.getUser_pass():
                    pass_exist = True
                    
    if check == True:
        for Enfermera in Enfermeras:
            if user_name == Enfermera.getUser_name():
                full_name = Enfermera.getNombre() + " " + Enfermera.getApellido()
                user_type = "Enfermera"
                user_exist = True
                check = False
                username = Enfermera.getUser_name()
                
                if user_pass == Enfermera.getUser_pass():
                    pass_exist = True
    
    if check == True:
        for Doctor in Doctores:
            if user_name == Doctor.getUser_name():
                full_name = Doctor.getNombre() + " " + Doctor.getApellido()
                user_type = "Doctor"
                user_exist = True
                check = False
                username = Doctor.getUser_name()
                
                if user_pass == Doctor.getUser_pass():
                    pass_exist = True
            
 
        
    if user_exist == True and pass_exist == True:
        print('existe ' + str(user_type))
        obj={
                "user_name": username,
                "type":user_type
            }
        return jsonify(obj)
              
    elif user_exist == True and pass_exist != True:
        print ("Contraseña Incorrecta")
        return "Contraseña Incorrecta"
    elif admin_exist == True:
        obj={
                "user_name": "admin",
                "type":"admin"
            }
        return jsonify(obj)
    else:
        return "Usuario no existe"
    
    

@app.route("/doctor", methods=['GET'])
def doctor_page():
    return "You are a Doctor"

@app.route("/patient", methods=['GET'])
def patirnt_page():
    return "You are a Patient"

@app.route("/nurse", methods=['GET'])
def nurse_page():
    return "You are a Nurse"

@app.route("/Login", methods=["GET"])
def login():
    return "You are login in"


@app.route("/carga_pacientes", methods=["POST"])
def cargaUsuarios():
    global Usuarios
    fecha = request.json["usuarios"]
    
    for usuario in usuariosCM:
        nuevo = Usuario(len(Usuarios)+1,usuario['Nombre'],usuario['Apellido'],usuario['Fecha'],usuario['Sexo'],usuario['User_name'],usuario['Password'],usuario['Telefono'])
        Usuarios.append(nuevo)
    
    return jsonify({
            "Mensaje":"Se han añadido los usuario"
        })

@app.route("/carga_doctores", methods=["POST"])
def cargaDoctores():
    global Doctores
    doctoresCM = request.json["doctores"]
    
    for doctor in doctoresCM:
        nuevo = Doctor(len(Doctores)+1,doctor['Nombre'],doctor['Apellido'],doctor['Fecha'],doctor['Sexo'],doctor['User_name'],doctor['Password'],doctor['Telefono'],doctor['Especialidad'])
        Doctores.append(nuevo)
    
    return jsonify({
            "Mensaje":"Se han añadido los usuario"
        })

@app.route("/carga_enfermeras", methods=["POST"])
def cargaEnfermeras():
    global Enfermeras
    enfermerasCM = request.json["enfermeras"]
    
    for enfermera in enfermerasCM:
        nuevo = Enfermera(len(Enfermeras)+1,enfermera['Nombre'],enfermera['Apellido'],enfermera['Fecha'],enfermera['Sexo'],enfermera['User_name'],enfermera['Password'],enfermera['Telefono'])
        Enfermeras.append(nuevo)
    
    return jsonify({
            "Mensaje":"Se han añadido los usuario"
        })

@app.route("/carga_medicamentos", methods=["POST"])
def cargaMedicamentos():
    global Medicamentos
    medicamentosCM = request.json["medicamentos"]
    
    for medicamento in medicamentosCM:
        nuevo = Medicamento(len(Medicamentos)+1,medicamento['Nombre'],medicamento['Descripcion'],medicamento['Precio'],medicamento['Cantidad'])
        Medicamentos.append(nuevo)
    
    return jsonify({
            "Mensaje":"Se han añadido los usuario"
        })


Citas = []
Citas.append(Cita(len(Citas)+1,"Desquivel501","2021/9/12","12:00","Test","Pendiente",""))

@app.route("/Cita", methods=["POST"])
def crearCita():
    global Citas
    global Usuarios
    
    nombre = request.json['nombre']
    fecha = request.json['fecha']
    hora = request.json["hora"]
    motivo = request.json["motivo"]
    print(nombre)
    cita_solicitada = False
    
    for Usuario in Usuarios:
        if Usuario.getUser_name() == nombre:
            
             for cit in Citas:
                if cit.getSolicitante() == Usuario.getUser_name() and cit.getEstado() != "Completada" and cit.getEstado() != "Rechazada":
                    cita_solicitada = True
                    break
    
    if cita_solicitada == False:
        nueva = Cita(len(Citas)+1, nombre, fecha, hora, motivo ,'Pendiente','')
        Citas.append(nueva)
        return jsonify({
            "Estado":"Nueva",
            "Mensaje":"Se ha solicitado la cita"
        })
    elif cita_solicitada == True:
        return jsonify({
            "Estado":"Solicitada",
            "Mensaje":"No puede solicitar una cita si se tiene una cita pendiente."
        })

@app.route("/cita/<string:name>", methods=["GET"])
def verCita(name):
    global Citas
    global Usuarios
    
    cita_solicitada = False
    
    obj={
        "Mensaje":"No existe"  
    }
    
    for Usuario in Usuarios:
        if Usuario.getNombre() == name:
             for Cita in Citas:
                if Cita.getSolicitante() == Usuario.getId() and Cita.getEstado() != "Completada" and Cita.getEstado() != "Rechazada":
                   obj={
                       "Fecha":Cita.getFecha(),
                       "Hora":Cita.getHora(),
                       "Motivo":Cita.getMotivo(),
                       "Estado":Cita.getEstado(),
                       "Mensaje":"Existe"  
                   }
                else:
                    obj={
                       "Mensaje":"No existe"  
                    }
    
    return jsonify(obj)

@app.route("/citas_pendientes", methods=["GET"])
def verCitasPendientes():
    global Citas
    global Usuarios
    
    Datos = []
    obj={}
    name=""
    
    for Cita in Citas:
        if Cita.getEstado() != "Completada" and Cita.getEstado() != "Rechazada" and  Cita.getEstado() != "Aceptada":
            for user in Usuarios:
                if Cita.getSolicitante() == user.getUser_name():
                    name = user.getNombre() + " " + user.getApellido()
            
            obj={
                "Id":Cita.getId(),
                "Fecha":Cita.getFecha(),
                "Hora":Cita.getHora(),
                "Motivo":Cita.getMotivo(),
                "Paciente":name
            }
            Datos.append(obj)
            
    return jsonify(Datos)


@app.route("/citas_aceptadas", methods=["GET"])
def verCitasAceptadas():
    global Citas
    global Usuarios
    
    Datos = []
    obj={}
    name_pac=""
    name_doc=""
    
    for Cita in Citas:
        if Cita.getEstado() == "Aceptada":
            for user in Usuarios:
                if Cita.getSolicitante() == user.getUser_name():
                    name_pac = user.getNombre() + " " + user.getApellido()
            for doc in Doctores:
                        if Cita.getDoctor() == doc.getUser_name():
                            name_doc = doc.getNombre() + " " + doc.getApellido()   
            
            obj={
                "Id":Cita.getId(),
                "Fecha":Cita.getFecha(),
                "Hora":Cita.getHora(),
                "Motivo":Cita.getMotivo(),
                "Paciente":name_pac,
                "Doctor":name_doc
            }
            Datos.append(obj)
            
    return jsonify(Datos)
        
@app.route("/citas/<string:name>", methods=["GET"])
def verCitas(name):
    global Citas
    global Usuarios
    global Doctores

    cita_solicitada = False
    obj={
        "Mensaje":"No existe"  
    }
    
    Doc_name = " "
    
    for Usuario in Usuarios:
        if Usuario.getUser_name() == name:
             for Cita in Citas:
                if Cita.getSolicitante() == Usuario.getUser_name() and Cita.getEstado() != "Completada" and Cita.getEstado() != "Rechazada":
                   
                    for doc in Doctores:
                        if Cita.getDoctor() == doc.getUser_name():
                            Doc_name = doc.getNombre() + " " + doc.getApellido()
                   
                    obj={
                        "Fecha":Cita.getFecha(),
                        "Hora":Cita.getHora(),
                        "Motivo":Cita.getMotivo(),
                        "Estado":Cita.getEstado(),
                        "Doctor":Doc_name,
                        "Mensaje":"Existe"  
                    }
                else:
                    obj={
                       "Mensaje":"No existe"  
                    }
    
    return jsonify(obj)
        
        
@app.route("/citas/<string:id>/aceptar", methods=["POST"])
def aceptarCita(id):
    global Citas
    global Usuarios
    global Doctores
    
    doctor = request.json["doctor"]
    id_cita = request.json["id_cita"]
    
    obj={
        "Mensaje":"Error Here"  
    }
    Doc_name = " "
    
    for doc in Doctores:
        if doctor == doc.getUser_name():
            Doc_name = doc.getNombre() + " " + doc.getApellido()
            print(Doc_name)
    
 
    for Cita in Citas:
        if int(Cita.getId()) == int(id_cita):
            print("here")
            Cita.setEstado("Aceptada")
            Cita.setDoctor(doctor)
       
            obj={
                "Mensaje":"Se ha aceptado la cita" ,
                "Nombre_doctor":str(Doc_name)
            }
            
    return jsonify(obj)


@app.route("/citas/<string:id>/rechazar", methods=["POST"])
def rechazarCita(id):
    global Citas
    global Usuarios
    
    id_cita = request.json["id_cita"]
    
    obj={
        "Mensaje":"Error Here"  
    }
 
    for Cita in Citas:
        if int(Cita.getId()) == int(id):
            print("here")
            Cita.setEstado("Rechazada")
       
            obj={
                "Mensaje":"Se ha rechazado la cita"  
                
            }
            
    return jsonify(obj)


@app.route("/citas/<string:id>/completar", methods=["POST"])
def completarCita(id):
    global Citas
    global Usuarios
    
    id_cita = request.json["id_cita"]
    
    obj={
        "Mensaje":"Error Here"  
    }
 
    for Cita in Citas:
        if int(Cita.getId()) == int(id):
            print("here")
            Cita.setEstado("Completada")
       
            obj={
                "Mensaje":"Se ha completado la cita"  
                
            }
            
    return jsonify(obj)


@app.route("/citas/doctor/<string:name>", methods=["GET"])
def verCitasDoc(name):
    global Citas
    global Usuarios
    global Doctores

    cita_solicitada = False
    
    Datos =[]
    
    Doc_name = " "
    name_pac = " "
    
    for doctor in Doctores:
        if doctor.getUser_name() == name:
            Doc_name= doctor.getNombre() + " " + doctor.getApellido()
            for Cita in Citas:
                if Cita.getDoctor() == doctor.getUser_name() and Cita.getEstado() != "Completada" and Cita.getEstado() != "Rechazada":
                    
                    for user in Usuarios:
                        if Cita.getSolicitante() == user.getUser_name():
                            name_pac = user.getNombre() + " " + user.getApellido()
                    
                    
                    obj={
                        "Id":Cita.getId(),
                        "Fecha":Cita.getFecha(),
                        "Hora":Cita.getHora(),
                        "Motivo":Cita.getMotivo(),
                        "Estado":Cita.getEstado(),
                        "Doctor":Doc_name,
                        "Paciente":name_pac,
                        "Mensaje":"Existe"  
                    }
                    Datos.append(obj)
    
    return jsonify(Datos)



Facturas=[]

@app.route("/Factura", methods=["POST"])
def agregarFactura():
    global Usuarios
    global Doctores
    global Enfermeras
    global Facturas
    
    user_exist = False
    fecha = request.json['fecha']
    paciente = request.json['paciente']
    doctor = request.json['doctor']
    total = request.json['total']

    nuevo = Factura(len(Facturas)+1,fecha,paciente,doctor,total)
    Facturas.append(nuevo)
    
    newObj={
        "fecha":fecha,
        "paciente":paciente,
        "doctor": doctor,
        "total":total,
    }
    
    return jsonify(newObj)


if __name__ == "__main__":
    app.run(threaded=True, port=3000, debug=True)

