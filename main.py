import datetime
from Project1 import Recurso,Planificador,Evento
    

planificador = Planificador()

nuevo_evento = Evento(
    nombre = "Observacion de jupiter",
    inicio = datetime.datetime(10,8,2,5),
    fin = datetime.datetime(10,9,7,6),
    recursos = ["Telescopio Principal","Operador del telescopio principal"]
)

planificador.guardar_eventos(nuevo_evento)
planificador.mostrar_eventos()