from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class BotonPersonal(Button):
        def __init__(self):
            super().__init__()
            text= "Personal"



class SelectorToggle(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opciones_seleccionadas = []
    
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        boton = Button(
            text='Seleccionar Preferencias',
            size_hint=(None, None),
            size=(280, 60),
            pos_hint={'center_x': 0.5}
        )
        boton.bind(on_press=self.mostrar_selector)
        
        self.label_resultado = Label(
            text='Preferencias: Ninguna seleccionada',
            text_size=(400, None),
            halign='center'
        )
        
        layout.add_widget(boton)
        layout.add_widget(self.label_resultado)
        return layout
    
    def mostrar_selector(self, instance):
        contenido = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # Título
        titulo = Label(
            text='Selecciona tus preferencias:',
            size_hint_y=None,
            height=40,
            font_size='16sp'
        )
        contenido.add_widget(titulo)
        
        # Grid de botones toggle
        grid = GridLayout(cols=2, spacing=10, size_hint_y=0.7)
        
        opciones = [
            'Deportes', 'Música', 'Cine', 'Lectura',
            'Viajes', 'Tecnología', 'Cocina', 'Arte'
        ]
        
        self.botones_toggle = []
        for opcion in opciones:
            btn = ToggleButton(
                text=opcion,
                group=None,  # Sin grupo para selección múltiple
                state='down' if opcion in self.opciones_seleccionadas else 'normal'
            )
            btn.opcion = opcion
            self.botones_toggle.append(btn)
            grid.add_widget(btn)
        
        contenido.add_widget(grid)
        for b in self.botones_toggle:
            print(b.state)

        # Botones de acción
        botones_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        boton_aceptar = Button(text='Aceptar', background_color=(0, 0.7, 0, 1))
        boton_limpiar = Button(text='Limpiar', background_color=(0.9, 0.6, 0, 1))
        boton_cancelar = Button(text='Cancelar')
        
        botones_layout.add_widget(boton_aceptar)
        botones_layout.add_widget(boton_limpiar)
        botones_layout.add_widget(boton_cancelar)
        contenido.add_widget(botones_layout)
        
        # Crear popup
        self.popup = Popup(
            title='Mis Preferencias',
            content=contenido,
            size_hint=(None, None),
            size=(400, 500)
        )
        print()
        
        # Vincular eventos
        boton_aceptar.bind(on_press=self.guardar_seleccion)
        boton_limpiar.bind(on_press=self.limpiar_seleccion)
        boton_cancelar.bind(on_press=self.popup.dismiss)
        
        self.popup.open()
    
        print(self.opciones_seleccionadas)

    def guardar_seleccion(self, instance):
        self.opciones_seleccionadas = [
            btn.opcion for btn in self.botones_toggle if btn.state == 'down'
        ]
        
        self.actualizar_resultado()
        self.popup.dismiss()
    
    def limpiar_seleccion(self, instance):
        for btn in self.botones_toggle:
            btn.state = 'normal'
    
    def actualizar_resultado(self):
        if self.opciones_seleccionadas:
            texto = f'Preferencias: {", ".join(self.opciones_seleccionadas)}'
        else:
            texto = 'Preferencias: Ninguna seleccionada'
        
        self.label_resultado.text = texto

if __name__ == '__main__':
    SelectorToggle().run()