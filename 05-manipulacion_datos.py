def realizar_operaciones_con_lista(lista):
    if not lista:
        return "Error: La lista está vacía"

    try:
        numeros = [float(num) for num in lista]
    except ValueError:
        return "Error: Todos los elementos de la lista deben ser números válidos"

    maximo = max(numeros)
    minimo = min(numeros)
    promedio = sum(numeros) / len(numeros)

    return maximo, minimo, promedio

# Lista para almacenar números ingresados por el usuario
numeros = []

# Código para ingresar números y almacenarlos en la lista
while True:
    num = input("Ingrese un número (deje en blanco para terminar): ")
    if num == "":
        break
    try:
        numeros.append(float(num))
    except ValueError:
        print("No es un número válido. Por favor, inténtelo de nuevo.")

# Llamar a la función y mostrar los resultados de las operaciones
resultado = realizar_operaciones_con_lista(numeros)
print(f"Máximo: {resultado[0]}, Mínimo: {resultado[1]}, Promedio: {resultado[2]}")
