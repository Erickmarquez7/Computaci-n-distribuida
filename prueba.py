import simpy

def carro(env):
    while True:
        print('Empieza a estacionarse al %d' % env.now)
        duracion_estacionado = 5
        yield env.timeout(duracion_estacionado)

        print('Empieza a conducir al %d' % env.now)
        duracion_viaje = 2
        yield env.timeout(duracion_viaje)

env = simpy.Environment()
env .process(carro(env))
env.run(until=20)
env.run(until=40)
