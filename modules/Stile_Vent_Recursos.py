'''
En este archivo es donde se crea el estilo de los elementos de las ventanas para seleccionar recursos,
esta compuesto en su totalidad en lenguaje kv y forma parte solamente de el diseño de la interfaz grafica
'''

kv3 = '''
<informacion>:
    markup: True
    font_size: 20       
    text_size: 460,170
    size_hint: None,None
    valign: 'top'
    size: 480,202
            
<filas>:
    size_hint: None,None
    padding: 0,0

    canvas.before:
        Color: 
            rgba: 0,0,0,0.3
        Rectangle:
            pos: self.pos
            size: self.size

<Lbl_img>:
    size_hint: None,None
    size: 180,180
    pos_hint: {"center_x": 0.5,"center_y": 0.5}

<BotonHerramientas>:
    source: "Imagenes/Boton_Recurso.png"
    size_hint: None,None
    size: 150,120
    pos: 790,240

<menu>:
    size_hint: None,None
    size: 725,768
    pos: 100,290
    orientation: "vertical"
    index:0

    canvas.before:
        Color:
            rgba: 0.2,0,0.55,0.1
        Rectangle:
            pos: self.pos
            size: self.size

<botonSalir>:
    source: "Imagenes/Cancelar.png"
    size_hint: None,None
    size: 250,90
    pos: 620,60

<informacion_personaje>:
    size_hint: None,None 
    size: 700,210   

    canvas.before:
        Color: 
            rgba: 0,0,0,0.3
        Rectangle:
            pos: self.pos
            size: self.size

<Contenedor_Recursos>:
    size_hint: None,None
    size: 725,768
    padding: 20,0
    orientation: "vertical"

    canvas.before:
        Color: 
            rgba: 0.2,0,0.8,0.1,
        Rectangle:
            pos: self.pos
            size: self.size

<vent_cant>:
    orientation: "vertical"
    size_hint: None,None
    size: 225,85
    padding: 200,0

    canvas.before:
        Color:
            rgba: 0,0,0,0
        Rectangle:
            pos: self.pos
            size: self.size
    
'''