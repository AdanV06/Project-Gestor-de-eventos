from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
import datetime
import json
import calendar
from Estilo import kv
from Imagenes import*
from Backend1 import*

Window.size = (1150,900)

Builder.load_string(kv)


class evento:
    recursos_persona = []
    recursos_herramienta = []
    recursos_sala = []
    datos = {}
    cantidad = []


class informacion(Label):
    def __init__(self,inf):
        super().__init__()
        self.markup=True
        self.text=inf
        self.font_size = 20       
        self.text_size=(460,170)
        self.size_hint=(None,None)
        self.valign='top'
        self.size=(480,202)

class informacion_personaje(BoxLayout):
    def __init__(self,imagen,inf,nombre):
        super().__init__()
        self.imagen = Image(source=imagen,size_hint=(None,None),size=(180,180), pos=(260,195))
        self.informacion = informacion(inf=inf)
        self.spacing = 2
        self.nombre = nombre
        print(self.nombre)

        self.espacio = filas(orientacion="horizontal",tamano=(30,0),espacio=2)
        self.img = FloatLayout(size_hint=(None,None),size=(180,180),pos_hint={"center_x": 0.5,"center_y": 0.5})
        self.img.add_widget(self.imagen)
        
        self.add_widget(self.espacio)
        self.add_widget(self.img)
        self.add_widget(self.informacion)

class nombres(Label):
    def __init__(self,texto):
        super().__init__()
        self.text = texto

class TiposPersonal(Label):
     def __init__(self,texto):
        super().__init__()
        self.text = texto

class Contenedor_Recursos(BoxLayout):
    def __init__(self):
        super().__init__()

class filas(BoxLayout):
    def __init__(self,orientacion,tamano,espacio):
        super().__init__()
        self.orientation = orientacion
        self.size = tamano
        self.spacing = espacio

class menu(BoxLayout):
    def __init__(self):
        super().__init__()

class BotonHerramientas(ButtonBehavior,Image):
    def __init__(self):
        super().__init__()
        self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Boton_Recurso.png"
        self.size_hint = (None,None)
        self.size = (150,120)
        self.pos = (790,240)
        self.opciones_seleccionadas = []


    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.mostrar_herramintas(touch)

    def mostrar_herramintas(self,touch):
        self.menu_H = menu()
        self.popup_H = Popup(title="Herramientas",content=self.menu_H,size_hint=(None, None),size=(750, 840),background_color=(0.2,0,0.6,0.9))
        self.popup_H.open()

        self.contenedor = Contenedor_Recursos()
        self.grid = GridLayout(cols=5,spacing=40)
        self.row4 =FloatLayout(size_hint=(None,None),size=(725,140),pos=self.pos)

        opciones = [("Polarimetro",objeto2,obj2),("Camara estelar",objeto3,obj3),("Espectrometro",objeto4,obj4),("Telescopio de Galaxias",objeto5,obj5),("Portatiles",objeto6,obj6),("Telescopio de agujeros negros",objeto7,obj7),("Gafas virtuales",objeto8,obj8),("Telescopio lunar",objeto9,obj9),
        ("Telescopio de Rayos Gama",objeto10,obj10),("Telescopio solar",objeto11,obj11),("Radio Telescopio",objeto12,obj12),("Telescopio",objeto13,obj13)]

        self.all_opciones = []
        for opcion,img,info in opciones:
            btn = OpcionHerramienta(
            opcion=opcion,
            size_hint=(None, None),
            size=(80, 80),
            allow_stretch=True,
            source = img,
            state='down' if opcion in self.opciones_seleccionadas else 'normal',
            img_press= "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Guardar_Touch.png",
            inf = info
            )
            self.all_opciones.append(btn)
            self.grid.add_widget(btn)

        self.fila = informacion_personaje(imagen=objeto1,inf="",nombre="")
        

        self.boton_aceptar = botonAceptar(all_opciones=self.all_opciones,popup=self.popup_H,Id="Herramienta")
        self.boton_salir = botonSalir(popup=self.popup_H)
        self.row4.add_widget(self.boton_aceptar)
        self.row4.add_widget(self.boton_salir)
        self.contenedor.add_widget(self.grid)
        self.contenedor.add_widget(self.fila)
        self.contenedor.add_widget(self.row4)
        self.menu_H.add_widget(self.contenedor)

