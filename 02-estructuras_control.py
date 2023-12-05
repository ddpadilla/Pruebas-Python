
num = int(input("Ingrese un numero entero: "))

while num >= 0:
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} es impar")
    num = int(input("Ingrese un numero entero: "))
print("Programa finalizado")