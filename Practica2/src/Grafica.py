## Erick Bernal Marquez             317042522
## Ana Valeria Deloya Andrade       317277582

from Canales import *
from Nodos import *
import simpy

class Grafica:
    """Representa una grafica.

    Atributos:
    nombre -- cadena que identifica a la grafica
    adyacencias -- lista de listas, adyacencias[i] representa las adyacencias
                    del i-esimo nodo
    nodos -- lista de nodos de la grafica. Dependiendo el algoritmo que hayamos
              corrido, el tipo de nodo sera distinto.
    """
    def __init__(self, nombre: str, adyacencias: list):
        self.nombre = nombre
        self.adyacencias = adyacencias
        self.nodos = []

    def __str__(self):
        return f'Grafica: (self.nombre), Adyacencias: (self.adyacencias)'

    def get_nombre(self) -> str:
        return self.nombre

    def get_adyacencias(self) -> list:
        return self.adyacencias

    def get_nodos(self) -> list:
        return self.nodos

    def bfs(self, env: simpy.Environment, canal: Canal) -> None:
        """Algoritmo de bfs."""
        self.nodos = []
        for i in range(0, len(self.adyacencias)):
            self.nodos.append(
                NodoBFS(i,self.adyacencias[i],(canal.crea_canal_de_entrada(),canal)))

        for nodo in self.nodos:
            env.process(nodo.bfs(env))

        yield env.timeout(0)


    def dfs(self, env: simpy.Environment, canal: Canal) -> None:
        """Algoritmo de dfs."""
        self.nodos = []

        for i in range(0, len(self.adyacencias)):
            self.nodos.append(
                NodoDFS(i, self.adyacencias[i], 
                    (canal.crea_canal_de_entrada(),canal)))

        for nodo in self.nodos:
            env.process(nodo.dfs(env))

        yield env.timeout(0)