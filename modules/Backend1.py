import json 
import datetime

#Ruta de los archivos Json
ruta_eventos = "datas/Eventos.json"
ruta_recursos = "datas/Recursos.json"

#Funcion para comparar
def comparar(a,b):
    if a.inicio > b.inicio:
        return True
    return False

#Funcion para ordenar los eventos por fecha
def ordenar(lista):
    n = len(lista)

    for i in range(n):
        for j in range(n-i-1):
            if comparar(lista[j],lista[j+1]):
                lista[j],lista[j+1] = lista[j+1],lista[j]

    return lista 

#Funcion para verficar la cantidad de recursos que hay disponibles
def verificar_cantidad(recursos,evento_recursos):
    for r in evento_recursos:
        for rec in recursos:
            if r[0]==rec.nombre:
                if r[1] > rec.cantidad: return f"No contamos con esa cantidad de {r[0]}, solo contamos con {rec.cantidad}"

#Funcion para verificar la disponibilidad de los recursos
def verificar_recurso(recurso,recursos,rec):
    disp= 1000000
    for j in recursos:
            if j.nombre == recurso:
                print(f"Desde la funcion: {recurso}")
                if j.cantidad == 1:
                    return f"El recurso {j.nombre} no esta disponible en ese horario"
                else:disp = j.cantidad
                    
        
    disp -= rec[1]
    if disp < rec[1]:
        return f"No hay suficientes {r[0]} disponibles en ese horario, solo hay {disp} disponibles"

#Funcion para verificar si 2 eventos estan en el mismo horario
def verificar_hora(ini_ev,ini_evs,fin_ev,fin_evs):
    band = False
    if (ini_ev<=ini_evs and fin_ev>ini_evs) or (ini_ev>=ini_evs and ini_ev<fin_evs):
        band = True
    return band
    

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
    def __init__(self,ruta_eventos="datas/Eventos.json",ruta_recursos="datas/Recursos.json"):
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

    #Funcion para verificar los complementarios
    def verificar_complementarios(self,recursos_herramienta,recurso_sala,recursos_personal):
        recursos_json = leer_json("datas/Recursos.json")
        band_sala = False
        band_rec = False

        #Verificar los complementarios para las salas
        for i in range(len(recursos_json["recursos"])):
            if recurso_sala[0][0] == recursos_json["recursos"][i]["nombre"]:
                comp = recursos_json["recursos"][i]["complementario"]
                if comp == "NULL":
                    band_sala = True
                else:
                    if comp[0] in recursos_personal:
                        band_sala = True
                    else:
                        if recurso_sala[0][0] == "Planetario":
                            return f"En el {recurso_sala[0][0]} debe estar Cleo Abram la encargada de esta sala"
                        if recurso_sala[0][0] == "Sala de optica":
                            return f"En la {recurso_sala[0][0]} debe estar la especialista Henrietta Leavitt"

        #Verificar los complementarios para los recursos herramienta
        for rec_event in recursos_herramienta:
            for i in range(len(recursos_json["recursos"])):
                if rec_event[0] == recursos_json["recursos"][i]["nombre"]:
                    rec_comp = recursos_json["recursos"][i]["complementario"]
                    if rec_comp == "NULL":
                        band_rec = True
                    else:                         
                        for n in rec_comp:
                            if (n in recursos_personal) or (n in recurso_sala):
                                band_rec = True
                                break
                            else:
                                band_rec = False
                        if band_rec == False:
                            if (rec_event[0] == "Gafas virtuales" or rec_event[0] == "Portatiles" or rec_event[0] == "Telescopio"):
                                return f"El recurso {rec_event[0]} solo puede ser usado en la sala de conferencias o en el planetario"

                            if (rec_event[0] == "Telescopio de agujeros negros"):
                                return f"El {rec_event[0]} solo puede ser usado por especialistas de agujeros negros"

                            if (rec_event[0] == "Telescopio Lunar"):
                                return f"El {rec_event[0]} solo puede ser utilizado por especialistas en astros"

                            if (rec_event[0] == "Telescopio de Galaxias"):
                                return f"El {rec_event[0]} solo puede ser utilizado por especialistas de galaxias"

                            if (rec_event[0] == "Telescopio solar"):
                                return f"El {rec_event[0]} solo puede ser utilizado por especialistas del sol"
                                
                            if (rec_event[0] == "Polarimetro" or rec_event[0] == "Espectrometro"):
                                return f"El {rec_event[0]} solo puede ser utilizado por la especialista en optica Henrietta Leavitt"

        if band_sala == True and band_rec == True:
            return True
    
    #Funcion para verficar excluyentes
    def verificar_excluyentes(self,recursos_personal):
        recursos_json = leer_json("datas/Recursos.json")
        band = True

        for rec in recursos_personal:
            for i in range(len(recursos_json["recursos"])):
                if rec[0] == recursos_json["recursos"][i]["nombre"]:
                    rec_ex = recursos_json["recursos"][i]["excluyentes"]
                    if rec_ex == "NULL":
                        band = True
                    else:
                        for n in rec_ex:
                            if n in recursos_personal:
                                band = False
                                break
                        if band == False:
                            if (rec[0] == "Vera Rubin" or rec[0] == "Edwin Huble"):
                                return "Los especialistas en galaxias no pueden trabajar junto a los especialistas en el sol"
                            if (rec[0] == "Margaret Burbidge"):
                                return "Los especialistas en la luna no pueden trabajar con los especialistas en agujeros negros"
        
        if band == True:
            return True

    #Funcion para agregar evento al json
    def agregar_evento(self,evento):
        result = verificar_cantidad(self.recursos,evento.recursos)
        if result != None:
            return result
        disp= 1000000
        for r in evento.recursos:
            for e in self.eventos:
                for rec in e.recursos:
                    if r[0] == rec[0]:
                        if verificar_hora(evento.inicio,e.inicio,evento.fin,e.fin):
                            print(f"Desde el otro: {r[0]}")
                            result = verificar_recurso(r[0],self.recursos,rec)
                            if result != None :
                                return result

        self.eventos.append(evento)
        lista_eventos = [e.convertir_dicc() for e in self.eventos]
        with open(self.json_eventos,"w") as eventos_json:
            eventos_json.write(json.dumps({"eventos" : lista_eventos}))
        return "El evento se agrego correctamente"

    #Funcion para agregar el evento en el mejor horario
    def buscar(self,evento,horas):
        if len(self.eventos) == 0:
            self.agregar_evento(evento)
            return "El evento se agrego correctamente"
        eventos_ordenados = ordenar(self.eventos)
        if len(self.eventos) == 1:
            a = self.agregar_evento(evento)
            if a != "El evento se agrego correctamente":
                evento.inicio = self.eventos[0].fin
                evento.fin = evento.inicio + datetime.timedelta(hours=horas)
                return self.agregar_evento(evento)
            else:
                return "El evento se agrego correctamente"
        for i in range(len(self.eventos)+1):
            b = self.agregar_evento(evento)
            if b != "El evento se agrego correctamente":
                evento.inicio = self.eventos[i].fin
                evento.fin = evento.inicio + datetime.timedelta(hours=horas)
            else:
                return "El evento se agrego correctamente"

operaciones = Planificador()
