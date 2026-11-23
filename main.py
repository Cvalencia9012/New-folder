from ArbolBinarioGenerico import ArbolBinarioBusqueda
from modelos import Incidente, Alumno, Producto


def demostrar(titulo, arbol, datos, claveBuscar, claveEliminar):
    print("\n" + "=" * 65)
    print(titulo)
    print("=" * 65)

    for dato in datos:
        arbol.insertar(dato)

    print("\nARBOL:")
    arbol.imprimirArbol()

    print("\nRECORRIDO INORDEN:")
    arbol.recorridoInorden()

    print("\nRECORRIDO PREORDEN:")
    arbol.recorridoPreorden()

    print("\nRECORRIDO POSTORDEN:")
    arbol.recorridoPostorden()

    print("\nCantidad de nodos:", arbol.contarNodos())
    print("Elemento con menor clave:", arbol.obtenerMenor())
    print("Elemento con mayor clave:", arbol.obtenerMayor())

    print(f"\nBUSCAR CLAVE {claveBuscar}:")
    encontrado = arbol.buscar(claveBuscar)

    if encontrado is not None:
        print(encontrado)
    else:
        print("El elemento no existe.")

    print(f"\nELIMINAR CLAVE {claveEliminar}:")

    if arbol.eliminar(claveEliminar):
        print("Elemento eliminado.")
    else:
        print("No se encontro el elemento.")

    print("\nARBOL DESPUES DE ELIMINAR:")
    arbol.imprimirArbol()

    print("\nINORDEN DESPUES DE ELIMINAR:")
    arbol.recorridoInorden()

    print("\nCantidad final de nodos:", arbol.contarNodos())
    print(
        "La clave eliminada sigue presente:",
        arbol.buscar(claveEliminar) is not None
    )


def mainIncidentes():
    arbol = ArbolBinarioBusqueda(
        clave=lambda incidente: incidente.idIncidente
    )

    datos = [
        Incidente(
            105, "192.168.1.10", "Phishing", "Alto", "Abierto"
        ),
        Incidente(
            102, "192.168.1.20", "Escaneo", "Medio", "En revision"
        ),
        Incidente(
            108, "192.168.1.30", "Malware", "Alto", "Abierto"
        ),
        Incidente(
            101, "192.168.1.40", "Intento de acceso", "Bajo", "Cerrado"
        ),
        Incidente(
            106, "192.168.1.50", "Fuerza bruta", "Alto", "En revision"
        ),
        Incidente(
            103, "192.168.1.60", "Escaneo", "Bajo", "Cerrado"
        )
    ]

    demostrar(
        "ARBOL DE INCIDENTES",
        arbol,
        datos,
        claveBuscar=106,
        claveEliminar=102
    )

    print("\nINCIDENTES CON RIESGO ALTO:")

    encontrados = arbol.filtrar(
        lambda incidente: incidente.nivelRiesgo.lower() == "alto"
    )

    for incidente in encontrados:
        print(incidente)


def mainAlumnos():
    arbol = ArbolBinarioBusqueda(
        clave=lambda alumno: alumno.numeroControl
    )

    datos = [
        Alumno(2350005, "Ana", "Ciberseguridad"),
        Alumno(2350002, "Luis", "Sistemas Computacionales"),
        Alumno(2350008, "Carlos", "Mecatronica"),
        Alumno(2350001, "Maria", "Industrial"),
        Alumno(2350006, "Pedro", "Ciberseguridad"),
        Alumno(2350003, "Sofia", "Sistemas Computacionales")
    ]

    demostrar(
        "ARBOL DE ALUMNOS",
        arbol,
        datos,
        claveBuscar=2350006,
        claveEliminar=2350002
    )


def mainProductos():
    arbol = ArbolBinarioBusqueda(
        clave=lambda producto: producto.codigo
    )

    datos = [
        Producto("P105", "Teclado", 650.00),
        Producto("P102", "Mouse", 350.00),
        Producto("P108", "Monitor", 3200.00),
        Producto("P101", "Cable HDMI", 150.00),
        Producto("P106", "Audifonos", 800.00),
        Producto("P103", "Memoria USB", 180.00)
    ]

    demostrar(
        "ARBOL DE PRODUCTOS",
        arbol,
        datos,
        claveBuscar="P106",
        claveEliminar="P102"
    )


if __name__ == "__main__":
    mainIncidentes()
    mainAlumnos()
    mainProductos()