class OpcionHerramienta(ButtonBehavior, Image,FloatLayout):
    def __init__(self, opcion,img_press,inf, **kwargs):
        super().__init__(**kwargs)
        self.opcion = opcion
        self.seleccionado = False
        self.img = self.source
        self.size_hint = (None,None)
        self.size = (100,100)
        self.img_press = img_press
        self.inf = inf
 
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            apps = App.get_running_app()
            apps.contenedor.body.nueva_ventana.recursos_herramienta.fila.imagen.source = self.img
            apps.contenedor.body.nueva_ventana.recursos_herramienta.fila.informacion.text = self.inf
            apps.contenedor.body.nueva_ventana.recursos_herramienta.fila.nombre = self.opcion
            print(apps.contenedor.body.nueva_ventana.recursos_herramienta.fila.nombre)
            if self.state=="normal":
                self.state = 'down'
                if self.opcion == "Gafas virtuales" or self.opcion == "Portatiles" or self.opcion == "Telescopio":
                    self.contenedor_cant = vent_cant()
                    self.cant = TextInput(size_hint=(None,None),size=(200,30),hint_text="Cantidad",cursor_color=(1,0,0,1),background_color=(0,0,0,0.4),font_size=17,pos_hint={"center_x":0.5,"top":1},foreground_color=(1,1,1,1))
                    self.popup_cant = Popup(title=f"Diga cantidad de {self.opcion}",content=self.contenedor_cant,size_hint=(None,None),size=(250,150),background_color=(0.4,0,0.9,1))
                    self.btn_aceptar = Button(size_hint=(None,None),size=(100,30),text="Aceptar",pos_hint={"center_x":0.50,"center_y":0.1},padding=(0,100),background_color=(0.6,0,1,0.7))

                    self.btn_aceptar.bind(on_press=self.guardar)
                    
                    self.contenedor_cant.add_widget(self.cant)
                    self.contenedor_cant.add_widget(self.btn_aceptar)
                    

                    self.popup_cant.open()
                '''elif self.opcion == "Portatiles":
                    self.contenedor_cant = vent_cant()
                    self.cant = TextInput(size_hint=(None,None),size=(200,30),hint_text="Cantidad",cursor_color=(1,0,0,1),background_color=(0,0,0,0.4),font_size=17,pos_hint={"center_x":0.5,"top":1},foreground_color=(1,1,1,1))
                    self.popup_cant = Popup(title=f"Diga cantidad de {self.opcion}",content=self.contenedor_cant,size_hint=(None,None),size=(250,150),background_color=(0.4,0,0.9,1))
                    self.btn_aceptar = Button(size_hint=(None,None),size=(100,30),text="Aceptar",pos_hint={"center_x":0.50,"center_y":0.1},padding=(0,100),background_color=(0.6,0,1,0.7))

                    self.contenedor_cant.add_widget(self.cant)
                    self.contenedor_cant.add_widget(self.btn_aceptar)

                    self.popup_cant.open()'''
            
        
            else: 
                self.state = 'normal'
                if self.opcion == 'Gafas virtuales':
                    self.remove_widget(self.cant)

            self.on_press()
    def guardar(self,instance):

        try:
            evento.cantidad.append(int(self.cant.text))

        except Exception as e:
            print("Cantidad incorrecta")

        else:
            print("Se agrego correctamete")
            print(evento.cantidad)
            self.popup_cant.dismiss()
                

        
    def on_press(self):
        self.seleccionado = not self.seleccionado
        if self.seleccionado:
            self.source = self.img_press
        else:
            self.source = self.img  # Imagen cuando no está seleccionado
        
class vent_cant(BoxLayout):
    def __init__(self):
        super().__init__()
        self.size_hint=(None,None)
        self.size=(220,85)
        self.orientation="vertical"
        self.spacing=20
        


class BotonPersonal(ButtonBehavior,Image):
        def __init__(self):
            super().__init__()
            self.text= "Personal"
            self.size_hint = (None,None)
            self.size = (150,120)
            self.font_size = 23
            self.pos = (545,240)
            self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Boton_Persona.png"

        def on_touch_down(self,touch):
            if self.collide_point(*touch.pos):
                self.mostrar_menu(touch)
        
        def mostrar_menu(self,touch):
            self.menu = menu()
            self.popup = Popup(title='Cientificos del centro',content=self.menu,size_hint=(None, None),size=(750, 840),background_color=(0.2,0,0.6,0.9))
            self.popup.open()
            self.opciones_seleccionadas = []

            self.grid = GridLayout(cols=5,spacing=(40,20),rows=5,size_hint=(None,None),size=(300,400))
            self.contenedor = Contenedor_Recursos()
            self.row4 =FloatLayout(size_hint=(None,None),size=(725,140),pos=self.pos)

            opciones = [("Carl Sagan",persona1,inf1),("Vera Rubin",persona2,inf2),("Henrietta Leavitt",persona3,inf3),("Edwin Huble",persona5,inf5),("Claudia Aguilar",persona6,inf6),("Margaret Burbidge",persona8,inf8),("Hans Bethe",persona9,inf9),
            ("Neil Tyson",persona10,inf10),("Stiphen Hawking",persona11,inf11)]

            self.all_opciones = []

            for opcion,img,informacion in opciones:
                btn = OpcionPersonal(
                opcion=opcion,
                size_hint=(None, None),
                size=(80, 80),
                allow_stretch=True,
                source = img,
                state='down' if opcion in self.opciones_seleccionadas else 'normal',
                img_press = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Guardar_Touch.png",
                inf=informacion
                )
                
                self.all_opciones.append(btn)
                self.grid.add_widget(btn)
            
            #Informacion del recurso
            self.fila = informacion_personaje(imagen=persona1,inf="",nombre="")
            
            

            #Creando los botones de accion:
            self.boton_aceptar = botonAceptar(all_opciones=self.all_opciones,popup=self.popup,Id="Persona")
            self.boton_salir = botonSalir(popup=self.popup)
            self.row4.add_widget(self.boton_aceptar)
            self.row4.add_widget(self.boton_salir)
            self.contenedor.add_widget(self.grid)
            self.contenedor.add_widget(self.fila)
            self.contenedor.add_widget(self.row4)

            self.menu.add_widget(self.contenedor)
    
