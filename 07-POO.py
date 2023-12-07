# Programación Orientada a Objetos (POO)
#
#     Diseña una clase Vehiculo que demuestre los conceptos de POO como encapsulación, herencia y polimorfismo.
#     Incluye validaciones en los métodos para manejar entradas incorrectas o situaciones inesperadas.
#     Crea varias instancias de la clase y prueba sus métodos.
#     Maneja errores y proporciona retroalimentación clara.

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def detalle1(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

    def enciende_motor1(self):
        return "Motor encendido"

class camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def detalle2(self):
        return f"{super().detalle1()}, Puertas: {self.puertas}"

    def enciende_motor2(self):
        return "El motor ruge con fuerza"

try:
    v = Vehiculo("Toyota", "Corolla", 2020)
    print(v.detalle1())
    print(v.enciende_motor1())

    c = camioneta("Honda", "CRV", 2021, 4)
    print(c.detalle2())
    print(c.enciende_motor2())
except Exception as e:
    print(f"Ha ocurrido un error: {e}")