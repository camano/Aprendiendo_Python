#Programacion orientada a objetos

class Coche:
    #Atributos 
    color="Rojo"
    marca="Ferrari"
    modelo="Aventador"
    velocidad=300
    caballage=500

    #Metodos 
    def setColor(self,color):
        self.color=color

    def  getColor(self):
        return self.color
    def setModelo(self,modelo):
        self.modelo=modelo
        
    def  getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1
    
    def getvelocidad(self):
        return self.velocidad
    
#Fin de la clase

#Crear objeto / Instaciar
coche=Coche()

coche.setColor("Verde")
coche.setModelo("murcielago")
print(coche.marca,coche.getModelo(),coche.getColor())
print("Velocidad Actual :",coche.velocidad)
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("Velocidad Actual :",coche.getvelocidad())