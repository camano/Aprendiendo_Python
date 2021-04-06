""" try :
    nombre =input("Cual es tu nombre ? ")
    if len(nombre)>1:
        nombre_usuario="El nombre es "+nombre
    print(nombre_usuario)
except:
    print("ooh a ocurrido un error ingresa bien tu nombre")
else:
    print("Todo a ocurrido bien")
finally:
    print("Fin de la iteracion !!") """

#multiple excepciones
""" try:
    numero=int(input("Introdusca un numero cualquiera :"))
    print("El numero del cuadrado es " + str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a entero")
except ValueError:
    print("Introduce un numero correcto")
except Exception as e:
    print("Ha ocurrido un erro ",type(e).__name__) """

#Excepciones personalisadas
