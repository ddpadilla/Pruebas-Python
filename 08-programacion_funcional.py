from functools import reduce # Para reducir una lista a un solo valor
import numbers # Para validar que los datos son números

def funcion_principal(datos):
    # Validar que los datos son una lista
    if not isinstance(datos, list):
        raise ValueError("Los datos deben ser una lista")

    # Validar que todos los elementos son números
    if not all(isinstance(dato, numbers.Number) for dato in datos):
        raise ValueError("Todos los elementos de la lista deben ser números")

    # Convertir todos los elementos a flotantes
    datos = list(map(float, datos))

    # Separar los números en positivos, negativos y ceros
    positivos = list(filter(lambda num: num > 0, datos))
    negativos = list(filter(lambda num: num < 0, datos))
    ceros = list(filter(lambda num: num == 0, datos))

    # Calcular la suma, el promedio, el máximo y el mínimo
    suma = reduce(lambda a, b: a + b, datos) if datos else 0
    promedio = suma / len(datos) if datos else 0
    maximo = reduce(lambda a, b: a if a > b else b, datos) if datos else None
    minimo = reduce(lambda a, b: a if a < b else b, datos) if datos else None

    # Devolver un diccionario con los resultados
    return {
        'positivos': positivos,
        'negativos': negativos,
        'ceros': ceros,
        'suma': suma,
        'promedio': promedio,
        'maximo': maximo,
        'minimo': minimo
    }

# Pruebas de la función
print(funcion_principal([1, -2, 3, -4, 0, 5.5, -6.6, 0]))
print(funcion_principal([]))
print(funcion_principal([1, 2, 3]))
print(funcion_principal([-1, -2, -3]))
print(funcion_principal([0, 0, 0]))