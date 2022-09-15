import Canales
import simpy

class Nodo:
    """Representa un nodo basico.

    Atributos:
    id_nodo -- identificador del nodo
    vecinos -- lista con los ids de nuestros vecinos
    canales -- tupla de la forma (canal_entrada, canal_salida)
    """
    def __init__(self, id_nodo: int, vecinos: list, canales: tuple):
        """Constructor basico de un Nodo."""
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canales = canales

    def __str__(self):
        return f'Nodo: {self.nodos}\n vecinos: {self.vecinos}'
        
    
    def get_id(self) -> int:
        """Regresa el identificador del nodo."""
        return self.id_nodo
    
    def get_vecinos(self) -> list:
        """Regresa la lista de vecinos del nodo."""
        return self.vecinos

    def get_canal_entrada(self) -> simpy.Store:
        """Regresa el canal de entrada del nodo."""
        return self.canales[0]

    def get_canal_salida(self) -> Canales.Canal:
        """Regresa el canal de salida del nodo."""
        return self.canales[1]

class NodoVecinos(Nodo):
    """Nodo que implementa el algoritmo del ejercicio 1.

    Atributos adicionales:
    vecinos_de_vecinos -- lista con los ids de los vecinos de nuestros vecinos
    """
    def __init__(self, id_nodo: int, vecinos: list, canales: tuple):
        """Constructor para el nodo 'vecinos'."""
        #llamamos al padre
        #aunque tambien podriamos con 
        #super.__init__(...), notemos que no necesitamos de self
        Nodo.__init__(self, id_nodo, vecinos, canales)
        self.vecinos_de_vecinos = []


    def conoce_vecinos(self, env: simpy.Environment):
        """Algoritmo para conocer a los vecinos de mis vecinos."""
        #enviar mis vecinos a mis vecinos, pues es el algoritmo que todos los nodos
        #estaran haciendo al mismo tiempo
        canal_salida = self.canales[1]
        #le enviamos nuestros vecinos a nuestros vecinos
        canal_salida.envia(self.vecinos, self.vecinos)
        #recibimos y procesamos los mensajes de mis vecinos, rellenar la lista
        #True pues no sabamos cuantos mensajes vamos a recibir
        while True:
            msg = yield self.canales[0].get() #esperamos el mensaje hasta que tenga un valor
            for vecino in msg: #recordemos que mrecibimos una lista vecino
                if vecino not in self.vecinos_de_vecinos:#verificamos que este
                    self.vecinos_de_vecinos.append(vecino)#lo agregamos si no esta



class NodoArbolGenerador(Nodo):
    """Nodo que implementa el algoritmo del ejercicio 2.

    Atributos adicionales:
    madre -- id del nodo madre dentro del arbol
    hijas -- lista de nodos hijas del nodo actual
    """
    def __init__(self, id_nodo: int, vecinos: list, canales: tuple):
        """Constructor para el nodo arbol generador."""
        raise NotImplementedError('Constructor de NodoArbolGenerador no implementado')

    def genera_arbol(self, env: simpy.Store):
        """Algoritmo para producir el arbol generador."""
        raise NotImplementedError('GeneraArbol de NodoArbolGenerador no implementado')

class NodoBroadcast(Nodo):
    """Nodo que implementa el algoritmo del ejercicio 3.

    Atributos adicionales:
    mensaje -- cadena con el mensaje que se distribuye
    """
    def __init__(self, id_nodo: int, vecinos: list, canales: tuple):
        """Constructor para el nodo broadcast."""
        raise NotImplementedError('Constructor de NodoBroadcast no implementado')

    def broadcast(self, env: simpy.Store):
        """Algoritmo de broadcast."""
        raise NotImplementedError('Broadcast de NodoBroadcast no implementado')
