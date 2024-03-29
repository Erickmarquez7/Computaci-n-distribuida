#Integrantes:
#Bernal Márquez Erick           317042522
#Deloya Andrade Ana valeria     317277582
from Canales import *
from Grafica import *
from Nodos import *
import simpy

# Las unidades de tiempo que les daremos a las pruebas
TIEMPO_DE_EJECUCION = 50

class Test_Practica1:
    """Pruebas para la practica 1."""
    adyacencias = [[1, 2], [0, 3], [0, 3, 5], [1, 2, 4], [3, 5], [2, 4]]
    adyacencias_arbol = [[1, 2], [3], [5], [4], [], []]

    g = Grafica('A', adyacencias=adyacencias)

    def get_ambiente_y_canal(self) -> tuple:
        """Funcion auxiliar para preparar las pruebas."""
        env = simpy.Environment()
        canal = CanalGeneral(env)
        return (env, canal)

    def uno(self):
        """Prueba el algoritmo 'Conocer a los vecinos de mis vecinos'."""
        env, canal = self.get_ambiente_y_canal()

        env.process(self.g.conoce_vecinos(env, canal))

        env.run(until=TIEMPO_DE_EJECUCION)

        # Comprobamos los resultados
        identifiers_esperados = [[0, 3, 5], [1, 2, 4], [1, 2, 4], [0, 3, 5],
                                 [1, 2, 4], [0, 3, 5]]
        nodos_res = self.g.get_nodos()
        # Para cada nodo verificamos que su lista de identifiers sea la esperada.
        for i in range(0, len(nodos_res)):
            nodo = nodos_res[i]
            assert set(identifiers_esperados[i]) == set(nodo.vecinos_de_vecinos), \
                   ('El nodo %d está mal' % nodo.id_nodo)
    
    def dos(self):
        """Prueba el algoritmo 'Creacion de arbol generador'."""
        env, canal = self.get_ambiente_y_canal()

        env.process(self.g.genera_arbol_generador(env, canal))

        env.run(until=TIEMPO_DE_EJECUCION)

        # Y probamos que los padres y los hijos sean los correctos.
        padres = [0, 0, 0, 1, 3, 2]
        hijos = [[1, 2], [3], [5], [4], [], []]
        nodos_res = self.g.get_nodos()
        for i in range(0, len(nodos_res)):
            nodo = nodos_res[i]
            assert nodo.madre == padres[i],\
                   ('El nodo %d tiene un padre erróneo' % nodo.id_nodo)
            assert set(nodo.hijas) == set(hijos[i]), \
                   ('El nodo %d no tiene a los hijos correctos' % nodo.id_nodo)

    def tres(self):
        """Prueba el algoritmo 'Creacion de arbol generador'."""
        env, canal = self.get_ambiente_y_canal()

        env.process(self.g.broadcast(env, canal, self.adyacencias_arbol))

        env.run(until=TIEMPO_DE_EJECUCION)

        # Probamos que todos los nodos tengan ya el mensaje
        nodos_res = self.g.nodos
        mensaje_enviado = nodos_res[0].mensaje
        for nodo in nodos_res:
            assert mensaje_enviado == nodo.mensaje,\
            ('El nodo %d no tiene el mensaje correcto' % nodo.id_nodo)


pruebas = Test_Practica1()
#pruebas.uno() 
#pruebas.dos()
pruebas.tres()
