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

        self.padre=None
        self.hijos=[]

        self.nivel=float('inf')
        self.msg_esperados=0


    def bfs(self, env: simpy.Environment):
        """Algoritmo de BFS."""
        # if self.get_id() == 0:
        #     self.padre = self.get_id()
        

        #     #mensajes esperados
        #     self.msg_esperados = len(self.vecinos)

        #     tipo = 'go'
        #     info = (tipo, self.get_id(), 0)
        #     #enviamos nuestro mensaje a los vecinos
        #     self.canales[1].envia(info, self.vecinos)
        tipo = 'go'
        info = (tipo, -1, 0, 'si')
        self.canales[1].envia(info, self.vecinos)
        # else:  #los demas no tienen padre jaja xd
        #     self.padre = None

        # #aqui es donde ocurre la magia
        # while True:
        while True:
            #tipo, candidato, valor = yield self.canales[0].get()  #esperamos el mensaje
            tipo, n, candidato, confir = yield  self.canales[0].get()

        #   verificamos si es go o back
        #   if tipo == 'go':
            if tipo == 'go':
        #         #si no tiene padre xd
        #         if self.padre is None:
                if self.padre is None:
        #           #hacemos del candidato la padre
        #           self.padre = candidato
                    self.padre= candidato
        #           self.msg_esperados = len(self.vecinos) - 1
                    self.msg_esperados = len(self.vecinos)-1
                    self.nivel = n+1

        #           si no hay mensajes esperados
        #           if self.msg_esperados == 0:
                    if self.msg_esperados == 0:
        #               tipo = 'back'
                        tipo = 'back'

        #               info = (tipo, self.get_id(), self.get_id())
                        info = (tipo, n+1, self.get_id(), 'si')

        #               #enviamos la confirmacion al padre
        #               self.canales[1].envia(info,[candidato])  #porque tiene que verlo como lista
                        self.canales[1].envia(info, [candidato])

        #           #si no le seguimos envianos a nuestro vecinos
        #           else:
                    else:
        #               tipo = 'go'
                        tipo = 'go'
        #               info = (tipo, self.get_id(), None)
                        info = (tipo, n+1, self.get_id(), None)

        #               destinos = []
                        destinos = []
        #               for i in self.vecinos:
                        for i in self.vecinos:
        #                   if i != candidato:
                            if i != candidato:
        #                       destinos.append(i)
                                destinos.append(i)
        #               self.canales[1].envia(info, destinos)
                        self.canales[1].envia(info, destinos)
                        

                #si ya tiene padre y hay un nivel mas
                elif self.nivel > n+1:
                    self.padre = candidato
                    self.nivel = n+1
                    self.msg_esperados = len(self.vecinos)-1
                    if self.msg_esperados == 0:
                        tipo = 'back'
                        info = (tipo, self.nivel, self.get_id(),'si')

                    else:
                        tipo = 'go'
        #               info = (tipo, self.get_id(), None)
                        info = (tipo, n+1, None, None)

        #               destinos = []
                        destinos = []
        #               for i in self.vecinos:
                        for i in self.vecinos:
        #                   if i != candidato:
                            if i != candidato:
        #                       destinos.append(i)
                                destinos.append(i)
        #               self.canales[1].envia(info, destinos)
                        self.canales[1].envia(info, destinos)

        #       else:
                else: 
        #           tipo = 'back'
                    tipo = 'back'
        #           info = (tipo, self.get_id(), None)
                    info = (tipo, n+1, self.get_id() ,'nel')
        #           self.canales[1].envia(info, [candidato])
                    self.canales[1].envia(info, [candidato])

        
        #     #si es de tipo back
        #     elif tipo == 'back':
            elif tipo == 'back':
                if n == self.nivel+1:
                    if confir == 'si':
                        self.hijos.append(candidato)
                    if self.msg_esperados == 0:
                        if self.padre != self.id_nodo:
                            tipo = 'back'
                            info = (tipo, self.nivel, candidato, 'si')

        #         self.msg_esperados = self.msg_esperados - 1

        #         #si ya no tiene mensajes esperados
        #         if self.msg_esperados == 0:
        #             if self.padre != self.get_id():
        #                 tipo = 'back'
        #                 info = (tipo, self.get_id(), self.get_id())
        #                 self.canales[1].envia(info, [self.padre])

        #         if valor is not None:
        #             self.hijos.append(candidato)
