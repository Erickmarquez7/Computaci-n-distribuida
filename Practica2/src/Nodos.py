import Canales
import math
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
        """Regresa la representacion en cadena del nodo."""
        return f'Nodo: (self.id_nodo), Vecinos: (self.vecinos)'
    
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

class NodoBFS(Nodo):
    """Nodo que implementa el algoritmo del ejercicio 1.

    Atributos adicionales:
    padre -- id del nodo que sera su padre en el arbol
    nivel -- entero que representa la distancia del nodo a la raiz
    hijos -- lista de ids de los nodos hijos del nodo
    msjs_esperados -- numero de mensajes que espera el nodo
    """
    def __init__(self, id_nodo: int, vecinos: list, canales: tuple):
        """Constructor para el nodo 'bfs'."""
        Nodo.__init__(self, id_nodo, vecinos, canales)
        #id nodo
        #vecinos
        #canales
        self.padre=0
        self.hijos=[]
        self.nivel=float('inf')
        self.msg_esperados=0


    def bfs(self, env: simpy.Environment):
        """Algoritmo de BFS."""
        #si es el nodo inicial lo hacemos su propio padre
        if self.id_nodo == 0:
            self.nivel = 0
            #solo hace falta enviar el id y el nivel que será el siguiente nodo
            msj = (self.id_nodo, 1)
            self.canales[1].envia(msj, self.vecinos)
            
        #notemos que solo hace falta esparcir el mensje ya que cambiará de padre automaticamente
        #sin tener que poner back
        while True:
            #llega el mensaje.
            padre, n = yield self.canales[0].get()

            #si es menor toma este nuevo como su padre
            if n < self.nivel: 
                self.padre = padre
                self.nivel = n
                msj = (self.id_nodo, self.nivel+1)
                self.canales[1].envia(msj, self.vecinos)