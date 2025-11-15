import json 
import datetime

ruta_eventos = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Eventos.json"
ruta_recursos = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Recursos.json"

def leer_json(ruta):
    with open(ruta,"r") as elementos:
        return json.load(elementos)

class Recurso:
    def __init__(self,nombre,tipo,disponibilidad,cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.disponibilidad = disponibilidad
        self.cantidad = cantidad
    def convertir_dicc(self):
        return {
            "nombre" : self.nombre,
            "tipo" : self.tipo,
            "disponibilidad" : self.disponibilidad,
            "cantidad" : self.cantidad
        }
class Evento:
    def __init__(self,nombre,inicio,fin,recursos):
        self.nombre = nombre
        self.inicio = inicio
        self.fin = fin
        self.recursos = recursos
    def convertir_dicc(self):
        return {
            "nombre" : self.nombre,
            "inicio" : self.inicio.strftime("%Y-%m-%d-%H-%M"),
            "fin" : self.fin.strftime("%Y-%m-%d-%H-%M"),
            "recursos" : self.recursos
        }
class Planificador:
    def __init__(self,ruta_eventos="/home/adan/Adan/Programacion/Projects/Project Pro 1/Eventos.json",ruta_recursos="/home/adan/Adan/Programacion/Projects/Project Pro 1/Recursos.json"):
        self.eventos = []
        self.json_eventos = ruta_eventos
        self.json_recursos = ruta_recursos
        self.recursos = []
        self.mantener_eventos()
        self.cargar_recursos()
    
    def mantener_eventos(self):
        eventos_json = leer_json(self.json_eventos)
        for e in eventos_json.get("eventos"):
            inicio = datetime.datetime.strptime(e["inicio"], "%Y-%m-%d-%H-%M") 
            fin = datetime.datetime.strptime(e["fin"], "%Y-%m-%d-%H-%M")
            eventos_anteriores = Evento(e["nombre"], inicio, fin, e["recursos"])
            self.eventos.append(eventos_anteriores)

        

    def cargar_recursos(self):
        recursos_data = leer_json(self.json_recursos)
        #Guardando los recursos en una lista para poder ser iterados
        for r in recursos_data.get("recursos"):
            recurso = Recurso(r["nombre"],r["tipo"],r["disponibilidad"],r["cantidad"])
            self.recursos.append(recurso)


    #Funcion para mantener los eventos en una lista eventos y asi evitar que se borren cuando se sobrescriba     

    #Funcion para actualizar los recursos del json despues de agrgar un evento
    '''def actualizar_recursos(self,evento):
        #Actualizando la cantidad de cada recurso 
        for r in evento.recursos:
            for recur in self.recursos:
                if r[0] == recur.nombre:
                    recur.cantidad -= r[1]
        #Sobrescribienodo el archivo json de recursos con los nuevos cambios
        lista_recursos = [r.convertir_dicc() for r in self.recursos]
        with open(self.json_recursos,"w") as recursos_json:
            recursos_json.write(json.dumps({"recursos" : lista_recursos},indent=4))'''

    def verificar_hora(self,ini_ev,ini_evs,fin_ev,fin_evs):
        band = False
        if (ini_ev<=ini_evs and fin_ev>ini_evs) or (ini_ev>=ini_evs and ini_ev<fin_evs):
            band = True
        return band

    #Funcion para agregar evento al json
    def agregar_evento(self,evento):
        disp= 1000000
        for r in evento.recursos:
            for e in self.eventos:
                for rec in e.recursos:
                    if r[0] == rec[0]:
                        if self.verificar_hora(evento.inicio,e.inicio,evento.fin,e.fin):
                            for j in self.recursos:
                                if j.nombre == r[0]:
                                    if j.cantidad == 1:
                                        print(f"El recurso {j.nombre} no esta disponible en ese horario")
                                        return False
                                    else:disp = j.cantidad
                                     
                            
                            disp -= rec[1]
                            if disp < r[1]:
                                print(f"No hay suficientes {r[0]} disponibles en ese horario, solo se tienen {disp}")
                                return False

        self.eventos.append(evento)
        lista_eventos = [e.convertir_dicc() for e in self.eventos]
        with open(self.json_eventos,"w") as eventos_json:
            eventos_json.write(json.dumps({"eventos" : lista_eventos}))
            print("El evento se agrego correctamente")
        return True

evento1 = Evento(
    nombre = "Observacion 3",
    inicio = datetime.datetime(2024,10,4,11,00),
    fin = datetime.datetime(2024,10,4,12,00),
    recursos = [("Computadoras",15)]
)

operaciones = Planificador()
operaciones.agregar_evento(evento1)