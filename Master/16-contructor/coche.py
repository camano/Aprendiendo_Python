class Coche:
    #Atributos 
    color="Rojo"
    marca="Ferrari"
    modelo="Aventador"
    velocidad=300
    caballage=500

    #Constructor
    def __init__(self,color,marca,modelo,velocidad,caballage,plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballage=caballage
        self.plazas=plazas


    #Metodos 
    def setColor(self,color):
        self.color=color

    def  getColor(self):
        return self.color
    def setModelo(self,modelo):
        self.modelo=modelo
        
    def  getModelo(self):
        return self.modelo
    def setMarca(self,marca):
        self.marca=marca
    def getMarca(self):
        return self.marca
    def setVelocidad(self,velocidad):
        self.velocidad=velocidad
    def setCaballage(self,caballage):
        self.caballage=caballage
    def getCaballage(self):
        return self.caballage
    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1
    
    def getvelocidad(self):
        return self.velocidad
    def getInfo(self):
        info="----- Info -------"
        info+="\n Color : "+self.getColor()
        info+="\n Marca : "+self.getMarca()
        info+="\n velociadad : "+ str(self.getvelocidad())
        info+="\n Caballage : "+str(self.getCaballage())
        return info
        
    