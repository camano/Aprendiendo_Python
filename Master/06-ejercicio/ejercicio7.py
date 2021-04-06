numero1=int(input("Introdusca el primer numero :"))
numero2=int(input("Introdusca el segundo numero :"))

if numero1<numero2:
    for x in range(numero1,(numero2 +1)):
        if x%2==0:
            print(f"{x} es Par")
        else:
            print(f"{x} es impar")
else:
    print("El numero  1 debe ser mayor a 2")