from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

'''
En este archivo se contiene todas las clases declaradas para la creacion de la ventanda Agregar Evento
'''

#Opciones de el espiner seleccionar sala
class OpcionPersonalizada(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.4, 0.4, 0.9, 1) 
        self.color = (1, 1, 1, 1)  
        self.size_hint_y = None
        self.height = 40 
        self.font_size = '20sp'

#TexInput para ingresar el nombre del evento
class Input_Name(TextInput):
    def __init__(self):
        super().__init__()

#Año de inicio del evento
class Year_inicio(TextInput):
    def __init__(self):
        super().__init__()

#Año del fin del evento
class Year_fin(TextInput):
    def __init__(self):
        super().__init__()

#Mes de inicio del evento
class Month_inicio(TextInput):
    def __init__(self):
        super().__init__()

#Mes del fin del evento
class Month_fin(TextInput):
    def __init__(self):
        super().__init__()

#Dia de inicio del evento
class Day_inicio(TextInput):
    def __init__(self):
        super().__init__()

#Dia del fin del evento
class Day_fin(TextInput):
    def __init__(self):
        super().__init__()

#Hora de inicio del evento
class Hora_inicio(TextInput):
    def __init__(self):
        super().__init__()

#Hora del fin del evento
class Hora_fin(TextInput):
    def __init__(self):
        super().__init__()

#Minutos del inicio del evento
class Min_inicio(TextInput):
    def __init__(self):
        super().__init__()

#Minutos del final del evento
class Min_fin(TextInput):
    def __init__(self):
        super().__init__()

#Texto para el inicio del evengo
class Text_inicio(Label):
    def __init__(self):
        super().__init__()

#Texto para el fin del evento
class Text_fin(Label):
    def __init__(self):
        super().__init__()

#Texto para la hora inicio del evento
class Text_hora(Label):
    def __init__(self):
        super().__init__()

#Texto para seleccionar los recursos
class Text_recursos(Label):
    def __init__(self):
        super().__init__()

#Texto para seleccionar una sala
class Sala_selec(Spinner):
    def __init__(self):
        super().__init__()
        self.option_cls=OpcionPersonalizada

#BoxLayout que contiene las imagenes de la sala 
class Lbl(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.imagen_widget = Image(
            source="Imagenes/Sala Planetario.png",#Imagen por defecto
            size_hint=(None, None),
            size=self.size
        )
        self.add_widget(self.imagen_widget)
    #Funcion para actualizar la imagen de la sala despues de seleccionar alguna
    def actualizar_imagen(self, nueva_ruta):
        self.imagen_widget.source = nueva_ruta
        self.imagen_widget.reload()  