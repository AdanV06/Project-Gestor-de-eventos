#Creando clase recurso:
import datetime 
import json 


with open("Project Pro 1/Recursos.json") as file: #Abriendo el json que contiene los recursos 
    data = json.loads(file.read()) #Guardando en la variable data los lementos de json como diccionarios

class Recurso(): #Definiendo la clase recurso
    def __init__(self, nombre,tipo,disponibilidad,cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.disponibilidad = disponibilidad
        self.cantidad = cantidad

    def __repr__(self):
        return f"Recurso({self.nombre},{self.tipo})" 

class Evento: #Definiendo la clase Evento
    def __init__(self,nombre,inicio,fin,recursos):
        self.nombre = nombre
        self.inicio = inicio
        self.fin = fin
        self.recursos = recursos
    def conv_dicc(self):# Funcion para convertir a diccionario el evento
        return {
            "nombre": self.nombre,
            "inicio": self.inicio.strftime("%m-%d %H:%M"),
            "fin": self.fin.strftime("%m-%d %H:%M"),
            "recursos": self.recursos
        }
#Definiendo clase planificadoe
class Planificador:
    def __init__(self,archivo_eventos="Project Pro 1/Eventos.json"):
        self.eventos = [] #Lista de eventos
        self.archivo_eventos = archivo_eventos #Archivo donde se guardaran los eventos
        
        self.mantener_eventos()


    def guardar_eventos(self,evento): #Funcion para guardar eventos
        self.eventos.append(evento)#Agregando el evento a la lista de eventos
        lista_eventos = [e.conv_dicc() for e in self.eventos] #Convirtiendo en diccionario los eventos y agregandolos a una nueva lista de eventos
        with open("Project Pro 1/Eventos.json", "w") as file: #Abriendo el json donde se guardaran los eventos
            file.write(json.dumps({"eventos": lista_eventos})) #Agregando los eventos que estan en la lista de eventos como diccionarios
            print(f"El evento {evento.nombre} se agrego correctamente")
        return True

    def mantener_eventos(self): #Guardar los elementos existentes antes de anadir nuevos
        try:
            with open(self.archivo_eventos) as file:
                data = json.load(file)
                for e in data.get("eventos",[]): #Iterando en cada elemento anterior del json
                    inicio = datetime.datetime.strptime(e["inicio"], "%m-%d %H:%M") 
                    fin = datetime.datetime.strptime(e["fin"], "%m-%d %H:%M")
                    eventos_anteriores = Evento(e["nombre"],inicio,fin,e["recursos"]) #Creando un elemento con las mismas propiedades de cada elemento del json
                    self.eventos.append(eventos_anteriores) #Agregando los eventos anteriores a la lista de eventos
        except FileNotFoundError: #Si no se encuentra el archivo json crear uno nuevo
            print("No se encontro el archivo, se creara uno nuevo") 
            self.eventos = []


    def mostrar_eventos(self): #Mostrar eventos ya guardados
        if not self.eventos: #Si no hay eventos decir que no se encuentran todavia
            print("No hay elementos registrados todavia")
            return
        print(f"Se tienen registrado {len(self.eventos)} eventos: ") #Mostrando los eventos registrados
        for i,e in enumerate(self.eventos,start=1): #Iterando en cada evento y asigandole un indice a cada uno a partir de 1
            print(f"{i}.{e.nombre}") #Imprimir el indice asignado al evento y segido el nombre
            print(f"Inicio: {e.inicio.strftime('%m-%d %H:%M')}") #Imprimiendo cada unas de las propiedades del evento
            print(f"Fin: {e.fin.strftime('%m-%d %H:%M')}")
            print(f"Recursos: {',' .join(e.recursos)}")

            






