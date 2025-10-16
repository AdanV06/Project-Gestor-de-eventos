import customtkinter 
from PIL import Image,ImageTk
import os

app = customtkinter.CTk()
app.title("Gestor de eventos")
app.geometry("1000x800")
app.grid_columnconfigure(0,weight=1)
app.resizable(False,False)

imagen = Image.open("/home/adan/Projects/Project Pro 1/Fondos/astronomia-fq9xt51j0laxfpho2.jpg")

imagen_tk = customtkinter.CTkImage(imagen,size=(1000,800))

fondo_imagen = customtkinter.CTkLabel(app,image=imagen_tk,text="")

fondo_imagen.place(x=0,y=0,relwidth=1,relheight=1)

logo_img = Image.open("/home/adan/Projects/Project Pro 1/Fondos/astronomia-fq9xt51j0laxfpho.jpg")
logo_img = logo_img.resize((900,90))
img_tk = ImageTk.PhotoImage(logo_img)

boton = customtkinter.CTkButton(app, text="Agregar evento",width=300 ,height=100,font=("Arial",25),fg_color="#472AEB",border_color='white',border_width=2)
boton.grid(row=1,column=0, padx=170, pady=0, sticky="w")
boton = customtkinter.CTkButton(app, text="Ver eventos",width=300,height=100,font=("Arial",25),fg_color="#472AEB",border_color='white',border_width=2)
boton.grid(row=1,column=0, padx=200, pady=0, sticky="e")
boton = customtkinter.CTkButton(app, text="Buscar horarios libres",width=300 ,height=100,font=("Arial",25),fg_color="#472AEB",border_color='white',border_width=2)
boton.grid(row=2,column=0, padx=170, pady=20, sticky="w")
boton = customtkinter.CTkButton(app, text="Eventos especiales",width=300,height=100,font=("Arial",25),border_width=2,border_color="white",fg_color="#472AEB")
boton.grid(row=2,column=0, padx=200, pady=20, sticky="e")


frame = customtkinter.CTkFrame(app,width=400,height=85,corner_radius=20)
frame.grid(row=0,column=0, padx=50, pady=130, sticky="ew")

label = customtkinter.CTkLabel(frame,text="",image=img_tk)
label.place(x=0,y=0,relwidth=1,relheight=1)

#texto = customtkinter.CTkLabel(app,text="Centro Astronomico Estelar",font=("Arial",50),fg_color="#173366")
#texto.grid(row=0,column=0,padx=20,pady=150)

app.mainloop()