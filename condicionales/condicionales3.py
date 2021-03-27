print("Programa de beca año 2017");
distancia_escuela=int(input("Introdusca la distancia a la escuela en mk"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el n de hermanos en el centro"))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario anual"))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("Tiene derecho a beca")
else:
    print("No tiene derecho a beca")