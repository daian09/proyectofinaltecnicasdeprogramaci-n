import tkinter as tk
from PIL import Image, ImageTk
import os
import AddRegistro
import Consultar
import Graficas
import Filtrar

#Funciones de los botones
def Boton1():
    AddRegistro.Add_Registro()

def Boton2():
    Consultar.Consultar_Registro()
    
def Boton3():
    Filtrar.Filtrar_Registros()

def Boton4():
    Graficas.Visualizar()

# Ventana principal
root = tk.Tk()
root.title("Analisis de gastos en salud")
root.geometry("500x400")
root.resizable(False, False) #con esto se bloquea la posibilidad de maximizar la ventana
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(BASE_DIR, "salud-financiera.png")
    # Imagen de la ventana principal
    img_original = Image.open(ruta_imagen)
    img_redimensionada = img_original.resize((200, 200)) # Nuevo tamaño de la imagen
    img_tk = ImageTk.PhotoImage(img_redimensionada)

    # Crear una etiqueta para mostrar la imagen
    imagen = tk.Label(root, image=img_tk)
    # Guardar referencia a la imagen
    imagen.image = img_tk
    # Empaquetar la etiqueta para que sea visible
    imagen.pack(padx=5, pady=5)

except FileNotFoundError:
    error_label = tk.Label(root, text="No se encontró la imagen")
    error_label.pack(padx=5, pady=5)

# Marco para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=20)

# Botones
btn1 = tk.Button(frame_botones, text="Añadir Registro", width=20, height=3, command=Boton1)
btn2 = tk.Button(frame_botones, text="Consultar registro", width=20, height=3, command=Boton2)
btn3 = tk.Button(frame_botones, text="Filtrar datos por categorías", width=20, height=3, command=Boton3)
btn4 = tk.Button(frame_botones, text="Visualización de estadísticas", width=20, height=3, command=Boton4)

# Ubicación automática en cuadrícula (2x2)
btn1.grid(row=0, column=0, padx=10, pady=10)
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3.grid(row=1, column=0, padx=10, pady=10)
btn4.grid(row=1, column=1, padx=10, pady=10)

# Expandir columnas para que la cuadrícula quede proporcionada
frame_botones.grid_columnconfigure(0, weight=1)
frame_botones.grid_columnconfigure(1, weight=1)

# Ejecutar la aplicación
root.mainloop()