lista = [1,2,8,4,9]
c = 3

def Buscar(lista):
    minimo = min(lista)
    maximo = lista[len(lista)-1]
    band = 1
    dis = maximo - minimo
    for n in lista:
        if (maximo - n < dis) and n > maximo:
            lista.remove(maximo)
            band = False
            break
    if band == False:
        print(lista)
        respuesta = Buscar(lista)
    else:
        return dis
    return respuesta

print(Buscar(lista))
        
