# -*- coding: utf-8 -*-
# Parte B — Colas
from collections import deque
import heapq

# TODO 3: Simulación de turnos con cola
def simulacion_turnos(clientes):
    cola = deque(clientes)
    turno = 1
    while cola:
        atendido = cola.popleft()  # FIFO en O(1)
        print(f"Turno {turno}: atendiendo a {atendido}")
        turno += 1

# TODO 4: Cola de prioridad de tareas con heapq
def cola_prioridad(tareas):
    heap = []
    # Se incluye un contador para romper empates de forma estable
    for i, (prioridad, tarea) in enumerate(tareas):
        heapq.heappush(heap, (prioridad, i, tarea))

    while heap:
        prioridad, _, tarea = heapq.heappop(heap)
        print(f"Prioridad {prioridad}: {tarea}")

if __name__ == "__main__":
    print("== Colas ==")
    print("Simulación de turnos:")
    simulacion_turnos(["Cliente1", "Cliente2", "Cliente3"])

    print("\nCola de prioridad:")
    cola_prioridad([(2, "tarea media"), (1, "tarea alta"), (3, "tarea baja")])
