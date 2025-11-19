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
import datetime
import calendar
from Estilo import kv

Window.size = (1150,900)

Builder.load_string(kv)

class evento:
    recursos_persona = []
    recursos_herramienta = []
    recursos_sala = []
    nombre = []
    fecha = []
    datos = {}

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

        self.p1 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_1hxsj21hxsj21hxs.png"
        self.p2 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_2mdp3w2mdp3w2mdp.png"
        self.p3 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_2mmv5r2mmv5r2mmv.png"
        self.p4 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_98n6d698n6d698n6.png"
        self.p5 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_czxmoeczxmoeczxm.png"
        self.p6 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_iktxediktxediktx.png"
        self.p7 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_iudpr3iudpr3iudp.png"
        self.p8 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_izk5ekizk5ekizk5.png"
        self.p9 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_nz9ai9nz9ai9nz9a.png"
        self.p10 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_qfio6yqfio6yqfio.png"
        self.p11 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_tx3ambtx3ambtx3a.png"
        self.p12 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_u9ll5su9ll5su9ll.png"
        self.p13 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_nthhyhnthhyhnthh.png"

        opciones = [(1,self.p1),(2,self.p2),(3,self.p3),(4,self.p4),(5,self.p5),(6,self.p6),(7,self.p7),(8,self.p8),(9,self.p9),
        (10,self.p10),(11,self.p11),(12,self.p12),(13,self.p13)]

        self.all_opciones = []
        for opcion,img in opciones:
            btn = OpcionPersonal(
            opcion=opcion,
            size_hint=(None, None),
            size=(80, 80),
            allow_stretch=True,
            source = img,
            state='down' if opcion in self.opciones_seleccionadas else 'normal',
            img_press= "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Guardar_Touch.png"
            )
            self.all_opciones.append(btn)
            self.grid.add_widget(btn)
        
        self.boton_aceptar = botonAceptar(all_opciones=self.all_opciones,popup=self.popup_H,Id="Herramienta")
        self.boton_salir = botonSalir(popup=self.popup_H)
        self.row4.add_widget(self.boton_aceptar)
        self.row4.add_widget(self.boton_salir)
        self.contenedor.add_widget(self.grid)
        self.contenedor.add_widget(self.row4)
        self.menu_H.add_widget(self.contenedor)
        
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
            self.popup = Popup(title='Mis Preferencias',content=self.menu,size_hint=(None, None),size=(750, 840),background_color=(0.2,0,0.6,0.9))
            self.popup.open()
            self.opciones_seleccionadas = []

            self.grid = GridLayout(cols=5,spacing=(40,20),rows=5,size_hint=(None,None),size=(300,400))
            self.contenedor = Contenedor_Recursos()
            self.row4 =FloatLayout(size_hint=(None,None),size=(725,140),pos=self.pos)
            self.fila = filas(orientacion="vertical",tamano=(700,210),espacio=0)

            self.p1 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_1oeimx1oeimx1oei.png"
            self.p2 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_2hqe7c2hqe7c2hqe.png"
            self.p3 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_4wxxcw4wxxcw4wxx.png"
            self.p4 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_egvy09egvy09egvy.png"
            self.p5 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_i15n42i15n42i15n.png"
            self.p6 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_lzntnplzntnplznt.png"
            self.p7 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_n343ibn343ibn343.png"
            self.p8 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_pgqci1pgqci1pgqc.png"
            self.p9 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_rt9orart9orart9o.png"
            self.p10 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_w63t9uw63t9uw63t.png"
            self.p11 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_ug969bug969bug96.png"
            self.p12 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_wpdhhswpdhhswpdh.png"
            self.p13 = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Gemini_Generated_Image_xbjwuuxbjwuuxbjw.png"

            opciones = [("Carl Sagan",self.p1),("Vera Rubin",self.p2),("Henrietta Leavitt",self.p3),("Arthur Eddington",self.p4),("Edwin Huble",self.p5),(6,self.p6),("Roger Penrose",self.p7),("Margaret Burbidge",self.p8),("Hans Bethe",self.p9),
            ("Neil Tyson",self.p10),("Stiphen Hawking",self.p11)]

            self.all_opciones = []

            for opcion,img in opciones:
                btn = OpcionPersonal(
                opcion=opcion,
                size_hint=(None, None),
                size=(80, 80),
                allow_stretch=True,
                source = img,
                state='down' if opcion in self.opciones_seleccionadas else 'normal',
                img_press = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Guardar_Touch.png"
                )
                
                self.all_opciones.append(btn)
                self.grid.add_widget(btn)

            for b in self.all_opciones:
                print(b.state)

            #Creando los botones de accion:
            self.boton_aceptar = botonAceptar(all_opciones=self.all_opciones,popup=self.popup,Id="Persona")
            self.boton_salir = botonSalir(popup=self.popup)
            self.row4.add_widget(self.boton_aceptar)
            self.row4.add_widget(self.boton_salir)
            self.contenedor.add_widget(self.grid)
            self.contenedor.add_widget(self.fila)
            self.contenedor.add_widget(self.row4)

            self.menu.add_widget(self.contenedor)\
    
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
                evento.recursos_persona= [btn.opcion for btn in self.all_opciones if btn.state == 'down']
            if self.Id == "Herramienta":
                evento.recursos_herramienta.clear()
                evento.recursos_herramienta = [btn.opcion for btn in self.all_opciones if btn.state == 'down']
            self.popup.dismiss()
            print(evento.recursos_herramienta)
            print(evento.recursos_persona)
    
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