class botonAceptar(ButtonBehavior,Image):
    def __init__(self,all_opciones,popup,Id):
        super().__init__()
        self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003303.png"
        self.size_hint = (None,None)
        self.size = (250,90)
        self.pos = (270,60)
        self.popup = popup
        self.all_opciones = all_opciones
        self.Id = Id 


    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Guardar_Touch.png"
            Clock.schedule_once(lambda dt: self.restaurar_color(touch), 0.15)
            if self.Id == "Persona":
                evento.recursos_persona.clear()
        
                evento.recursos_persona= [(btn.opcion,1) for btn in self.all_opciones if btn.state == 'down']

            if self.Id == "Herramienta":
                i=len(evento.cantidad)#Guardando en i la cantidad de elementos de la lista
                evento.recursos_herramienta.clear()
                evento.recursos_herramienta = [[btn.opcion] for btn in self.all_opciones if btn.state == 'down']
                for n in evento.recursos_herramienta:
                    if n[0]=="Portatiles" or n[0]=="Telescopio" or n[0]=="Gafas virtuales":
                        n.append(evento.cantidad[i-1])#Agregando los elementos de la lista desde la ultima posicion a la primera
                        i-=1#Restandole 1 para poder pasar al antecesor
                    else:
                        n.append(1)
            print(evento.recursos_persona)
            self.popup.dismiss()


    
    def restaurar_color(self,touch):
            self.source = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003303.png"

class botonSalir(ButtonBehavior,Image):
    def __init__(self,popup):
        super().__init__()
        self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003303.png"
        self.size_hint = (None,None)
        self.size = (250,90)
        self.pos = (620,60)
        self.popup = popup

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Guardar_Touch.png"
            Clock.schedule_once(lambda dt: self.restaurar_color(touch), 0.15)
            self.popup.dismiss()

    def restaurar_color(self,touch):
            self.source = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003303.png"

class OpcionPersonal(ButtonBehavior, Image, BoxLayout):
    def __init__(self, opcion,img_press,inf, **kwargs):
        super().__init__(**kwargs)
        self.opcion = opcion
        self.seleccionado = False
        self.img = self.source
        self.size_hint = (None,None)
        self.size = (100,100)
        self.img_press = img_press
        self.inf = inf
 
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            apps = App.get_running_app()
            apps.contenedor.body.nueva_ventana.recursos_personal.fila.imagen.source = self.img
            apps.contenedor.body.nueva_ventana.recursos_personal.fila.informacion.text = self.inf
            if self.state=="normal":
                self.state = 'down'

            else: 
                self.state = 'normal'
            self.on_press()
        
    def on_press(self):
        self.seleccionado = not self.seleccionado
        if self.seleccionado:
            self.source = self.img_press
        else:
            self.source = self.img  # Imagen cuando no está seleccionado

