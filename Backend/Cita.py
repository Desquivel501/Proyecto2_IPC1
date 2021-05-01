class Cita:
    
    def __init__(self,id,solicitante,fecha,hora,motivo,estado,doctor):
        self.id = id
        self.solicitante = solicitante
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
        self.doctor = doctor
        
    def getId(self):
        return self.id
    
    def getSolicitante(self):
        return self.solicitante
    
    def getFecha(self):
        return self.fecha
    
    def getHora(self):
        return self.hora
    
    def getMotivo(self):
        return self.motivo
    
    def getEstado(self):
        return self.estado
    
    def getDoctor(self):
        return self.doctor
    
    
    def setSolicitante(self,solicitante):
        self.solicitante = solicitante
    
    def setFecha(self,fecha):
        self.fecha = fecha
    
    def setHora(self,hora):
         self.hora = hora
    
    def setMotivo(self,motivo):
        self.motivo = motivo
    
    def setEstado(self,estado):
        self.estado = estado
    
    def setDoctor(self,doctor):
        self.doctor = doctor

    
    