from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock


class Item_event(ButtonBehavior,BoxLayout):
    def __init__(self,nombre,info,hora):
        super().__init__()
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