class ButtonGuardar(ButtonBehavior,Image):
    def __init__(self,input_nombre,year_inicio,month_inicio,day_inicio,hora_inicio,min_inicio,input_sala,year_fin,month_fin,day_fin,hora_fin,min_fin):
        super().__init__()
        self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003303.png"
        self.size_hint = (None,None)
        self.size = (190,80)
        self.pos = (510,120)
        self.input_nombre = input_nombre
        self.year_inicio = year_inicio
        self.year_fin = year_fin
        self.month_inicio = month_inicio
        self.month_fin = month_fin
        self.day_inicio = day_inicio
        self.day_fin = day_fin
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.min_inicio = min_inicio
        self.min_fin = min_fin
        self.input_sala = input_sala

        print(self.input_sala.text)
    def mostrar_error(self,error):
        self.mensaje = error
        self.error = Label(text=self.mensaje,size_hint=(None,None),size=(250,140),pos_hint={"center_x":0.3,"center_y":0},text_size=(200,140),valign='top')
        self.popup_error = Popup(title='Error',content=self.error,size_hint=(None, None),size=(250, 140),background_color=(0.2,0,0.6,0.9))
        self.popup_error.open()

        
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Guardar_Touch.png"
            Clock.schedule_once(lambda dt: self.restaurar_color(touch), 0.15)
        
            #Agregando el nombre del evento:
            try:
                if self.input_nombre.text == "": raise Exception("Debe darle un nombre al evento")
                if self.input_sala.text == "Seleccione una sala": raise Exception("Debe seleccionar una sala")
                if len(evento.recursos_herramienta) == 0: raise Exception("Debe seleccionar al menos 1 recurso herramienta")
                if len(evento.recursos_persona) == 0: raise Exception("Debe seleccionar un cientifico para su evento")

                year = int(self.year_inicio.text)
                month = int(self.month_inicio.text)
                day = int(self.day_inicio.text)
                hora = int(self.hora_inicio.text)
                minu = int(self.min_inicio.text)

                year_fin = int(self.year_fin.text)
                month_fin = int(self.month_fin.text)
                day_fin = int(self.day_fin.text)
                hora_fin = int(self.hora_fin.text)
                minu_fin = int(self.min_fin.text)

                #Posibles errores de la fecha inicio
                if 2025 > year or year > 2040: raise Exception("El ano de inicio esta fuera del rango disponible")
                if 1 > month or month > 12: raise Exception("EL mes del inicio del eveno es incorrecto")
                if 1 > day or day > calendar.monthrange(year, month)[1]: raise Exception("El dia de inicio de su evento es incorrecto")
                if 0 > hora or hora > 23: raise Exception("La hora del inicio de su evento es incorrecta")
                if 0 > minu or minu > 59: raise Exception("La hora del inicio de su evento es incorrecta")

                #Posibles errores de la fecha fin
                if 2025 > year_fin or year_fin > 2030: raise Exception("El ano del fin de su evento es incorrecto")
                if year_fin < year: raise Exception("El ano del final es menor que el ano del inicio, por favor introduscalo correctamente")
                if 1 > month_fin or month_fin > 12: raise Exception("El mes del fin de su evento es incorrecto")
                if 1 > day_fin or day_fin > calendar.monthrange(year_fin, month_fin)[1]: raise Exception("El dia del fin del evento es incorrecto")
                if 0 > hora_fin or hora_fin > 23: raise Exception("La hora del final de su evento es incorrecta")
                if 0 > minu_fin or minu_fin > 59: raise Exception("La hora del final de su evento es incorrecta")

                if self.input_sala.text == "Planetario" and not(("Claudia Aguilar",1) in evento.recursos_persona): raise Exception(f"En la sala Planetario debe estar la encargada de esta sala")

                for n in evento.recursos_herramienta:
                    if (n[0] == "Gafas virtuales" or n[0] == "Portatiles" or n[0] == "Telescopio") and not(self.input_sala.text == "Sala de conferencias" or self.input_sala.text == "Planetario"): raise Exception(f"El recurso {n[0]} solo puede ser usado en la sala de conferencias o en el planetario")
                    if (n[0] == "Telescopio de agujeros negros") and not(("Stiphen Hawking",1) in evento.recursos_persona or ("Neil Tyson",1) in evento.recursos_persona): raise Exception(f"El {n[0]} solo puede ser usado por especialistas de agujeros negros")
                    if (n[0] == "Telescopio Lunar") and not(("Margaret Burbidge",1) in evento.recursos_persona or ("Neil Tyson",1) in evento.recursos_persona): raise Exception(f"El {n[0]} solo puede ser utilizado por especialistas de la luna")
                    if (n[0] == "Telescopio de Galaxias") and not(("Vera Rubin",1) in evento.recursos_persona or ("Edwin Huble",1) in evento.recursos_persona or ("Neil Tyson",1) in evento.recursos_persona): raise Exception(f"El {n[0]} solo puede ser utilizado por especialistas de galaxias")
                    if (n[0] == "Telescopio Solar") and not(("Hans Bethe",1) in evento.recursos_persona or ("Carl Sagan",1) in evento.recursos_persona or ("Neil Tyson",1) in evento.recursos_persona): raise Exception(f"El {n[0]} solo puede ser utilizados por especialistas del sol")
                    if (n[0] == "Polarimetro" or n[0] == "Espectrometro") and not(("Henrietta Leavitt") in evento.recursos_persona): raise Exception(f"El {n[0]} es solo puede ser utilizado por Henrietta Leavitt")

            except Exception as e:
                error = e.args[0] if type(e) != ValueError else "Su formato de fecha es incorrecto"
                self.mostrar_error(error)
                
            else:
                print(f"Recursos herramienta: {evento.recursos_herramienta}")
                print(f"Recursos sala: {evento.recursos_sala}")

                nombre = self.input_nombre.text
                fecha = datetime.datetime(year,month,day,hora,minu)
                fecha_fin = datetime.datetime(year_fin,month_fin,day_fin,hora_fin,minu_fin)
                evento.recursos_sala.clear()
                evento.recursos_sala.append((self.input_sala.text,1))
                recursos = evento.recursos_sala+evento.recursos_herramienta+evento.recursos_persona

                print(recursos)

                event = Evento(
                    nombre= nombre,
                    inicio= fecha,
                    fin= fecha_fin,
                    recursos=recursos
                )

                self.mostrar_error(operaciones.agregar_evento(event))


    def restaurar_color(self,touch):
            self.source = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003303.png"

