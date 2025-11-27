import json 
import datetime

#Ruta de los archivos Json
ruta_eventos = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Eventos.json"
ruta_recursos = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Recursos.json"

#Funcion para leer los json
def leer_json(ruta):
    with open(ruta,"r") as elementos:
        return json.load(elementos)

#Clase recurso
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

#Clase evento
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

#Clase planificador donde contiene todas las funciones
class Planificador:
    def __init__(self,ruta_eventos="/home/adan/Adan/Programacion/Projects/Project Pro 1/Eventos.json",ruta_recursos="/home/adan/Adan/Programacion/Projects/Project Pro 1/Recursos.json"):
        self.eventos = []
        self.json_eventos = ruta_eventos
        self.json_recursos = ruta_recursos
        self.recursos = []
        self.cargar_eventos()
        self.cargar_recursos()
    
    #Guardar los eventos del json en una lista
    def cargar_eventos(self):
        eventos_json = leer_json(self.json_eventos) #Leer el json y guardar su contenido en la variable eventos_json
        for e in eventos_json.get("eventos"): 
            inicio = datetime.datetime.strptime(e["inicio"], "%Y-%m-%d-%H-%M") 
            fin = datetime.datetime.strptime(e["fin"], "%Y-%m-%d-%H-%M")
            eventos_anteriores = Evento(e["nombre"], inicio, fin, e["recursos"])
            self.eventos.append(eventos_anteriores)

    #Guardar los recursos del json en una lista 
    def cargar_recursos(self):
        recursos_data = leer_json(self.json_recursos)
        #Guardando los recursos en una lista para poder ser iterados
        for r in recursos_data.get("recursos"):
            recurso = Recurso(r["nombre"],r["tipo"],r["disponibilidad"],r["cantidad"])
            self.recursos.append(recurso)

    #Verificar si 2 eventos estan en el mismo horario
    def verificar_hora(self,ini_ev,ini_evs,fin_ev,fin_evs):
        band = False
        if (ini_ev<=ini_evs and fin_ev>ini_evs) or (ini_ev>=ini_evs and ini_ev<fin_evs):
            band = True
        return band

    #Funcion para agregar evento al json
    def agregar_evento(self,evento):
        for r in evento.recursos:
            for rec in self.recursos:
                if r[0]==rec.nombre:
                    if r[1] > rec.cantidad:
                        
                        return f"No contamos con esa cantidad de {r[0]}, solo contamos con {rec.cantidad}"
        disp= 1000000
        for r in evento.recursos:
            for e in self.eventos:
                for rec in e.recursos:
                    if r[0] == rec[0]:
                        if self.verificar_hora(evento.inicio,e.inicio,evento.fin,e.fin):
                            for j in self.recursos:
                                if j.nombre == r[0]:
                                    if j.cantidad == 1:
                                        return f"El recurso {j.nombre} no esta disponible en ese horario"
                                    else:disp = j.cantidad
                                     
                            
                            disp -= rec[1]
                            if disp < r[1]:
                                return f"No hay suficientes {r[0]} disponibles en ese horario, solo hay {disp} disponibles"

        self.eventos.append(evento)
        lista_eventos = [e.convertir_dicc() for e in self.eventos]
        with open(self.json_eventos,"w") as eventos_json:
            eventos_json.write(json.dumps({"eventos" : lista_eventos}))
        return "El evento se agrego correctamente"



operaciones = Planificador()
