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
from modules.Stile_principal import kv
from modules.Stile_vent_Agregar_Evento import kv2
from modules.Imagenes import*
from modules.Backend1 import*
from modules.Stile_Vent_Recursos import*
from modules.Stile_Vent_Ver_Eventos import*
from modules.Class_vent_Agregar_Evento import *
from modules.Class_Vent_Recursos import *
from modules.Class_Vent_Ver_Eventos import *
from kivy.config import Config