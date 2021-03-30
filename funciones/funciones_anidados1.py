def funcion(mensaje):
    mensaje()  
    print ("funcion")

def mensaje():
    print("hola mundo")


print(funcion(mensaje))