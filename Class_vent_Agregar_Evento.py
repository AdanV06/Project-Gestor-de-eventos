from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.image import Image


#Opciones de el espiner seleccionar sala
class OpcionPersonalizada(Button):
    """Clase personalizada para las opciones del spinner"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.4, 0.4, 0.9, 1)  # Color de fondo
        self.color = (1, 1, 1, 1)  # Color del texto
        self.size_hint_y = None
        self.height = 40 # ALTURA de cada opción
        self.font_size = '20sp'

class Input_Name(TextInput):
    def __init__(self):
        super().__init__()

class Year_inicio(TextInput):
    def __init__(self):
        super().__init__()

class Year_fin(TextInput):
    def __init__(self):
        super().__init__()

class Month_inicio(TextInput):
    def __init__(self):
        super().__init__()

class Month_fin(TextInput):
    def __init__(self):
        super().__init__()

class Day_inicio(TextInput):
    def __init__(self):
        super().__init__()

class Day_fin(TextInput):
    def __init__(self):
        super().__init__()

class Hora_inicio(TextInput):
    def __init__(self):
        super().__init__()

class Hora_fin(TextInput):
    def __init__(self):
        super().__init__()

class Min_inicio(TextInput):
    def __init__(self):
        super().__init__()

class Min_fin(TextInput):
    def __init__(self):
        super().__init__()

class Text_inicio(Label):
    def __init__(self):
        super().__init__()

class Text_fin(Label):
    def __init__(self):
        super().__init__()

class Text_hora(Label):
    def __init__(self):
        super().__init__()
    
class Text_recursos(Label):
    def __init__(self):
        super().__init__()

class Sala_selec(Spinner):
    def __init__(self):
        super().__init__()
        self.option_cls=OpcionPersonalizada

