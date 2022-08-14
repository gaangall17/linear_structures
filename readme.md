### Tipos de colecciones/estructuras:

> - Dinamicas
> - Inmutables

### Estructura Lineal

Tiene un orden. Listas, Queues, Strings

### Estrcutura Jerarquica

Tiene estructura de arbol, con objetos padres e hijos

### Estructura Grafos

Los objetos tienen uno o mas vecinos. Como las rutas o enlaces de comunicacion

### Estructura Desordenada

No existe orden, predecesores, sucesores. Como los diccionarios o los conjuntos

### Estructura Ordenada

Llevan una secuencia segun una regla

## Operaciones con Estructuras

> - Concatenacion
> - Conversion
> - Insertar
> - Remover
> - Reemplazar
> - Acceder

## Colecciones incorporadas

> - Listas [  ]
> - Tuplas (  )
> - Conjuntos {  }
> - Diccionarios {  :  }

## Array

Los Arrays son listas con la restriccion de que sus dimensiones y tamano son declaradas al inicio y no se pueden cambiar.  
Optimiza la memoria al establecer desde el inicio la cantidad de bits a utilizar

## Linked Structures

Consiste en nodos. Recorremos los nodos hasta llegar al valor

> - Data: Valor almacenado en el nodo
> - Next: Referencia al siguiente nodo
> - Previous: Referencia al nodo anterior
> - Head: Primer nodo
> - Tail: Ultimo nodo

Son utilizados para generar estructuras más complejas como Queues

Son utilizados en Hacer/Rehacer y en Historal de un navegador

## Circular Linked Structures

Igual que una Singly Linked List pero head.next ahora referencia a tail

## Stacks

Colección lineal basada en arreglos o linked lists con la funcionalidad **LIFO** (Last-in First-out)

Entre sus métodos se encuentran PUSH (Añadir) y POP (Remover)

Entre sus atributos se encuentran TOP (último valor agregado) y BOTTOM (Primer valor agregado)

> - .is_empty()
> - .__len__()
> - .__str__()
> - .__iter__(): Iteración de TOP a BOTTOM
> - .__contains__(item)
> - .__add__(stack2)
> - .clear()
> - .peek(): Retorna el elemento TOP
> - .push(item):
> - .pop():

## Queues

Collección lineal con la funcionalidad **FIFO** (First-in First-out)

Los elementos pueden tener prioridad, alterando la regla FIFO

Entre sus atributos se encuentran REAR (último valor agregado) y FRONT (Valor más antiguo)

> - .is_empty()
> - .__len__()
> - .__str__()
> - .__iter__(): Iteración de FRONT a REAR
> - .__contains__(item)
> - .__add__(queue2)
> - .clear()
> - .peek(): Retorna el elemento FRONT
> - .add(item):
> - .pop():