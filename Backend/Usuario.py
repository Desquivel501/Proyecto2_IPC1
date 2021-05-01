class Usuario:
    
    def __init__(self, id, nombre, apellido, cumpleaños, sexo, user_name, user_pass, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.cumpleaños = cumpleaños
        self.user_name = user_name
        self.user_pass = user_pass
        self.telefono = telefono
    
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getSexo(self):
        return self.sexo
    
    def getCumpleaños(self):
        return self.cumpleaños
    
    def getUser_name(self):
        return self.user_name
    
    def getUser_pass(self):
        return self.user_pass
    
    def getTelefono(self):
        return self.telefono
    
    def getRol(self):
        return self.rol
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setId(self, id):
        self.id = id
    
    def setSexo(self, sexo):
        self.sexo = sexo
        
    def setCumpleaños(self, cumple):
        self.cumpleaños = cumple
    
    def setUser_name(self, user_name):
        self.user_name = user_name
    
    def setUser_pass(self, user_pass):
        self.user_pass = user_pass
        
    def setTelefono(self,telefono):
        self.telefono = telefono
    
    
class Doctor:
    def __init__(self, id, nombre, apellido,cumpleaños, sexo, user_name, user_pass, telefono, especialidad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.cumpleaños = cumpleaños
        self.user_name = user_name
        self.user_pass = user_pass
        self.telefono = telefono
        self.especialidad = especialidad
    
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getSexo(self):
        return self.sexo
    
    def getCumpleaños(self):
        return self.cumpleaños
    
    def getUser_name(self):
        return self.user_name
    
    def getUser_pass(self):
        return self.user_pass
    
    def getTelefono(self):
        return self.telefono
    
    def getEspecialidad(self):
        return self.especialidad
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setApellido(self, apellido):
        self.apellido = apellido
        
    def setCumpleaños(self, cumple):
        self.cumpleaños = cumple
    
    def setId(self, id):
        self.id = id
    
    def setSexo(self, sexo):
        self.sexo = sexo
    
    def setUser_name(self, user_name):
        self.user_name = user_name
    
    def setUser_pass(self, user_pass):
        self.user_pass = user_pass
        
    def setTelefono(self,telefono):
        self.telefono = telefono
    
    def setEspecialidad(self,especialidad):
        self.especialidad = especialidad
        

class Enfermera:
    
    def __init__(self, id, nombre, apellido, cumpleaños, sexo,  user_name, user_pass, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.user_name = user_name
        self.user_pass = user_pass
        self.telefono = telefono
        self.cumpleaños = cumpleaños
    
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getSexo(self):
        return self.sexo
    
    def getCumpleaños(self):
        return self.cumpleaños
    
    def getUser_name(self):
        return self.user_name
    
    def getUser_pass(self):
        return self.user_pass
    
    def getTelefono(self):
        return self.telefono
    
    def getRol(self):
        return self.rol
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setId(self, id):
        self.id = id
    
    def setSexo(self, sexo):
        self.sexo = sexo
        
    def setCumpleaños(self, cumple):
        self.cumpleaños = cumple
    
    def setUser_name(self, user_name):
        self.user_name = user_name
    
    def setUser_pass(self, user_pass):
        self.user_pass = user_pass
        
    def setTelefono(self,telefono):
        self.telefono = telefono
        
        
class Admin:
    
    def __init__(self, nombre, apellido, user_name, user_pass):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.user_name = user_name
        self.user_pass = user_pass
        
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getUser_name(self):
        return self.user_name
    
    def getUser_pass(self):
        return self.user_pass
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setApellido(self, apellido):
        self.apellido = apellido
        
    def setUser_name(self, user_name):
        self.user_name = user_name
    
    def setUser_pass(self, user_pass):
        self.user_pass = user_pass
    
    
    