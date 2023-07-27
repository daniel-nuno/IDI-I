# %%
class cola:
    def __init__(self, capacity = 100):
        self.data = []
        self.capacity = capacity
    
    #método enqueue que inserta un elemento al "final" de la cola (si está llena ignora la llamada)
    def enqueue(self, x):
        if self.capacity != len(self.data):
            self.data.append(x)
            #return print("elemento insertado en el tope")
        else:
            return print("pila llena")
    
    #método dequeue que quita y devuelve el elemento al "inicio" de la cola (no previene si la cola está vacía)
    def dequeue(self):
        #print("elemento", self.data[0], "en el tope fue eliminado")
        return self.data.pop(0)

    #método peek que devuelve sin sacar el elemento al "inicio" de la cola (no previene si la cola está vacía)
    def peek(self):
        return print("elemento en el tope es", self.data[0])
    
    #método empty que devuelve un booleano en función de si la cola está vacía o no
    def empty(self):
        return len(self.data) == 0

    #método full que devuelve un booleano en función de si la cola está llena o no
    def full(self):
        return self.capacity == len(self.data)

    #método count que devuelve la cantidad de elementos actual en la cola
    def count(self):
        return len(self.data)
    
    #método print que imprime la cola en el orden que se insertaron los datos
    def print(self):
        return f"{self.data!r}"

    def __repr__(self):
        return f"{self.data!r}"
        #return f"pila({self.data!r})"


class nodo:
    def __init__(self, x):
        self.dato = x
        self.izq = None
        self.der = None

    def imprimir_produndidad(self):
        print(self.dato)
        if self.izq is not None:
            self.izq.imprimir_produndidad()
        if self.der is not None:
            self.der.imprimir_produndidad()

    def minimo_profundida(self):
        min1, min2 = self.dato, self.dato
        if self.izq is not None:
            min1 = self.izq.minimo_profundida()
        if self.der is not None:
            min2 = self.der.minimo_profundida()
        return min(self.dato, min1, min2)

    def minimo_amplitud(self):
        aux = cola()
        minimo = self.dato
        aux.enqueue(self)

        while not aux.empty():
            actual = aux.dequeue()
            minimo = min(minimo, actual.dato)
            if actual.izq is not None:
                aux.enqueue(actual.izq)
            if actual.der is not None:
                aux.enqueue(actual.der)

        return minimo

    def suma_profundidad(self):
        suma_izq = 0
        suma_der = 0
        if self.izq is not None:
            suma_izq = suma_izq + self.izq.suma_profundidad()
        if self.der is not None:
            suma_der = suma_der + self.der.suma_profundidad()
        return suma_izq + suma_der + self.dato

    def suma_amplitud(self):
        aux = cola()
        aux.enqueue(self)
        total = 0

        while not aux.empty():
            actual = aux.dequeue()
            total = total + actual.dato
            if actual.izq is not None:
                aux.enqueue(actual.izq)
            if actual.der is not None:
                aux.enqueue(actual.der)
        
        return total

    def imprimir_amplitud(self):
        aux = cola()
        aux.enqueue(self)

        while not aux.empty():
            actual = aux.dequeue()
            print(actual.dato)
            if actual.izq is not None:
                aux.enqueue(actual.izq)
            if actual.der is not None:
                aux.enqueue(actual.der)


# %%
raiz = nodo(2)
raiz.izq = nodo(5)
raiz.izq.izq = nodo(1)
raiz.izq.der = nodo(4)
raiz.der = nodo(7)
raiz.der.izq = nodo(3)
raiz.der.der = nodo(6)
# %%
suma_de_profundidad = raiz.suma_profundidad()
suma_de_amplitud = raiz.suma_amplitud()
# %%
raiz.imprimir_amplitud()
# %%
