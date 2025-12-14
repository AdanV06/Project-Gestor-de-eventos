from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')
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
            rgba: 0,0,0,0
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
            width: 1.1
        
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

<ContenidoBase>:
    padding: 30
    spacing: 15
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
    def __init__(self, texto):
        super().__init__(text=texto)


class Agregar_Evento(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        label = Label(
            text='[b]AGREGAR NUEVO EVENTO[/b]\\nFormulario para ingresar eventos astronómicos',
            font_size=24,
            markup=True,
            halign='center'
        )
        self.add_widget(label)

class Eventos_Importantes(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        label = Label(
            text='[b]EVENTOS IMPORTANTES[/b]\\nLista de eventos destacados',
            font_size=24,
            markup=True,
            halign='center'
        )
        self.add_widget(label)

class Buscar_Hueco(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        label = Label(
            text='[b]BUSCAR HUECO TEMPORAL[/b]\\nHerramienta de búsqueda de ventanas',
            font_size=24,
            markup=True,
            halign='center'
        )
        self.add_widget(label)

class Ver_Eventos(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        label = Label(
            text='[b]VISUALIZAR EVENTOS[/b]\\nLista completa de eventos',
            font_size=24,
            markup=True,
            halign='center'
        )
        self.add_widget(label)

class BoxButtons(BoxLayout):
    def __init__(self, box_principal):
        super().__init__()
        self.box_principal = box_principal  # Guardamos referencia directa
        
        # Crear botones con referencia al contenido que activan
        self.add_eventos = Buttons("Agregar evento")
        self.add_eventos.contenido = 'agregar_evento'
        self.add_eventos.bind(on_press=self.on_boton_presionado)
        self.add_widget(self.add_eventos)

        self.important_eventos = Buttons("Eventos importantes")
        self.important_eventos.contenido = 'eventos_importantes'
        self.important_eventos.bind(on_press=self.on_boton_presionado)
        self.add_widget(self.important_eventos)

        self.buscar_hueco = Buttons("Buscar hueco")
        self.buscar_hueco.contenido = 'buscar_hueco'
        self.buscar_hueco.bind(on_press=self.on_boton_presionado)
        self.add_widget(self.buscar_hueco)

        self.ver_eventos = Buttons("Ver eventos")
        self.ver_eventos.contenido = 'ver_eventos'
        self.ver_eventos.bind(on_press=self.on_boton_presionado)
        self.add_widget(self.ver_eventos)

    def on_boton_presionado(self, instance):
        """Se ejecuta cuando se presiona cualquier botón"""
        # Cambiar el contenido
        self.box_principal.mostrar_contenido(instance.contenido)
        # Resaltar el botón activo
        self.box_principal.resaltar_boton_activo(instance)

class BoxL(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'

        self.titulo = Titulo()
        self.add_widget(self.titulo)

        # Crear barra de botones pasando referencia a self
        self.barra_botones = BoxButtons(self)
        self.add_widget(self.barra_botones)

        # CONTENEDOR DINÁMICO - donde va el contenido cambiante
        self.contenido_dinamico = BoxLayout()
        self.add_widget(self.contenido_dinamico)

        # Mostrar contenido inicial
        self.mostrar_contenido('agregar_evento')

    def mostrar_contenido(self, tipo_contenido):
        """Cambia el contenido del área principal"""
        # Limpiar contenido anterior
        self.contenido_dinamico.clear_widgets()
        
        # Crear nuevo contenido según el tipo
        if tipo_contenido == 'agregar_evento':
            nuevo_contenido = Ver_Eventos()
        elif tipo_contenido == 'eventos_importantes':
            nuevo_contenido = Eventos_Importantes()
        elif tipo_contenido == 'buscar_hueco':
            nuevo_contenido = Buscar_Hueco()
        elif tipo_contenido == 'ver_eventos':
            nuevo_contenido = Ver_Eventos()
        else:
            nuevo_contenido = Label(text='Contenido no encontrado')
        
        # Agregar el nuevo contenido
        self.contenido_dinamico.add_widget(nuevo_contenido)

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

if __name__ == '__main__':
    Myapp().run()