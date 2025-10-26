import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Gestor de eventos")
        self.app.geometry("1000x950")
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(0,weight=0)
        self.app.resizable(False, False)


        # Frame principal que contendrá todo
        self.main_container = ctk.CTkFrame(self.app)
        self.main_container.pack(fill="both", expand=True)
        self.main_container.configure(fg_color="#0b0e2b")
        
        # Frame para el menú principal (siempre visible)
        self.menu_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.menu_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Frame para contenido dinámico (se superpone)
        self.content_frame = None
        
        self.crear_menu_principal()

    def crear_menu_principal(self):
        # Limpiar frame de contenido si existe
        if self.content_frame:
            self.content_frame.destroy()
            self.content_frame = None
        
        # Mostrar el menú principal
        self.menu_frame.lift()
        
        # Título
        texto = ctk.CTkLabel(
            self.menu_frame, 
            text="Observatorio Astronomico",
            font=("Arial", 56),
            text_color="white"
        )
        texto.grid(row=0, column=0, columnspan=2, padx=20, pady=100)
        
        # Botón 1 - Agregar evento
        boton1 = ctk.CTkButton(
            self.menu_frame, 
            text="➕ Agregar evento",
            width=320,
            height=120,
            font=("Arial", 26),
            fg_color="#472AE8",
            border_color='white',
            border_width=2,
            command=self.mostrar_agregar_evento
        )
        boton1.grid(row=1, column=0, padx=20, pady=20)
        
        # Botón 2 - Box ejercicios
        boton2 = ctk.CTkButton(
            self.menu_frame, 
            text=" 🗓️ Ver eventos",
            width=320,
            height=120,
            font=("Arial", 26),
            fg_color="#472AE8",
            border_color='white',
            border_width=2,
            command=self.mostrar_eventos
        )
        boton2.grid(row=1, column=1, padx=20, pady=20)
        
        # Botón 3 - Buscar horarios libres
        boton3 = ctk.CTkButton(
            self.menu_frame, 
            text="🔍 Buscar horarios libres",
            width=320,
            height=120,
            font=("Arial", 25),
            fg_color="#472AE8",
            border_color='white',
            border_width=2,
            command=self.mostrar_buscar_horarios
        )
        boton3.grid(row=2, column=0, padx=20, pady=20)
        
        # Botón 4 - Eventos especiales
        boton4 = ctk.CTkButton(
            self.menu_frame, 
            text="⭐ Eventos especiales",
            width=320,
            height=120,
            font=("Arial", 26),
            border_width=2,
            border_color='white',
            fg_color="#472AE8",
            command=self.mostrar_eventos_especiales
        )
        boton4.grid(row=2, column=1, padx=20, pady=20)
    
    def crear_frame_contenido(self, titulo):
        """Crea un frame de contenido superpuesto"""
        if self.content_frame:
            self.content_frame.destroy()
        
        # Crear frame de contenido (se superpone sobre el fondo)
        self.content_frame = ctk.CTkFrame(
            self.main_container, 
            width=1900, 
            height=1700,
            fg_color="white"
        )
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.content_frame.lift()  # Traer al frente
        
        # Header con título y botón volver
        header_frame = ctk.CTkFrame(self.content_frame, fg_color="#2b2b2b", height=80)
        header_frame.pack(side="top",fill="x", padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        # Botón volver
        btn_volver = ctk.CTkButton(
            header_frame,
            text="⬅️ Volver al Menú",
            command=self.crear_menu_principal,
            width=120,
            height=40,
            fg_color="#472AE8"
        )
        btn_volver.pack(side="left", padx=20, pady=20)
        
        # Título
        lbl_titulo = ctk.CTkLabel(
            header_frame,
            text=titulo,
            font=("Arial", 28, "bold"),
            text_color="white"
        )
        lbl_titulo.pack(side="left", padx=20, pady=2)
        
        return self.content_frame
    
    def mostrar_agregar_evento(self):
        content_frame = self.crear_frame_contenido("➕ Agregar Nuevo Evento")
        
        # Contenido del formulario
        form_frame = ctk.CTkFrame(content_frame, fg_color="white")
        form_frame.pack(side="top", expand=True, padx=30, pady=15,)
        


        # Campos del formulario
        formulario = [
            ("Nombre del evento: ", ctk.CTkEntry),
            ("Fecha de inicio de la forma (A-M-D-H-Min): ", ctk.CTkEntry),
            ("Duracion del evento: ", ctk.CTkEntry),
            ("Recursos necesarios: ", ctk.CTkCheckBox)
        ]
        
        for i, (texto, widget_class) in enumerate(formulario):
            label_formulario = ctk.CTkLabel(form_frame, text=texto, font=("Arial", 20), text_color="black")
            label_formulario.grid(row=i, column=0, padx=10, pady=15)
            
            if widget_class == ctk.CTkEntry:
                entrada = widget_class(form_frame, width=400, fg_color="white", text_color="black")
            else:
                entrada = widget_class(form_frame, height=80, width=400, fg_color="white", text_color="black")
            
            entrada.grid(row=i, column=1, padx=10, pady=15)
            
        # Botón guardar
        btn_guardar = ctk.CTkButton(
            form_frame,
            text="💾 Guardar Evento",
            width=200,
            height=50,
            font=("Arial", 16),
            fg_color="#472AE8"
        )
        btn_guardar.grid(row=len(formulario), column=0, columnspan=2, pady=30)
    
    def mostrar_eventos(self):
        content_frame = self.crear_frame_contenido("Eventos guardados")
        
        # Frame scrollable para ejercicios
        scroll_frame = ctk.CTkScrollableFrame(content_frame, fg_color="white")
        scroll_frame.pack(fill="both",expand=True,ipadx=180,ipady=120,pady=20,padx=20)
        
        frame_ej = ctk.CTkFrame(scroll_frame, height=80)
        frame_ej.pack(fill="x", pady=5)
        frame_ej.pack_propagate(False)
            

        eventos = []

        if len(eventos) == 0:
            btn_vacio = ctk.CTkLabel(
                frame_ej, 
                text="No se han agregado eventos", 
                font=("Arial", 30),
                text_color="Black"
            )
            btn_vacio.pack(side="left", padx=10, pady=20)
        else:
            for i, evento in enumerate(eventos):
                lbl_ej = ctk.CTkLabel(
                    frame_ej, 
                    text=evento, 
                    font=("Arial", 16),
                    text_color="black"
                )
                lbl_ej.pack(side="left", padx=20, pady=20)
    def mostrar_eventos_especiales():
        pass

    def mostrar_buscar_horarios():
        pass

    def run(self):
        self.app.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = MainApp()
    app.run()