class Incidente:
    def __init__(self, idIncidente, ip, tipoAtaque, nivelRiesgo, estado):
        self.idIncidente = idIncidente
        self.ip = ip
        self.tipoAtaque = tipoAtaque
        self.nivelRiesgo = nivelRiesgo
        self.estado = estado

    def __str__(self):
        return (
            f"ID: {self.idIncidente} | "
            f"IP: {self.ip} | "
            f"Ataque: {self.tipoAtaque} | "
            f"Riesgo: {self.nivelRiesgo} | "
            f"Estado: {self.estado}"
        )


class Alumno:
    def __init__(self, numeroControl, nombre, carrera):
        self.numeroControl = numeroControl
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self):
        return (
            f"Control: {self.numeroControl} | "
            f"Nombre: {self.nombre} | "
            f"Carrera: {self.carrera}"
        )


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return (
            f"Codigo: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f}"
        )