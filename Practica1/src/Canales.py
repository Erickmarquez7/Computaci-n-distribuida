import simpy


class Canal():
    """Clase Abstracta que modela el comportamiento que cualquier canal debe 
    tomar."""

    def __init__(self, env: simpy.Environment, capacidad=simpy.core.Infinity):
        """Constructor de la clase."""
        self.env = env
        self.capacidad = capacidad
        self.canales = []

    def envia(self, mensaje, vecinos):
        """Metodo abstracto.
        
        Envia un mensaje a los canales de entrada de los vecinos.
        """
        pass

    def crea_canal_de_entrada(self) -> simpy.Store:
        """Creamos un objeto Store en el un nodo recibirá los mensajes."""
        canal = simpy.Store(self.env, capacity=self.capacidad)
        self.canales.append(canal)
        return canal

    def get_canales(self) -> list:
        """Regresa la lista con los canales."""
        return self.canales


class CanalGeneral(Canal):
    """Implementacion de un canal para el caso general."""

    def envia(self, mensaje, vecinos):
        """Envia un mensaje a los canales de entrada de los vecinos."""
        #revisamos si hay canales
        if not self.canales:
            raise RuntimeError('No hay canales.')
        
        #para cada id en vecinos mandamos mensaje a canales[id]; [0,1,2,3,...id_n]
        eventos = []
        for j in vecinos:#para cada vecinos que le queramos enviar mensaje
            eventos.append(self.canales[j].put(mensaje))#le ponemos el mensaje en el buzon
        return self.env.all_of(eventos)#le enviamos dichos mensajes a traves del evento
        #es como hacer procces pero con una lista de eventos


