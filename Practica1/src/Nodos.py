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
        raise NotImplementedError('Constructor de Nodo no implementado')

    def __str__(self):
        """Regresa la representacion en cadena del nodo."""
        raise NotImplementedError('Str de Nodo no implementado')
    
    def get_id(self) -> int:
        """Regresa el identificador del nodo."""
        raise NotImplementedError('Get_id de Nodo no implementado')
    
    def get_vecinos(self) -> list:
        """Regresa la lista de vecinos del nodo."""
        raise NotImplementedError('Get_vecinos de Nodo no implementado')

    def get_canal_entrada(self) -> simpy.Store:
        """Regresa el canal de entrada del nodo."""
        raise NotImplementedError('Get_canal_entrada de Nodo no implementado')

    def get_canal_salida(self) -> simpy.Store:
        """Regresa el canal de salida del nodo."""
        raise NotImplementedError('Get_canal_salida de Nodo no implementado')

class NodoVecinos(Nodo):
    """Nodo que implementa el algoritmo del ejercicio 1.

    Atributos adicionales:
    vecinos_de_vecinos -- lista con los ids de los vecinos de nuestros vecinos
    """
    def __init__(self):
        """Constructor para el nodo 'vecinos'."""
        raise NotImplementedError('Constructor de NodoVecinos no implementado')

    def conoce_vecinos(self, env: simpy.Environment):
        """Algoritmo para conocer a los vecinos de mis vecinos."""
        raise NotImplementedError('Conoce_vecinos de NodoVecinos no implementado')

class NodoArbolGenerador(Nodo):
    """Nodo que implementa el algoritmo del ejercicio 2.

    Atributos adicionales:
    madre -- id del nodo madre dentro del arbol
    hijas -- lista de nodos hijas del nodo actual
    """
    def __init__(self):
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
    def __init__(self):
        """Constructor para el nodo broadcast."""
        raise NotImplementedError('Constructor de NodoBroadcast no implementado')

    def broadcast(self, env: simpy.Store):
        """Algoritmo de broadcast."""
        raise NotImplementedError('Broadcast de NodoBroadcast no implementado')