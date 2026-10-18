# Proyecto_final_EDyA_2
Proyecto final de la clase estructura de datos 2
Plataforma de Gestión de Envíos y Logística
> **Proyecto Final - Estructura de Datos y Algoritmos II**

Aplicación web desarrollada en Python con Flask para la gestión visual en tiempo real de clientes, pedidos, prioridades de urgencia y rutas de distribución mediante la implementación práctica de 5 estructuras de datos fundamentales.

Integrante : Edward Orlando Giraldo Fernández
Código: 2244783

Tecnologías Utilizadas
Lenguaje Backend: Python 
Framework Web: Flask
Frontend: HTML5, CSS3, JavaScript 

Estructuras de Datos Implementadas

Módulo - Estructura de Datos - Justificación Teórica y Uso en el Sistema

| 1 | **Registro de Clientes** | Lista Enlazada Simple | Permite una inserción y eliminación dinámica de clientes de forma secuencial con punteros sin reservar bloques contiguos rígidos de memoria. |

| 2 | **Gestión de Pedidos** | Cola (Queue - FIFO) | Cumple el principio *First In, First Out*. Garantiza que el primer pedido recibido sea el primero en despacharse en la fila de espera. |

| 3 | **Búsqueda de Pedidos** | Árbol Binario de Búsqueda | Organiza los IDs de los pedidos de forma jerárquica, optimizando la búsqueda de registros a una complejidad . |

| 4 | **Control de Urgencias** | Min-Heap | Mantiene en la cima el elemento con menor valor numérico de prioridad, permitiendo atender inmediatamente la emergencia más crítica. |

| 5 | **Mapa de Conexiones** | Grafo  | Modela la red física de sucursales (vértices) y las distancias entre ellas (aristas ponderadas) para análisis de rutas. |
