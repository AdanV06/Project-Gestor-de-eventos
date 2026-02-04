from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

'''
Aqui se contienen las clases declaradas para la creacion de la ventana para seleccionar recursos,
todo este archivo es parte de el diseño de la interfaz grafica
'''


#Label que contiene la descrpcion de cada recurso
class informacion(Label):
    def __init__(self,inf):
        super().__init__()
        self.text = inf

#Contenedor de la descripcion completa de los recursos
class informacion_personaje(BoxLayout):
    def __init__(self,imagen,inf,nombre):
        super().__init__()
        self.imagen = Image(source=imagen,size_hint=(None,None),size=(180,180), pos=(260,195))
        self.informacion = informacion(inf=inf)
        self.spacing = 2
        self.nombre = nombre
        print(self.nombre)

        self.espacio = filas(orientacion="horizontal",tamano=(30,0),espacio=2)
        self.img = Lbl_img()
        self.img.add_widget(self.imagen)
        
        self.add_widget(self.espacio)
        self.add_widget(self.img)
        self.add_widget(self.informacion)


class filas(BoxLayout):
    def __init__(self,orientacion,tamano,espacio):
        super().__init__()
        self.orientation = orientacion
        self.size = tamano
        self.spacing = espacio

#Contenedor de la imagen de descripcion del recurso
class Lbl_img(FloatLayout):
    def __init__(self):
        super().__init__()

#Contenedor de los recursos
class Contenedor_Recursos(BoxLayout):
    def __init__(self):
        super().__init__()

#Contenedor de todo el menu de recursos
class menu(BoxLayout):
    def __init__(self):
        super().__init__()

#Boton para salr de la ventana
class botonSalir(ButtonBehavior,Image):
    def __init__(self,popup):
        super().__init__()
        self.popup = popup

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.source="Imagenes/Cancelar_pulsado.png"
            Clock.schedule_once(lambda dt: self.restaurar_color(touch), 0.15)
            self.popup.dismiss()

    def restaurar_color(self,touch):
            self.source = "Imagenes/Cancelar.png"

#Contenedor de la ventana para la cantidad
class vent_cant(FloatLayout):
    def __init__(self):
        super().__init__()