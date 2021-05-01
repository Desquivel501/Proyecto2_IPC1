class Factura:
    
    def __init__(self, id,fecha, paciente, doctor, total):
        self.id = id
        self.fecha = fecha
        self.paciente = paciente
        self.doctor = doctor
        self.total = total
    
    def getId(self):
        return self.id
    
    def getFecha(self):
        return self.fecha
    
    def getPaciente(self):
        return self.paciente
    
    def getDoctor(self):
        return self.doctor
    
    def getTotal(self):
        return self.total
    
