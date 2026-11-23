class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijoIzquierdo = None
        self.hijoDerecho = None


class ArbolBinarioBusqueda:
    def __init__(self, clave):
        self.raiz = None
        self.clave = clave

    def insertar(self, dato):
        nuevo = Nodo(dato)
        claveDato = self.clave(dato)

        if self.raiz is None:
            self.raiz = nuevo
            return True

        actual = self.raiz

        while True:
            claveActual = self.clave(actual.dato)

            if claveDato == claveActual:
                print(f"Ya existe un elemento con clave {claveDato}.")
                return False

            if claveDato < claveActual:
                if actual.hijoIzquierdo is None:
                    actual.hijoIzquierdo = nuevo
                    return True

                actual = actual.hijoIzquierdo
            else:
                if actual.hijoDerecho is None:
                    actual.hijoDerecho = nuevo
                    return True

                actual = actual.hijoDerecho

    def buscar(self, clave):
        actual = self.raiz

        while actual is not None:
            claveActual = self.clave(actual.dato)

            if clave == claveActual:
                return actual.dato
            elif clave < claveActual:
                actual = actual.hijoIzquierdo
            else:
                actual = actual.hijoDerecho

        return None

    def eliminar(self, clave):
        self.raiz, eliminado = self._eliminar(self.raiz, clave)
        return eliminado

    def _eliminar(self, nodo, clave):
        if nodo is None:
            return None, False

        claveActual = self.clave(nodo.dato)

        if clave < claveActual:
            nodo.hijoIzquierdo, eliminado = self._eliminar(
                nodo.hijoIzquierdo, clave
            )

        elif clave > claveActual:
            nodo.hijoDerecho, eliminado = self._eliminar(
                nodo.hijoDerecho, clave
            )

        else:
            # Sin hijo izquierdo: devuelve el derecho.
            # También cubre el caso de un nodo sin hijos.
            if nodo.hijoIzquierdo is None:
                return nodo.hijoDerecho, True

            # Solo tiene hijo izquierdo.
            if nodo.hijoDerecho is None:
                return nodo.hijoIzquierdo, True

            # Tiene dos hijos: busca el menor del subárbol derecho.
            sucesor = nodo.hijoDerecho

            while sucesor.hijoIzquierdo is not None:
                sucesor = sucesor.hijoIzquierdo

            # Se reemplaza el objeto completo.
            nodo.dato = sucesor.dato

            # Se elimina la posición anterior del sucesor.
            nodo.hijoDerecho, _ = self._eliminar(
                nodo.hijoDerecho,
                self.clave(sucesor.dato)
            )

            eliminado = True

        return nodo, eliminado

    def recorridoInorden(self):
        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.hijoIzquierdo)
                print(nodo.dato)
                recorrer(nodo.hijoDerecho)

        recorrer(self.raiz)

    def recorridoPreorden(self):
        def recorrer(nodo):
            if nodo is not None:
                print(nodo.dato)
                recorrer(nodo.hijoIzquierdo)
                recorrer(nodo.hijoDerecho)

        recorrer(self.raiz)

    def recorridoPostorden(self):
        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.hijoIzquierdo)
                recorrer(nodo.hijoDerecho)
                print(nodo.dato)

        recorrer(self.raiz)

    def imprimirArbol(self):
        if self.raiz is None:
            print("El arbol esta vacio.")
            return

        def imprimir(nodo, prefijo="", etiqueta="Raiz: "):
            if nodo is None:
                return

            print(prefijo + etiqueta + str(self.clave(nodo.dato)))

            imprimir(
                nodo.hijoIzquierdo,
                prefijo + "    ",
                "Izq: "
            )

            imprimir(
                nodo.hijoDerecho,
                prefijo + "    ",
                "Der: "
            )

        imprimir(self.raiz)

    def contarNodos(self):
        def contar(nodo):
            if nodo is None:
                return 0

            return (
                1
                + contar(nodo.hijoIzquierdo)
                + contar(nodo.hijoDerecho)
            )

        return contar(self.raiz)

    def obtenerMenor(self):
        actual = self.raiz

        if actual is None:
            return None

        while actual.hijoIzquierdo is not None:
            actual = actual.hijoIzquierdo

        return actual.dato

    def obtenerMayor(self):
        actual = self.raiz

        if actual is None:
            return None

        while actual.hijoDerecho is not None:
            actual = actual.hijoDerecho

        return actual.dato

    def filtrar(self, condicion):
        encontrados = []

        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.hijoIzquierdo)

                if condicion(nodo.dato):
                    encontrados.append(nodo.dato)

                recorrer(nodo.hijoDerecho)

        recorrer(self.raiz)
        return encontrados