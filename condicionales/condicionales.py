print("Progama de evaluacion")
nota_alumno=input("introdusca algo") 
def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))