class ButtonBuscarHueco(ButtonBehavior,Image):
    def __init__(self,input_nombre,input_sala):
        super().__init__()
        self.input_nombre = input_nombre
        self.input_sala = input_sala
        self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003304.png"
        self.size_hint = (None,None)
        self.size = (190,80)
        self.pos = (770,120)

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Buscar_hueco_Touch.png"
            Clock.schedule_once(lambda dt: self.restaurar_color(touch), 0.15)
            self.pedir_duracion(touch)
            
            
    def pedir_duracion(self,touch):
        self.contenedor = vent_cant()
        self.horas = TextInput(size_hint=(None,None),size=(70,30),hint_text="Horas",cursor_color=(1,0,0,1),background_color=(1,0,0,0.4),font_size=17,pos_hint={"center_x":0.5,"top":0.9},foreground_color=(1,1,1,1))
        self.popup = Popup(title='Diga cuantas horas dura el evento',content=self.contenedor,size_hint=(None, None),size=(250, 140),background_color=(0.2,0,0.6,0.9))
        self.btn_aceptar = Button(size_hint=(None,None),size=(100,30),text="Aceptar",pos_hint={"center_x":0.50,"center_y":0.1},padding=(0,100),background_color=(0.6,0,1,0.7))
        
        self.contenedor.add_widget(self.horas)
        self.contenedor.add_widget(self.btn_aceptar)

        self.btn_aceptar.bind(on_press=self.buscar)

        self.popup.open()
    
    def buscar(self,instance):
        try:
            inicio = datetime.datetime.now()
            fin = inicio + datetime.timedelta(hours=int(self.horas.text))
            if self.input_nombre.text == "": raise Exception("Debe darle un nombre al evento")
            if self.input_sala.text == "Seleccione una sala": raise Exception("Debe seleccionar una sala")
            if len(evento.recursos_herramienta) == 0: raise Exception("Debe seleccionar al menos 1 recurso herramienta")
            if len(evento.recursos_persona) == 0: raise Exception("Debe seleccionar un cientifico para su evento")

            if self.input_sala.text == "Planetario" and not(("Claudia Aguilar",1) in evento.recursos_persona): raise Exception(f"En la sala Planetario debe estar la encargada de esta sala")

            for n in evento.recursos_herramienta:
                if (n[0] == "Gafas virtuales" or n[0] == "Portatiles" or n[0] == "Telescopio") and not(self.input_sala.text == "Sala de conferencias" or self.input_sala.text == "Planetario"): raise Exception(f"El recurso {n[0]} solo puede ser usado en la sala de conferencias o en el planetario")
                if (n[0] == "Telescopio de agujeros negros") and not(("Stiphen Hawking",1) in evento.recursos_persona or ("Neil Tyson",1) in evento.recursos_persona): raise Exception(f"El {n[0]} solo puede ser usado por especialistas de agujeros negros")
                if (n[0] == "Telescopio Lunar") and not(("Margaret Burbidge",1) in evento.recursos_persona or ("Neil Tyson",1) in evento.recursos_persona): raise Exception(f"El {n[0]} solo puede ser utilizado por especialistas en astros")
                if (n[0] == "Telescopio de Galaxias") and not(("Vera Rubin",1) in evento.recursos_persona or ("Edwin Huble",1) in evento.recursos_persona or ("Neil Tyson",1) in evento.recursos_persona): raise Exception(f"El {n[0]} solo puede ser utilizado por especialistas de galaxias")
                if (n[0] == "Telescopio solar") and not(("Hans Bethe",1) in evento.recursos_persona or ("Carl Sagan",1) in evento.recursos_persona or ("Neil Tyson",1) in evento.recursos_persona): raise Exception(f"El {n[0]} solo puede ser utilizados por especialistas del sol")
                if (n[0] == "Polarimetro" or n[0] == "Espectrometro") and not(("Henrietta Leavitt") in evento.recursos_persona): raise Exception(f"El {n[0]} es solo puede ser utilizado por Henrietta Leavitt")

        except Exception as e:
            error = e.args[0] if type(e) != ValueError else "El formato de la duracion es incorrecto"
            self.mostrar_error(error)
        
        else:
            nombre = self.input_nombre.text
            fecha = inicio
            fecha_fin = fin
            evento.recursos_sala.clear()
            evento.recursos_sala.append((self.input_sala.text,1))
            recursos = evento.recursos_sala+evento.recursos_herramienta+evento.recursos_persona
    
            event = Evento(
                nombre=nombre,
                inicio=fecha,
                fin=fecha_fin,
                recursos=recursos
            )
            self.mostrar_error(operaciones.buscar(event,int(self.horas.text)))
            

    def mostrar_error(self,error):
        self.error = Label(text=error,size_hint=(None,None),size=(250,140),pos_hint={"center_x":0.3,"center_y":0},text_size=(200,140),valign='top')
        self.popup_error = Popup(title='Error',content=self.error,size_hint=(None, None),size=(250, 140),background_color=(0.2,0,0.6,0.9))
        self.popup_error.open()

    def restaurar_color(self,touch):    
            self.source = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003304.png"

