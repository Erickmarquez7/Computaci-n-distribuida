## Entendiendo el uso de generadores en python
# En una funcion normal, nos va a regresar completamente la estrcutura que le pidamos
def doble(limite):
    '''Nos da el doble de una lista con el limite marcado'''
    res = []
    cont = 1
    while cont < limite:
        res.append(cont*2)
        cont=cont+1
    #nos devuelve la lista entera
    return res
    
print(doble(5))

#Pero yield nos devolverá uno por uno, de una estrucutra iterable

def doble_yield(limite):
    cont = 1
    while cont < limite:
        yield cont*2
        cont += 1

#guardamos la estrcutura en una variable
est_gen = doble_yield(5)
#y con next obtenemos el valor
print(next(est_gen))

print('Mas codigo...')

#Volvemos a obtener el siguiente
print(next(est_gen))
print(next(est_gen))
print(next(est_gen))
#print(next(est_gen)). En caso de que se acabe el iterable nos mandará una excepcion
#print(next(est_gen))

print('Otros ejemplos')

#otro ejemplo
def funcion(*args):
    for valor in args:
        return valor


print(funcion(1,2,3,4))#solo imprime el primero

#for valor in funcion(1,2,3,4,5):
#    print(valor) #error, pues int no es iterable

#Así que usamos yield para que los guarde en una edd iterable y los regrese
def generator(*args):
    for valor in args:
        yield valor

#print(funcion(1,2,3,4))
for valor in generator(1,2,3,4): #aqui ya me lo puede 'iterar'
    print(valor)