class OpcionPersonal(ButtonBehavior, Image):
    def __init__(self, opcion,img_press, **kwargs):
        super().__init__(**kwargs)
        self.opcion = opcion
        self.seleccionado = False
        self.img = self.source
        self.size_hint = (None,None)
        self.size = (100,100)
        self.img_press = img_press
 
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.state = 'down'
            self.on_press()
        
    def on_press(self):
        self.seleccionado = not self.seleccionado
        if self.seleccionado:
            self.source = self.img_press
        else:
            self.source = self.img  # Imagen cuando no está seleccionado

class ButtonGuardar(ButtonBehavior,Image):
    def __init__(self,input_nombre,input_year,input_month,input_day,input_hora,input_min,input_sala):
        super().__init__()
        self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003303.png"
        self.size_hint = (None,None)
        self.size = (190,80)
        self.pos = (510,120)
        self.input_nombre = input_nombre
        self.input_year = input_year
        self.input_month = input_month
        self.input_day = input_day
        self.input_hora = input_hora
        self.input_min = input_min
        self.input_sala = input_sala
        
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Guardar_Touch.png"
            Clock.schedule_once(lambda dt: self.restaurar_color(touch), 0.15)
    
            #Agregando el nombre del evento:
            try:
                if self.input_nombre.text == "": raise Exception("Sin nombre")
                if self.input_sala.text == "Seleccione una sala": raise Exception("Sin sala")

                year = int(self.input_year.text)
                month = int(self.input_month.text)
                day = int(self.input_day.text)
                hora = int(self.input_hora.text)
                minu = int(self.input_min.text)

                if 2025 > year or year > 2030: raise Exception("Ano incorrecto")
                if 1 > month or month > 12: raise Exception("Mes incorrecto")
                if 2025 > year or year > 2032: raise Exception("Ano incorrecto")
                if 1 > day or day > calendar.monthrange(year, month)[1]: raise Exception("Dia incorrecto")
                if 0 > hora or hora > 23: raise Exception("Hora incorrecta")
                if 0 > minu or minu > 59: raise Exception("Minutos incorrectos")

            except Exception as e:
                error = e.args[0] if type(e) != ValueError else "Fecha incorrecta!"
                print(error)
                
            else:
                nombre = self.input_nombre.text
                fecha = datetime.datetime(year,month,day,hora,minu)
                evento.recursos_sala.append(self.input_sala.text)
                recursos = evento.recursos_herramienta+evento.recursos_persona+evento.recursos_sala
                
                evento.datos["Nombre"] = nombre
                evento.datos["Fecha"] = fecha
                evento.datos["Recursos"] = recursos


            '''

            if self.input_nombre.text == "":
                print("Deve ponerle un nombre al evento")
            else:
                nombre = self.input_nombre.text

                #Agregando la fecha del evento(Si alguno de los campos esta vacio dar error)
                if self.input_year.text=="" or self.input_month.text=="" or self.input_day.text=="" or self.input_hora.text=="" or self.input_min.text== "":
                    print("Deve completar todos los campos de la fecha")
               # elif type(self.input_year.text) != int or type(self.input_month.text) != int or type(self.input_day.text) != int or type(self.input_hora.text) != int or type(self.input_min.text) != int:
                #    print("Entrada no valida")
                else:
                    fecha = self.input_year.text,self.input_month.text,self.input_day.text,self.input_hora.text,self.input_min.text

                    if self.input_sala.text == 'Seleccione una sala':
                        print("Debe seleccionar una sala")
            #Agregar los recursos del evento
            evento.recursos_sala.append(self.input_sala.text)
            recursos = evento.recursos_herramienta+evento.recursos_persona+evento.recursos_sala

            '''
            #Guardando los datos en un diccionario:
            '''evento.datos["Nombre"] = nombre
            evento.datos["Fecha"] = fecha
            evento.datos["Recursos"] = recursos'''

            print(evento.datos)
            

    def restaurar_color(self,touch):
            self.source = "/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003303.png"

