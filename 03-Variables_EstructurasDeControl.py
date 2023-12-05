import numpy as np

alumno = input("Ingrese el nombre del alumno: ")
clase = input("Ingrese el nombre de la asignatura: ")
nota = int(input("Ingrese la nota obtenida, escriba -1 para finalizar: "))
notas = []
#----------------------------------------------#
def calcular_promedio(nota):
    promedio = np.mean(nota)
    return promedio
#----------------------------------------------#
while nota != -1:
    notas.append(nota)
    nota = int(input("Ingrese la nota obtenida, escriba -1 para finalizar: "))
promedio = calcular_promedio(notas)
if promedio >=65:
    print(f"El alumno {alumno} aprobo {clase} con un promedio de {promedio}")
else:
    print(f"El alumno {alumno} reprobo {clase} con un promedio de {promedio}")
print("Programa finalizado")





