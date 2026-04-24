# Estructuras de Datos en Python

Implementación de pilas, colas y listas.


## Integrantes del Equipo

| Nombre Completo | Código |
|-----------------|--------|
| [Daniel Sebastian Cuaichar Pulido] | [2232264] |


## Estructura

```
pilas.py     Parte A — Pilas
colas.py     Parte B — Colas
listas.py    Parte C — Listas Enlazadas
```


## Pilas

`balanceado(exp)` verifica si los símbolos `()`, `[]` y `{}` están correctamente balanceados en una expresión, apilando aperturas y comparando contra el tope al encontrar un cierre. Corre en O(n).

`decimal_a_binario(n)` convierte un entero a binario apilando los residuos de dividir entre 2 y desapilándolos al final para formar el resultado. Maneja el caso cero y números negativos.

## Colas

`simulacion_turnos(clientes)` atiende clientes en orden de llegada usando `collections.deque`, ya que `popleft()` es O(1) frente al O(n) de `list.pop(0)`.

`cola_prioridad(tareas)` atiende tareas según prioridad usando `heapq`. Cada tarea se inserta como `(prioridad, índice, tarea)`; el índice rompe empates de forma estable y evita que el heap intente comparar objetos no comparables cuando dos tareas tienen la misma prioridad.

## Listas Enlazadas

Tanto la lista simple como la doblemente enlazada mantienen punteros a `head` y `tail`. Esto convierte `insert_end` en O(1) y permite que `traverse_backward` en la lista doble parta directamente del final, sin tener que recorrer la lista hacia adelante primero. Las inserciones al inicio son O(1) y los recorridos completos son O(n).