class ButtonBuscarHueco(ButtonBehavior,Image):
    def __init__(self):
        super().__init__()
        self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251117_003304.png"
        self.size_hint = (None,None)
        self.size = (190,80)
        self.pos = (770,120)

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Buscar_hueco_Touch.png"
            Clock.schedule_once(lambda dt: self.restaurar_color(touch), 0.15)

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

        self.orientation = "horizontal"

        self.input_nombre = TextInput(
            font_size = 19,
            background_color = (0,0.3,0,0.4),
            size_hint = (None,None),
            size = (420,40),
            pos_hint = {"center_x": 0.68,"center_y" : 0.78},
        )
        self.year_fecha = TextInput(
            size_hint = (None,None),
            background_color=(0,0.3,0,0.4),
            size = (80,30),
            font_size = 16,
            pos_hint = {"center_x": 0.48,"center_y" : 0.45},
        )
        self.month_fecha = TextInput(
            size_hint = (None,None),
            background_color=(0,0.3,0,0.4),
            size = (80,30),
            font_size = 16,
            pos_hint = {"center_x": 0.60,"center_y" : 0.45},
        )
        self.dia_fecha = TextInput(
            size_hint = (None,None),
            cursor_color = (0,0,0,1),
            background_color=(0,0.3,0,0.4),
            size = (80,30),
            font_size = 16,
            pos_hint = {"center_x": 0.72,"center_y" : 0.45},
        )
        self.hora = TextInput(
            font_size = 14,
            background_color = (0,0.3,0,0.4),
            size_hint = (None,None),
            size = (30,30),
            pos_hint = {"center_x": 0.85,"center_y" : 0.45}
        )
        self.minutos = TextInput(
            font_size = 14,
            background_color = (0,0.3,0,0.4),
            size_hint = (None,None),
            size = (30,30),
            pos_hint = {"center_x": 0.90,"center_y" : 0.45}
        )
        self.nombre = Label(
            text = "Nombre del evento",
            font_size = 20,
            size_hint = (None,None),
            size = (50,20),
            pos_hint = {"center_x": 0.7,"center_y" : 0.9}
        )
        self.fecha = Label(
            text = "          Year        Month       Day",
            font_size = 23,
            size_hint = (None,None),
            size = (50,20),
            pos_hint = {"center_x": 0.55,"center_y" : 0.55}
        )
        self.text_hora = Label(
            text = "Hora : Minutos",
            font_size = 15,
            size_hint = (None,None),
            size = (50,20),
            pos_hint = {"center_x": 0.88,"center_y" : 0.54}
        )
        self.selecc_sala = Spinner(
            text='Seleccione una sala',
            values=["Planetario","Sala del telescopio principal","Cupula de fotografia","Sala de exposiciones","Cupulas de observacion"],
            size_hint = (None,None),
            size = (260,35),
            font_size = 23,
            background_normal = "",
            option_cls=OpcionPersonalizada,
            pos_hint = {"center_x": 0.21,"center_y" : 0.8},
            background_color = (0,0,0,0.2)
        )        

        recursos_herramienta = BotonHerramientas()       

        guardar = ButtonGuardar(
            input_nombre=self.input_nombre,
            input_year=self.year_fecha,
            input_month=self.month_fecha,
            input_day=self.dia_fecha,
            input_hora=self.hora,
            input_min=self.minutos,
            input_sala=self.selecc_sala)

        buscar_hueco = ButtonBuscarHueco()

        recursos_personal = BotonPersonal() 

        text_recursos = Label(
            text = "Seleccione los recursos",
            font_size = 23,
            size_hint = (None,None),
            size = (100,30),
            pos_hint = {"center_x": 0.6,"center_y" : 0.25}
        )

        self.add_widget(buscar_hueco)
        self.add_widget(guardar)
        self.add_widget(recursos_herramienta)
        self.add_widget(recursos_personal)
        self.add_widget(text_recursos)
        self.add_widget(self.selecc_sala)
        self.add_widget(self.text_hora)
        self.add_widget(self.minutos)
        self.add_widget(self.hora)
        self.add_widget(self.dia_fecha)
        self.add_widget(self.month_fecha)
        self.add_widget(self.year_fecha)
        self.add_widget(self.fecha)
        self.add_widget(self.nombre)
        self.add_widget(self.input_nombre)
        self.add_widget(Lbl())

