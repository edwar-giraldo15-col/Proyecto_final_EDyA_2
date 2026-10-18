from flask import Flask, jsonify, request, render_template
from proyecto_final_ED2 import ListaEnlazada, ColaPedidos, ArbolBusqueda, HeapPrioridad, GrafoRutas

app = Flask(__name__)

lista_clientes = ListaEnlazada()
cola_pedidos = ColaPedidos()
arbol_pedidos = ArbolBusqueda()
heap_urgentes = HeapPrioridad()
grafo_rutas = GrafoRutas()

# Cargar algunas rutas iniciales en el Grafo
grafo_rutas.agregar_conexion("Centro", "Norte", 12)
grafo_rutas.agregar_conexion("Centro", "Sur", 15)
grafo_rutas.agregar_conexion("Norte", "Oriente", 8)


# 1. LISTA ENLAZADA: Clientes
@app.route('/api/clientes', methods=['GET', 'POST', 'DELETE'])
def gestionar_clientes():
    # AGREGAR CLENTE
    if request.method == 'POST':
        data = request.json
        nombre = data.get('nombre')
        if nombre:
            lista_clientes.agregar(nombre)
            return jsonify({"mensaje": f"Cliente '{nombre}' agregado a la Lista Enlazada."}), 201
        return jsonify({"error": "Nombre es requerido"}), 400

    # ELIMINAR CLIENTE
    if request.method == 'DELETE':
        data = request.get_json(silent=True)
        nombre_a_eliminar = data.get('nombre') if data else None
        if nombre_a_eliminar:
            eliminado = lista_clientes.eliminar(nombre_a_eliminar)
            if eliminado:
                return jsonify({"mensaje": f"Cliente '{nombre_a_eliminar}' eliminado."}), 200
            return jsonify({"error": "Cliente no encontrado"}), 404
        return jsonify({"error": "Nombre a eliminar es requerido"}), 400

    #  CONSULTAR CLIENTES 
    return jsonify({"clientes": lista_clientes.obtener_todos()})
    


# 2. COLA (Queue): Pedidos Normales
@app.route('/api/cola', methods=['GET', 'POST', 'DELETE'])
def gestionar_cola():
    if request.method == 'POST':
        data = request.json
        pedido = data.get('pedido')
        id_pedido = data.get('id')
        
        if pedido and id_pedido:
            cola_pedidos.encolar({"id": id_pedido, "descripcion": pedido})
            arbol_pedidos.insertar(int(id_pedido), {"descripcion": pedido})
            return jsonify({"mensaje": f"Pedido '{pedido}' agregado a la Cola."}), 201
        return jsonify({"error": "Datos incompletos"}), 400

    if request.method == 'DELETE':
        despachado = cola_pedidos.desencolar()
        if despachado:
            return jsonify({"mensaje": "Pedido despachado de la Cola", "pedido": despachado})
        return jsonify({"mensaje": "La cola está vacía"}), 404

    return jsonify({"cola": cola_pedidos.obtener_todos()})


# 3. ÁRBOL BINARIO: Buscar Pedido por ID
@app.route('/api/arbol/buscar/<int:id_pedido>', methods=['GET'])
def buscar_en_arbol(id_pedido):
    resultado = arbol_pedidos.buscar(id_pedido)
    if resultado:
        return jsonify({"encontrado": True, "id": id_pedido, "datos": resultado})
    return jsonify({"encontrado": False, "mensaje": "Pedido no registrado"}), 404


# 4. MIN-HEAP: Envíos Urgentes
@app.route('/api/heap', methods=['GET', 'POST', 'DELETE'])
def gestionar_heap():
    if request.method == 'POST':
        data = request.json
        prioridad = data.get('prioridad')  # Nivel de urgencia (1 = Máxima urgencia)
        descripcion = data.get('descripcion')
        
        if prioridad is not None and descripcion:
            heap_urgentes.agregar(int(prioridad), descripcion)
            return jsonify({"mensaje": "Pedido urgente agregado al Min-Heap"}), 201
        return jsonify({"error": "Datos incompletos"}), 400

    if request.method == 'DELETE':
        atendido = heap_urgentes.atender_urgente()
        if atendido:
            return jsonify({
                "mensaje": "Pedido más urgente despachado del Heap", 
                "prioridad": atendido[0], 
                "descripcion": atendido[1]
            })
        return jsonify({"mensaje": "El Heap está vacío"}), 404

    # devolmos una lista bonita en JSON
    elementos = [{"prioridad": p, "descripcion": d} for p, d in heap_urgentes.obtener_todos()]
    return jsonify({"heap": elementos})


# 5. GRAFO: Mapa de Rutas
@app.route('/api/grafo', methods=['GET', 'POST'])
def gestionar_grafo():
    if request.method == 'POST':
        data = request.json
        origen = data.get('origen')
        destino = data.get('destino')
        distancia = data.get('distancia')
        
        if origen and destino and distancia:
            grafo_rutas.agregar_conexion(origen, destino, int(distancia))
            return jsonify({"mensaje": f"Conexión agregada entre {origen} y {destino}"}), 201
        return jsonify({"error": "Datos incompletos"}), 400

    return jsonify({"mapa": grafo_rutas.obtener_mapa()})


# Ruta principal para cargar la página de inicio 
@app.route('/')
def inicio():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)