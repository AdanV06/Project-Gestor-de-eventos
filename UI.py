from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

Config.set('graphics', 'width', '1024')    # Ancho de 800 pixels
Config.set('graphics', 'height', '768')   # Alto de 600 pixels
Config.set('graphics', 'resizable', '0')

kv = '''
<BoxL>:
    size_hint: None,None 
    size: 800,600
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    orientation: "vertical"

    canvas.before:
        Color:
            rgba: 0.2,0,0.7,0.65
        
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15]

    canvas.after:
        Color:
            rgba: 0,0,0,1
        Line:
            rounded_rectangle: (self.x,self.y,self.width,self.height,15)
            width: 1.2

<BoxButtons>:
    size_hint: None,None
    size: 800,50


    canvas.before:
        Color:
            rgba: 0,0,0,0.1
        RoundedRectangle:
            pos: self.pos
            size: self.size

<Buttons>:
    background_color: 0,0,0,0
    font_size: 20

    canvas.after:
        Color:
            rgba: 1,1,1,1
        Line: 
            points: (self.x+1,self.y,self.x+self.width-1,self.y)
            width: 1.5
        
    
<Titulo>:
    size_hint: None,None
    size: 800,70


    canvas.before:
        Color:
            rgba: 0,0,0,0.1
        RoundedRectangle:
            pos: self.pos
            size: self.size
<Texto>:
    markup: True
    text: "[b] Observatorio de Astrofisica [/b]"
    font_size: 36
    pos_hint: {"center_x": 0,"center_y": 0.35}
    size_hint: None,None
    size: self.texture_size
    

'''


Builder.load_string(kv)

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
    def __init__(self):
        super().__init__()

        self.add_eventos = Buttons("Agregar evento")
        self.add_widget(self.add_eventos)

        self.important_eventos = Buttons("Eventos importantes")
        self.add_widget(self.important_eventos)

        self.buscar_hueco = Buttons("Buscar hueco")
        self.add_widget(self.buscar_hueco)

        self.ver_eventos = Buttons("Ver eventos")
        self.add_widget(self.ver_eventos)

class BoxL(BoxLayout):
    def __init__(self):
        super().__init__()

        self.titulo = Titulo()
        self.add_widget(self.titulo,index=0)  

        self.barra_botones = BoxButtons()
        self.add_widget(self.barra_botones,index=0)


        self.add_widget(Label(),index=0)





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


