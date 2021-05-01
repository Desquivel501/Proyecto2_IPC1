class Medicamento:
    
    def __init__(self, id, nombre, descripcion, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
    
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion
    
    def getPrecio(self):
        return self.precio
    
    def getCantidad(self):
        return self.cantidad
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def setPrecio(self, precio):
        self.precio = precio
    
    def setCantidad(self, cantidad):
        self.cantidad = cantidad

class Comprado:
    
    def __init__(self,id_med,id_paciente,cantidad):
        self.id_med = id_med
        self.id_paciente = id_paciente
        self.cantidad = cantidad
    
    def getId_med(self):
        return self.id_med
    
    def getCantidad(self):
        return self.cantidad
    
    def getId_paciente(self):
        return self.id_paciente

    def setId_med(self,id_med):
        self.id_med = id_med
    
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
        
    def setId_paciente(self):
        self.id_paciente = id_paciente
    
        
    
    
    
    
