from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox

class FormularioApp(App):
    def build(self):
        self.datos = {}  # Diccionario para almacenar los datos
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # TextInputs
        self.nombre_input = TextInput(hint_text='Nombre', multiline=False)
        self.email_input = TextInput(hint_text='Email', multiline=False)
        
        # Botones de opción (ToggleButtons)
        opciones_layout = BoxLayout(orientation='horizontal')
        self.opcion1 = ToggleButton(text='Opción 1', group='opciones')
        self.opcion2 = ToggleButton(text='Opción 2', group='opciones')
        self.opcion3 = ToggleButton(text='Opción 3', group='opciones')
        
        # Slider
        self.slider = Slider(min=0, max=100, value=50)
        self.slider_label = Label(text=f'Valor: {self.slider.value}')
        
        # Checkbox
        checkbox_layout = BoxLayout(orientation='horizontal')
        self.checkbox = CheckBox()
        checkbox_layout.add_widget(Label(text='Aceptar términos'))
        checkbox_layout.add_widget(self.checkbox)
        
        # Botón para recoger datos
        btn_recoger = Button(text='Recoger Datos', size_hint_y=None, height=50)
        btn_recoger.bind(on_press=self.recoger_datos)
        
        # Agregar widgets al layout
        layout.add_widget(Label(text='Formulario de Datos'))
        layout.add_widget(self.nombre_input)
        layout.add_widget(self.email_input)
        
        layout.add_widget(Label(text='Selecciona una opción:'))
        opciones_layout.add_widget(self.opcion1)
        opciones_layout.add_widget(self.opcion2)
        opciones_layout.add_widget(self.opcion3)
        layout.add_widget(opciones_layout)
        
        layout.add_widget(Label(text='Selecciona un valor:'))
        layout.add_widget(self.slider)
        layout.add_widget(self.slider_label)
        
        layout.add_widget(checkbox_layout)
        layout.add_widget(btn_recoger)
        
        # Actualizar label del slider
        self.slider.bind(value=self.actualizar_slider_label)
        
        return layout
    
    def actualizar_slider_label(self, instance, value):
        self.slider_label.text = f'Valor: {value:.1f}'
    
    def recoger_datos(self, instance):
        # Recoger datos de TextInputs
        self.datos['nombre'] = self.nombre_input.text
        self.datos['email'] = self.email_input.text
        
        # Recoger opción seleccionada
        opciones = [self.opcion1, self.opcion2, self.opcion3]
        for opcion in opciones:
            if opcion.state == 'down':
                self.datos['opcion'] = opcion.text
                break
        
        # Recoger valor del slider
        self.datos['valor_slider'] = self.slider.value
        
        # Recoger estado del checkbox
        self.datos['acepta_terminos'] = self.checkbox.active
        
        # Mostrar datos en consola
        print("Datos recogidos:")
        for clave, valor in self.datos.items():
            print(f"{clave}: {valor}")

if __name__ == '__main__':
    FormularioApp().run()