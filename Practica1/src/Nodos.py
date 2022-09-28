#Integrantes:
#Bernal Márquez Erick           317042522
#Deloya Andrade Ana valeria     317277582
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
        Nodo.__init__(self, id_nodo, vecinos, canales)
        self.madre = None
        self.hijas = []
        #raise NotImplementedError('Constructor de NodoArbolGenerador no implementado')

    def genera_arbol(self, env: simpy.Store):
        """Algoritmo para producir el arbol generador."""
        #El if es para tener al nodo con id 0, es decir, el nodo raiz
        if self.get_id() == 0:
            self.madre = self.get_id()

            #mensajes esperados
            self.esperados = len(self.vecinos)

            tipo = 'go'
            info = (tipo, self.get_id(), 0)
            #enviamos nuestro mensaje a los vecinos
            self.canales[1].envia(info, self.vecinos)

        else:  #los demas no tienen madre jaja xd
            self.madre = None

        #aqui es donde ocurre la magia
        while True:
            tipo, candidato, valor = yield self.canales[0].get()  #esperamos el mensaje

            #verificamos si es go o back
            if tipo == 'go':
                #si no tiene madre xd
                if self.madre is None:
                    #hacemos del candidato la madre
                    self.madre = candidato
                    self.esperados = len(self.vecinos) - 1

                    #si no hay mensajes esperados
                    if self.esperados == 0:
                        tipo = 'back'
                        info = (tipo, self.get_id(), self.get_id())
                        #enviamos la confirmacion al padre
                        self.canales[1].envia(info,[candidato])  #porque tiene que verlo como lista

                    #si no le seguimos envianos a nuestro vecinos
                    else:
                        tipo = 'go'
                        info = (tipo, self.get_id(), None)
                        destinos = []
                        for i in self.vecinos:
                            if i != candidato:
                                destinos.append(i)
                        self.canales[1].envia(info, destinos)

                else:
                    tipo = 'back'
                    info = (tipo, self.get_id(), None)
                    self.canales[1].envia(info, [candidato])

            #si es de tipo back
            elif tipo == 'back':
                self.esperados = self.esperados - 1

                #si ya no tiene mensajes esperados
                if self.esperados == 0:
                    if self.madre != self.get_id():
                        tipo = 'back'
                        info = (tipo, self.get_id(), self.get_id())
                        self.canales[1].envia(info, [self.madre])

                if valor is not None:
                    self.hijas.append(candidato)

        #raise NotImplementedError('GeneraArbol de NodoArbolGenerador no implementado')

class NodoBroadcast(Nodo):
    """Nodo que implementa el algoritmo del ejercicio 3.

    Atributos adicionales:
    mensaje -- cadena con el mensaje que se distribuye
    """
    def __init__(self, id_nodo: int, vecinos: list, canales: tuple):
        """Constructor para el nodo broadcast."""
        Nodo.__init__(self, id_nodo, vecinos, canales)
        self.mensaje = ''


    def broadcast(self, env: simpy.Store):
        """Algoritmo de broadcast."""
        #El if es para tener al nodo con id 0, es decir, el nodo raiz
        if self.get_id() == 0:
            self.mensaje = 'MENSAJE BROADCAST'
            self.canales[1].envia(self.mensaje, self.vecinos)

        #los que no son la raiz, no tienen mensaje
        else:
            self.mensaje = None

        while True:
            self.mensaje = yield self.canales[0].get()

            #el mensaje es enviado a los vecinos
            if len(self.vecinos) > 0:
                self.canales[1].envia(self.mensaje, self.vecinos)
                yield env.timeout(1) #si no c cicla

