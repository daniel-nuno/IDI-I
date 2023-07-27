# %%
class pila:
    def __init__(self, capacity = 100):
        self.data = []
        self.capacity = capacity
    
    #método push que inserta un elemento en el "tope" de la pila (si está llena ignora la llamada)
    def push(self, x):
        if self.capacity != len(self.data):
            self.data.append(x)
            #return print("elemento insertado en el tope")
        else:
            return print("pila llena")
    
    #método pop que quita y devuelve el elemento en el "tope" de la pila (no previene si la pila está vacía)
    def pop(self):
        print("elemento", self.data[-1], "en el tope fue eliminado")
        self.data.pop()

    #método peek que devuelve sin sacar el elemento en el "tope" de la pila (no previene si la pila está vacía)
    def peek(self):
        return print("elemento en el tope es", self.data[-1])
    
    #método empty que devuelve un booleano en función de si la pila está vacía o no
    def empty(self):
        return len(self.data) == 0

    #método full que devuelve un booleano en función de si la pila está llena o no
    def full(self):
        return self.capacity == len(self.data)

    #método count que devuelve la cantidad de elementos actual en la pila
    def count(self):
        return len(self.data)
    
    #método print que imprime la pila en el orden que se insertaron los datos
    def print(self):
        return f"{self.data!r}"

    def __repr__(self):
        return f"{self.data!r}"
        #return f"pila({self.data!r})"


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
        print("elemento", self.data[0], "en el tope fue eliminado")
        self.data.pop(0)

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

# %%
#Ahora use sus clases para generar una pila llamada pila1 de capacidad 50 en la que se apilen los primeros 50 números naturales impares.
#Ahora cree una cola llamada cola1 de capacidad 50 y encole los elementos de la pila1
#Imprima ambas estructuras para comprobar.

pila1 = pila(50)
for i in range(50):
    pila1.push(i * 2 + 1)

cola1 = cola(50)
for i in range( len(pila1.data) -1, -1, -1):
    cola1.enqueue(pila1.data[i])

print("pila1:", pila1.print())
print("cola1:", cola1.print())

# %%
# %%
