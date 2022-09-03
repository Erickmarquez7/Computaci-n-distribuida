## Entiendo el uso de generadores en python
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
