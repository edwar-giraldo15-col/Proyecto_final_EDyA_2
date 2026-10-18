import heapq

# 1. LISTA ENLAZADA SIMPLE 
class NodoLista:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = NodoLista(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def obtener_todos(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

# 2. COLA / QUEUE
    def __init__(self):
        self.items = []

    def encolar(self, pedido):
        self.items.append(pedido)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def obtener_todos(self):
        return self.items

# 3. ÁRBOL BINARIO DE BÚSQUEDA 
class NodoArbol:
    def __init__(self, id_pedido, datos):
        self.id_pedido = id_pedido
        self.datos = datos
        self.izq = None
        self.der = None

class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, id_pedido, datos):
        if not self.raiz:
            self.raiz = NodoArbol(id_pedido, datos)
        else:
            self._insertar_rec(self.raiz, id_pedido, datos)

    def _insertar_rec(self, nodo, id_pedido, datos):
        if id_pedido < nodo.id_pedido:
            if nodo.izq is None:
                nodo.izq = NodoArbol(id_pedido, datos)
            else:
                self._insertar_rec(nodo.izq, id_pedido, datos)
        else:
            if nodo.der is None:
                nodo.der = NodoArbol(id_pedido, datos)
            else:
                self._insertar_rec(nodo.der, id_pedido, datos)

    def buscar(self, id_pedido):
        return self._buscar_rec(self.raiz, id_pedido)

    def _buscar_rec(self, nodo, id_pedido):
        if nodo is None or nodo.id_pedido == id_pedido:
            return nodo.datos if nodo else None
        if id_pedido < nodo.id_pedido:
            return self._buscar_rec(nodo.izq, id_pedido)
        return self._buscar_rec(nodo.der, id_pedido)

# 4. MIN-HEAP
class HeapPrioridad:
    def __init__(self):
        self.heap = []

    def agregar(self, prioridad, descripcion):
        heapq.heappush(self.heap, (prioridad, descripcion))

    def atender_urgente(self):
        if self.heap:
            return heapq.heappop(self.heap) 
        return None

    def obtener_todos(self):
        return sorted(self.heap)

# 5. GRAFO / MAPA DE RUTAS 
class GrafoRutas:
    def __init__(self):
        self.adj = {}  # Lista adyacete usando un diccionario

    def agregar_sucursal(self, nombre):
        if nombre not in self.adj:
            self.adj[nombre] = []

    def agregar_conexion(self, origen, destino, distancia):
        self.agregar_sucursal(origen)
        self.agregar_sucursal(destino)
        self.adj[origen].append({"destino": destino, "distancia": distancia})
        self.adj[destino].append({"destino": origen, "distancia": distancia})  # Conexión bidireccional

    def obtener_mapa(self):
        return self.adj