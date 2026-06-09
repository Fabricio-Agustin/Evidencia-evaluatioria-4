class Helicoptero:
    def __init__(self, marca, modelo, combustible=100):
        self.__marca = marca
        self.__modelo = modelo
        self.__combustible = combustible
        self.__altitud = 0
        self.__velocidad = 0
        self.__motor_encendido = False

    @property
    def altitud(self):
        return self.__altitud

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def motor_encendido(self):
        return self.__motor_encendido

    def __tiene_combustible(self, cantidad):
        return self.__combustible >= cantidad

    def __consumir_combustible(self, cantidad):
        self.__combustible = max(0, self.__combustible - cantidad)

    def encender_motor(self):
        if self.__motor_encendido:
            return "El motor ya se encuentra encendido."
        self.__motor_encendido = True
        return "Motor encendido correctamente."

    def apagar_motor(self):
        if not self.__motor_encendido:
            return "El motor ya se encuentra apagado."
        if self.__altitud > 0:
            return "No es posible apagar el motor mientras el helicoptero esta en vuelo."
        self.__motor_encendido = False
        return "Motor apagado correctamente."

    def despegar(self):
        if not self.__motor_encendido:
            return "Debe encender el motor antes de despegar."
        if self.__altitud > 0:
            return "El helicoptero ya se encuentra en vuelo."
        if not self.__tiene_combustible(10):
            return "Combustible insuficiente para despegar."
        self.__consumir_combustible(10)
        self.__altitud = 100
        return "Despegue realizado con exito."

    def volar(self):
        if not self.__motor_encendido:
            return "Debe encender el motor para volar."
        if self.__altitud == 0:
            return "Debe despegar antes de volar."
        if not self.__tiene_combustible(15):
            return "Combustible insuficiente para continuar el vuelo."
        self.__consumir_combustible(15)
        self.__velocidad = 150
        self.__altitud += 50
        return f"Volando a {self.__velocidad} km/h. Altitud actual: {self.__altitud} metros."

    def aterrizar(self):
        if self.__altitud == 0:
            return "El helicoptero ya se encuentra en tierra."
        self.__altitud = 0
        self.__velocidad = 0
        return "Aterrizaje realizado con exito."

    def __str__(self):
        estado = "Encendido" if self.__motor_encendido else "Apagado"
        return (f"\n===== ESTADO DEL HELICOPTERO =====\n"
                f"Marca: {self.__marca}\nModelo: {self.__modelo}\n"
                f"Combustible: {self.__combustible}%\nAltitud: {self.__altitud} metros\n"
                f"Velocidad: {self.__velocidad} km/h\nMotor: {estado}\n")