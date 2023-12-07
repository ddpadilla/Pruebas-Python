
# Entrada de datos
numero = int(input("Ingrese un número (negativo para salir): "))

# Estructura de control para determinar paridad
while numero >= 0:
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
    numero = int(input("Ingrese un numero entero: "))
print("Programa finalizado")