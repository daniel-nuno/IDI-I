# %%
# la nueva función se llama alfa_beta y para ver cómo funciona imprimo los nodos que revisa.
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
    
    def maximo_profundidad(self):
        max1, max2 = self.dato, self.dato
        if self.izq is not None:
            max1 = self.izq.maximo_profundidad()
        if self.der is not None:
            max2 = self.der.maximo_profundidad()
        return max(self.dato, max1, max2)

    def si_esta_profundidad(self, x):
        if self.dato == x:
            return True
        if self.izq is not None:
            if self.izq.si_esta_profundidad(x):
                return True
        if self.der is not None:
            if self.der.si_esta_profundidad(x):
                return True
        return False

    def cuantas_veces_profundidad(self, x):
        suma_izq = 0
        suma_der = 0
        if self.dato == x:
            cuenta = 1
        else:
            cuenta = 0
        
        if self.izq is not None:
            suma_izq = suma_izq + self.izq.cuantas_veces_profundidad(x)
        if self.der is not None:
            suma_der = suma_der + self.der.cuantas_veces_profundidad(x)
        return suma_izq + suma_der + cuenta      

    def busqueda_amplitud(self, x):
        aux = cola()
        aux.enqueue(self)
        total = 0

        while not aux.empty():
            actual = aux.dequeue()
            total = total + 1
            if actual.dato == x:
                return total
            if actual.izq is not None:
                aux.enqueue(actual.izq)
            if actual.der is not None:
                aux.enqueue(actual.der)
        
        return total

    def crear_arbol_aplitud(self, N):
        primes = cola(N-1)
        count = 0
        n = self.dato + 1
        while count != N-1:
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    break
            else:
                primes.enqueue(n)
                count = count + 1
            n = n + 1
        
        aux = cola()
        aux.enqueue(self)
        while not primes.empty():
            actual = aux.dequeue()
            if actual.izq is None and not primes.empty():
                prime = primes.dequeue()
                actual.izq = nodo(prime)
                aux.enqueue(actual.izq)
            if actual.der is None and not primes.empty():
                prime = primes.dequeue()
                actual.der = nodo(prime)
                aux.enqueue(actual.der)

        return self

    def minimax2(self, profundidad: int, maximo: bool):
        if profundidad == 1 or (self.izq is None and self.der is None):
            return self.dato, ' '
        if maximo:
            if self.izq is not None:
                value_izq = self.izq.minimax2(profundidad-1, False)
            if self.der is not None:
                value_der = self.der.minimax2(profundidad-1, False)
            return (max(value_izq[0], value_der[0]), 'IZQ' if value_izq[0] >= value_der[0] else 'DER')
        else:
            if self.izq is not None:
                value_izq = self.izq.minimax2(profundidad-1, True)
            if self.der is not None:
                value_der = self.der.minimax2(profundidad-1, True)
            return (min(value_izq[0], value_der[0]), 'IZQ' if value_izq[0] <= value_der[0] else 'DER')

    def alfa_beta(self, profundidad: int, maximo: bool, a = (float('-inf'), ' '), b = (float('inf'), ' ')):
        if profundidad == 1 or (self.izq is None and self.der is None):
            print(self.dato)
            return self.dato, ' '

        if maximo:
            if self.izq is not None:
                value_izq = self.izq.alfa_beta(profundidad-1, False, a, b)
                a = max(a[0], value_izq[0]), 'IZQ'
                if a[0] >= b[0]:
                    return b[0], 'IZQ'
            if self.der is not None:
                value_der = self.der.alfa_beta(profundidad-1, False, a, b)
                a = max(a[0], value_der[0]), 'DER'
                if a[0] >= b[0]:
                    return b[0], 'DER'
            return (max(value_izq[0], value_der[0]), 'IZQ' if value_izq[0] >= value_der[0] else 'DER')

        else:
            if self.izq is not None:
                value_izq = self.izq.alfa_beta(profundidad-1, True, a, b)
                b = min(b[0], value_izq[0]), 'IZQ'
                if b[0] <= a[0]:
                    return a[0], 'IZQ'
            if self.der is not None:
                value_der = self.der.alfa_beta(profundidad-1, True, a, b)
                b = min(b[0], value_der[0]), 'DER'
                if b[0] <= a[0]:
                    return a[0], 'DER'     
            return (min(value_izq[0], value_der[0]), 'IZQ' if value_izq[0] <= value_der[0] else 'DER')

#árbol prueba ultimo nivel
raiz = nodo(0)

raiz.izq = nodo(0)

raiz.der = nodo(0)

raiz.izq.izq = nodo(0)
raiz.izq.der = nodo(0)

raiz.der.izq = nodo(0)
raiz.der.der = nodo(0)

raiz.izq.izq.izq = nodo(3)
raiz.izq.izq.der = nodo(5)
raiz.izq.der.izq = nodo(6)
raiz.izq.der.der = nodo(9)

raiz.der.izq.izq = nodo(1)
raiz.der.izq.der = nodo(2)
raiz.der.der.izq = nodo(0)
raiz.der.der.der = nodo(-1)
# %%
prueba1 = raiz.alfa_beta(4, True)
print(prueba1)
# %%