class OpcionPersonalizada(Button):
    """Clase personalizada para las opciones del spinner"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.4, 0.4, 0.9, 1)  # Color de fondo
        self.color = (1, 1, 1, 1)  # Color del texto
        self.size_hint_y = None
        self.height = 40 # ALTURA de cada opción
        self.font_size = '20sp'

            



class Agregar_Evento(FloatLayout):
    def __init__(self):
        super().__init__()
        #self.orientation = "horizontal"

        self.input_nombre = TextInput(
            hint_text = "Nombre del evento",
            font_size = 20,
            background_color = (0,0.3,0,0.4),
            size_hint = (None,None),
            size = (420,40),
            pos_hint = {"center_x": 0.68,"center_y" : 0.83},
        )
        self.year_inicio = TextInput(
            hint_text="year",
            size_hint = (None,None),
            background_color=(0,0.3,0,0.4),
            size = (68,30),
            font_size = 16,
            pos_hint = {"center_x": 0.56,"center_y" : 0.55},
        )
        self.year_fin = TextInput(
            hint_text="year",
            size_hint = (None,None),
            background_color=(0,0.3,0,0.4),
            size = (68,30),
            font_size = 16,
            pos_hint = {"center_x": 0.56,"center_y" : 0.43},
        )
        self.month_inicio = TextInput(
            hint_text = 'month',
            size_hint = (None,None),
            background_color=(0,0.3,0,0.4),
            size = (68,30),
            font_size = 16,
            pos_hint = {"center_x": 0.656,"center_y" : 0.55},
        )
        self.month_fin = TextInput(
            hint_text = 'month',
            size_hint = (None,None),
            background_color=(0,0.3,0,0.4),
            size = (68,30),
            font_size = 16,
            pos_hint = {"center_x": 0.656,"center_y" : 0.43},
        )
        self.day_inicio = TextInput(
            hint_text = "day",
            size_hint = (None,None),
            cursor_color = (0,0,0,1),
            background_color=(0,0.3,0,0.4),
            size = (68,30),
            font_size = 16,
            pos_hint = {"center_x": 0.75,"center_y" : 0.55},
        )
        self.day_fin = TextInput(
            hint_text = "day",
            size_hint = (None,None),
            cursor_color = (0,0,0,1),
            background_color=(0,0.3,0,0.4),
            size = (68,30),
            font_size = 16,
            pos_hint = {"center_x": 0.75,"center_y" : 0.43},
        )
        self.hora_inicio = TextInput(
            font_size = 14,
            background_color = (0,0.3,0,0.4),
            size_hint = (None,None),
            size = (30,30),
            pos_hint = {"center_x": 0.85,"center_y" : 0.55}
        )
        self.hora_fin = TextInput(
            font_size = 14,
            background_color = (0,0.3,0,0.4),
            size_hint = (None,None),
            size = (30,30),
            pos_hint = {"center_x": 0.85,"center_y" : 0.43}
        )
        self.min_inicio = TextInput(
            font_size = 14,
            background_color = (0,0.3,0,0.4),
            size_hint = (None,None),
            size = (30,30),
            pos_hint = {"center_x": 0.90,"center_y" : 0.55}
        )
        self.min_fin = TextInput(
            font_size = 14,
            background_color = (0,0.3,0,0.4),
            size_hint = (None,None),
            size = (30,30),
            pos_hint = {"center_x": 0.90,"center_y" : 0.43}
        )
        self.text_inicio = Label(
            text = " Inicio: ",
            font_size = 21, 
            size_hint = (None,None),
            size = (50,20),
            pos_hint = {"center_x": 0.47,"center_y" : 0.552}
        )
        self.text_fin = Label(
            text = " Fin: ",
            font_size = 21, 
            size_hint = (None,None),
            size = (50,20),
            pos_hint = {"center_x": 0.47,"center_y" : 0.432}
        )
        self.text_hora = Label(
            text = "Hora : Minutos",
            font_size = 15,
            size_hint = (None,None),
            size = (50,20),
            pos_hint = {"center_x": 0.88,"center_y" : 0.64}
        )
        self.selecc_sala = Spinner(
            text='Seleccione una sala',
            values=["Planetario","Cupula de observacion","Cupula de fotografia","Sala de conferencias","Sala de optica"],
            size_hint = (None,None),
            size = (260,35),
            font_size = 23,
            background_normal = "",
            option_cls=OpcionPersonalizada,
            pos_hint = {"center_x": 0.21,"center_y" : 0.8},
            background_color = (0,0,0,0.2),
        )
        self.selecc_sala.bind(text=self.cambiar_imagen_lbl)

        self.recursos_herramienta = BotonHerramientas()       

        self.guardar = ButtonGuardar(
            input_nombre=self.input_nombre,
            year_inicio=self.year_inicio,
            month_inicio=self.month_inicio,
            day_inicio=self.day_inicio,
            hora_inicio=self.hora_inicio,
            min_inicio=self.min_inicio,
            input_sala=self.selecc_sala,
            year_fin=self.year_fin,
            month_fin=self.month_fin,
            day_fin=self.day_fin,
            hora_fin=self.hora_fin,
            min_fin=self.min_fin

            )


        self.buscar_hueco = ButtonBuscarHueco(input_nombre=self.input_nombre,input_sala=self.selecc_sala,)

        self.recursos_personal = BotonPersonal() 

        self.text_recursos = Label(
            text = "Seleccione los recursos",
            font_size = 23,
            size_hint = (None,None),
            size = (100,30),
            pos_hint = {"center_x": 0.6,"center_y" : 0.25}
        )

        self.add_widget(self.buscar_hueco)
        self.add_widget(self.guardar)
        self.add_widget(self.recursos_herramienta)
        self.add_widget(self.recursos_personal)
        self.add_widget(self.text_recursos)
        self.add_widget(self.selecc_sala)
        self.add_widget(self.text_hora)
        self.add_widget(self.min_inicio)
        self.add_widget(self.hora_inicio)
        self.add_widget(self.day_inicio)
        self.add_widget(self.month_inicio)
        self.add_widget(self.year_inicio)
        self.add_widget(self.min_fin)
        self.add_widget(self.hora_fin)
        self.add_widget(self.day_fin)
        self.add_widget(self.month_fin)
        self.add_widget(self.year_fin)
        self.add_widget(self.text_inicio)
        self.add_widget(self.text_fin)
        self.add_widget(self.input_nombre)
        self.Lbl=Lbl()
        self.add_widget(self.Lbl)
        
    def cambiar_imagen_lbl(win, ins, seleccion):
        print("Eeeeeeeeeeeeeeeeeeeeeee")
        rutas = {
            "Planetario": "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Sala Planetario.png",
            "Cupula de observacion": "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Cupula de Observacion.png",
            "Cupula de fotografia": "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Sala Telescopio Principal.png",
            "Sala de conferencias": "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Sala de conferencias.png",
            "Sala de optica": "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Sala de Optica.png"
        }    
        print(rutas[seleccion])
        win.Lbl.actualizar_imagen(rutas[seleccion])


'''class Lbl(BoxLayout):
    def __init__(self,):
        super().__init__()
        self.imagen = Image(source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Sala Planetario.png",size_hint= (None,None), size=self.size)
        self.add_widget(self.imagen)'''

class Lbl(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Solo un widget de imagen que se actualiza
        self.imagen_widget = Image(
            source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Sala Planetario.png",
            size_hint=(None, None),
            size=self.size
        )
        self.add_widget(self.imagen_widget)
    
    def actualizar_imagen(self, nueva_ruta):
        print("Aaaaaaaaaaaaaaaaaaa")
        """Solo actualiza la fuente de la imagen existente"""
        self.imagen_widget.source = nueva_ruta
        self.imagen_widget.reload()  # Forzar recarga

class Item_event(ButtonBehavior,BoxLayout):
    def __init__(self,nombre,info,hora):
        super().__init__()
        self.orientation = "horizontal"
        self.size_hint=(None,None)
        self.size=(870,80)
        self.pos = self.center
        self.nombre = nombre
        self.info = info
        recursos = ""
        self.hora = hora



        for rec in self.info:
            if rec[1] > 1:
                recursos += f" {str(rec[0])} : {str(rec[1])},"
            else:
                recursos += f" {str(rec[0])},"

        informacion = Label(text=f"              Recursos:\n{recursos}",font_size=12,text_size=(280,60),pos_hint={"center_x":0,"center_y":0.7},color=(1,1,1,1))
        inf_hora = Label(text=self.hora,color=(0,0,0,1),size_hint=(None,None),size=(220,80))
        
        self.add_widget(Label(text= self.nombre,font_size=20,text_size=(220,80),valign="center"))
        self.add_widget(inf_hora)
        self.add_widget(informacion)


class cont_event(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation='vertical'
        self.size_hint = (None,None)
        self.bind(minimum_height=self.setter('height'))
        self.spacing = 8

        eventos = leer_json(ruta_eventos)

        for event in eventos.get("eventos"):
            self.add_widget(Item_event(nombre=event["nombre"],info=event["recursos"],hora=f"{event["inicio"]} : {event["fin"]}"))
 


class Ver_Eventos(FloatLayout):
    def __init__(self):
        super().__init__()
        self.orientation='vertical'
        self.lista_eventos = ScrollView(pos=(138,225))
        self.contenedor_eventos = cont_event()
        self.lista_eventos.add_widget(self.contenedor_eventos)
        self.add_widget(self.lista_eventos)
    



class Texto(Label):
    def __init__(self):
        super().__init__()        

class Titulo(BoxLayout):
    def __init__(self):
        super().__init__()
        self.imagen = Image(source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251116_040931.png",size_hint= (None,None), size= (100,65))
        self.add_widget(self.imagen)
        self.add_widget(Texto())

class Buttons(Button):
    def __init__(self,texto):
        super().__init__(text=texto)

class BoxButtons(BoxLayout):
    def __init__(self,box_principal):
        super().__init__()

        self.box_principal = box_principal

        self.add_eventos = Buttons("Agregar evento")
        self.add_eventos.contenido = "Agregar evento"
        self.add_eventos.bind(on_press=self.cambiar_ventana)
        self.add_widget(self.add_eventos)

        self.ver_eventos = Buttons("Ver eventos")
        self.ver_eventos.contenido = "Ver eventos"
        self.ver_eventos.bind(on_press=self.cambiar_ventana)
        self.add_widget(self.ver_eventos)

    def cambiar_ventana(self,instance):
        self.box_principal.mostrar(instance.contenido)
        self.box_principal.resaltar_boton_activo(instance)

class BoxL(BoxLayout):
    def __init__(self):
        super().__init__()

        self.titulo = Titulo()
        self.add_widget(self.titulo,index=0)  
        self.barra_botones = BoxButtons(self)
        self.add_widget(self.barra_botones,index=0)
        self.boxlayout_dinamico = BoxLayout(size_hint_y=None,height=400)
        self.add_widget(self.boxlayout_dinamico)
        self.mostrar("Agregar evento")
        self.add_widget(Label(),index=0)

    def mostrar(self,boton):
        self.boxlayout_dinamico.clear_widgets()

        if boton == "Agregar evento":
            self.nueva_ventana = Agregar_Evento()

        if boton == "Ver eventos":
            self.nueva_ventana = Ver_Eventos()

        self.boxlayout_dinamico.add_widget(self.nueva_ventana)
        
    def resaltar_boton_activo(self, boton_activo):
        """Resalta el botón activo y desresalta los demás"""
        color_activo = (0.3, 0.1, 0.8, 1)    # Azul/morado para activo
        color_inactivo = (0, 0, 0, 0)         # Transparente para inactivos
        
        # Recorrer todos los botones de la barra
        for boton in self.barra_botones.children:
            if boton == boton_activo:
                # Botón activo - color destacado
                boton.background_color = color_activo
                boton.color = (1, 1, 1, 1)  # Texto blanco
            else:
                # Botones inactivos - color normal
                boton.background_color = color_inactivo
                boton.color = (1, 1, 1, 1)  # Texto blanco



class Contenedor(FloatLayout):
    def __init__(self):
        super().__init__()
        self.background = Image(source="Imagenes/Copilot_20251116_014842.png")
        self.add_widget(self.background)
        self.body = BoxL()
        self.add_widget(self.body)

class Myapp(App):
    def build(self):
        self.contenedor = Contenedor()
        return self.contenedor

Myapp().run()
