'''
En este archivo se tienen los estilo de los elementos de la ventana Ver Eventos 
este archivo es puramente en lenguaje kv y solo es parte puramente de el diseño de la interfaz grafica
'''
kv4 = '''
<Item_event>:
    orientation: "horizontal"
    size_hint: None,None
    size: 870,130

    canvas.before:
        Color:
            rgba: 0.3,0,0.8,0.7
        Rectangle:
            pos: self.pos
            size: self.size

<cont_event>:
    orientation: 'vertical'
    size_hint: None,None
    spacing: 8

    canvas.before:
        Color:
            rgba: 0,0,0,0
        Rectangle:
            pos: self.pos
            size: self.size

<Delete>:
    size_hint: None,None
    size: 50,50
'''