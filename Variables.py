num_entero = int(input("Ingrese un numero entero: "))
num_float = float(input("Ingrese un numero flotante: "))
dato_string = str(input("Ingrese un valor tipo string: "))
dato_booleano = bool(input("ingrese un valor booleano 'True' o 'False': "))

float_a_entero = int(num_float)
entero_a_float = float(num_entero)
entero_a_string = str(num_entero)
booleano_a_string = str(dato_booleano)
string_a_booleano = bool(dato_string)

print(f"El numero flotante es {num_float} y La conversion de flotante a entero es: {float_a_entero}",
        f"\nEl numero entero es {num_entero} y La conversion de entero a flotante es: {entero_a_float}",
        f"\nEl numero entero es {num_entero} y La conversion de entero a string es: {entero_a_string}",
        f"\nEl booleano es {dato_booleano} y La conversion de booleano a string es: {booleano_a_string}",
        f"\nEl string es {dato_string} y La conversion de string a booleano es: {string_a_booleano}"
      )