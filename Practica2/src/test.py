## Erick Bernal Marquez             317042522
## Ana Valeria Deloya Andrade       317277582

from Canales import *
from Grafica import *
from Nodos import *
import simpy

# Las unidades de tiempo que les daremos a las pruebas
TIEMPO_DE_EJECUCION = 50

class Test_Practica2:
    """Pruebas para la practica 2.""" #necesitamos verlo como conjuntos para dfs
    adyacencias = [{1, 3, 4, 6}, {0, 3, 5, 7}, {3, 5, 6}, {0, 1, 2}, {0}, {1, 2}, {0, 2}, {1}]

    g = Grafica('A', adyacencias)

    def get_ambiente_y_canal(self) -> tuple:
        """Funcion auxiliar para preparar las pruebas."""
        env = simpy.Environment()
        canal = CanalGeneral(env)
        return (env, canal)

    def uno(self):
        """Prueba el algoritmo 'BFS'."""
        env, canal = self.get_ambiente_y_canal()

        env.process(self.g.bfs(env, canal))

        env.run(until=TIEMPO_DE_EJECUCION)

        # Comprobamos los resultados
        padres_esperados = [0, 0, 3, 0, 0, 1, 0, 1]
        niveles_esperados = [0, 1, 2, 1, 1, 2, 1, 2]
        nodos_res = self.g.get_nodos()
        # Para cada nodo verificamos que su lista de identifiers sea la esperada.
        for i in range(0, len(nodos_res)):
            nodo = nodos_res[i]
            assert nodo.padre == padres_esperados[i],\
                (f'El nodo {nodo.id_nodo} tiene mal padre.\n\
                    Padre actual: {nodo.padre}\nPadre esperado: {padres_esperados[i]}')
            assert nodo.nivel == niveles_esperados[i],\
                (f'El nodo {nodo.id_nodo} tiene mal nivel.\n\
                    Nivel actual: {nodo.nivel}\nNivel esperado: {niveles_esperados[i]}')

    def dos(self):
        """Prueba el algoritmo 'DFS'."""
        env, canal = self.get_ambiente_y_canal()

        env.process(self.g.dfs(env, canal))

        env.run(until=TIEMPO_DE_EJECUCION)
      
        # Comprobamos los resultados
        padres_esperados = [0, 0, 3, 1, 0, 2, 2, 1]
        hijos_esperados = [{1, 4}, {3, 7}, {5, 6}, {2}, set(), set(), set(), set()]
        nodos_res = self.g.get_nodos()
        # Para cada nodo verificamos que su lista de identifiers sea la esperada.
        for i in range(0, len(nodos_res)):
            nodo = nodos_res[i]
            assert nodo.padre == padres_esperados[i],\
                (f'El nodo {nodo.id_nodo} tiene mal padre.\n\
                    Padre actual: {nodo.padre}\nPadre esperado: {padres_esperados[i]}')


pruebas = Test_Practica2()
pruebas.uno() 
#pruebas.dos()
