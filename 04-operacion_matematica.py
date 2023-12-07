def calcular_operacion(num1, num2, operacion):
    try:
        if operacion == "suma":
            return num1 + num2
        elif operacion == "resta":
            return num1 - num2
        elif operacion == "multiplicacion":
            return num1 * num2
        elif operacion == "division":
            return num1 / num2
        else:
            return "Operacion no valida"
    except ZeroDivisionError:
        return "Error: Division por cero"

# Prueba de la función
print(calcular_operacion(50, 2, "suma",))
print(calcular_operacion(25, 20, "resta"))
print(calcular_operacion(35, 2, "multiplicacion"))
print(calcular_operacion(10, 0, "division"))
print(calcular_operacion(100, 2, "division"))
print(calcular_operacion(10, 5, "raiz cuadrada"))