class Eventos_Importantes(BoxLayout):
    def __init__(self):
        super().__init__()

        self.orientation = "vertical"
        tex = Label(
            text="Eventos Importantes",
            font_size= 45,
            markup=True,
            halign="center")
        self.add_widget(tex)

class Lbl(BoxLayout):
     def __init__(self):
        super().__init__()
        self.imagen = Image(source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Sala Planetario.png",size_hint= (None,None), size=self.size)
        self.add_widget(self.imagen)

class Ver_Eventos(BoxLayout):
    def __init__(self):
        super().__init__()

        self.orientation = "vertical"
        tex = Label(
            text="Ver_eventos",
            font_size= 60,
            markup=True,
            halign="center")
        self.add_widget(tex)

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
        self.important_eventos = Buttons("Eventos importantes")
        self.important_eventos.contenido = "Eventos importantes"
        self.important_eventos.bind(on_press=self.cambiar_ventana)
        self.add_widget(self.important_eventos)
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
            nueva_ventana = Agregar_Evento()
        if boton == "Eventos importantes":
            nueva_ventana = Eventos_Importantes()
        if boton == "Ver eventos":
            nueva_ventana = Ver_Eventos()

        self.boxlayout_dinamico.add_widget(nueva_ventana)
        
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
        self.background = Image(source="/home/adan/Adan/Programacion/Projects/Project Pro 1/Imagenes/Copilot_20251116_014842.png")
        self.add_widget(self.background)
        self.body = BoxL()
        self.add_widget(self.body)

class Myapp(App):
    def build(self):
        return Contenedor()

Myapp().run()

print(evento.nombre)