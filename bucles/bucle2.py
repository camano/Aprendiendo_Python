for i in range(5,50,3):
    print(f"valor entre llaves {i}")

edad=int(input("Introdusca tu edad por favor :"))
while edad<5 or edad>100:
    print("Has introducido una edad Negativa vuelve a intentarlo")
    edad=int(input("Introdusca tu edad por favor :"))

print("Gracias por su colaboracion")
print("Edad del aspirante :"+str(edad))