import datetime
from Project1 import Recurso,Planificador,Evento

def mostrar_menu():
    print("Que desea hacer: ")
    print("1- Agregar evento")
    print("2- Mostrar eventos")
    print("3- Salir")
    return input()


band = True
planificador = Planificador()

while(band == True):
    resp = mostrar_menu()
    if resp == '1':
        name = input("Diga el nombre del evento: ")
        fecha_str = input("Diga la fecha de inicio de la forma ano-mes-dia-hora-minutos: ")
        fecha_int = [int(x) for x in fecha_str.split("-")]
        inicio = datetime.datetime(*fecha_int)
        fecha_str = input("Diga la fecha del fin de la forma ano-mes-dia-hora-minutos: ")
        fecha_int = [int(x) for x in fecha_str.split("-")]
        fin = datetime.datetime(*fecha_int)
        recursos = []
        for i in range(0,2):
            recursos.append(input("Diga un recursos:"))
        
        nuevo_evento = Evento(
        nombre = name,
        inicio = inicio,
        fin = fin,
        recursos = recursos
        )

        planificador.agregar_evento(nuevo_evento)

        resp = input("Desea hacer algo mas (s/n): ")
        if resp == 's':
            pass
        if resp == 'n':
            band == False
    if resp == '2':
        planificador.mostrar_eventos()
        resp = input("Desea hacer algo mas (s/n): ")
        if resp == 's':
            pass
        if resp == 'n':
            band == False
    if resp == '3':
        band = False


