def calculadora(numero1,numero2,operacion):
    if operacion=="suma":
        total=numero1+numero2
    if operacion=="resta":
        total=numero1-numero2
    if operacion=="multiplicar":
        total=numero1*numero2
    
    return total

numero1=int(input("Escoge el primer Numero 1:"))
numero2=int(input("Escoge el primer Numero 2:"))
operacion=input("Escoge la Operacion :")
calc= str(calculadora(numero1,numero2,operacion))
print(f"La {operacion} es {calc}")

