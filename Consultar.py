import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd

def Consultar_Registro():
    New_Reg = tk.Toplevel()
    New_Reg.title("Consultar registro")
    New_Reg.geometry("500x500")
    New_Reg.resizable(False, False)

    # cargar base de datos
    try:
        df = pd.read_excel("base_datos_salud_procesada.xlsx")
    except:
        messagebox.showerror("Error", "No se pudo cargar la base de datos.")
        return

    # cargar imagen
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ruta_imagen = os.path.join(BASE_DIR, "busqueda-de-lupa.png")

        img_original = Image.open(ruta_imagen)
        img_redimensionada = img_original.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img_redimensionada)

        imagen = tk.Label(New_Reg, image=img_tk)
        imagen.image = img_tk
        imagen.pack(pady=5)

    except:
        tk.Label(New_Reg, text="No se encontró la imagen").pack(pady=5)

    # elementos de búsqueda
    tk.Label(New_Reg, text="Escriba País o ISO:", font=("Arial", 11)).pack(pady=5)
    entry_busqueda = tk.Entry(New_Reg, width=40)
    entry_busqueda.pack(pady=5)

    # listbox para mostrar resultados
    lista = tk.Listbox(New_Reg, width=50, height=10)
    lista.pack(pady=10)

    # label para mostrar información detallada
    info = tk.Label(New_Reg, text="", justify="left", anchor="w", font=("Arial", 10))
    info.pack(pady=10)

    # función para actualizar la lista de resultados
    def actualizar_lista(event=None):
        lista.delete(0, tk.END)
        texto = entry_busqueda.get().strip()

        if texto == "":
            return

        resultados = df[
            (df["Country"].str.contains(texto, case=False, na=False)) |
            (df["ISO_Code"].str.contains(texto, case=False, na=False))
        ]

        for i, row in resultados.iterrows():
            lista.insert(tk.END, f"{row['Country']} ({row['ISO_Code']}) - Año {row['Year']}")

    # Actualizar lista automáticamente al escribir
    entry_busqueda.bind("<KeyRelease>", actualizar_lista)

    #mostrar detalle del registro seleccionado
    def mostrar_detalle(event=None):
        seleccion = lista.curselection()
        if not seleccion:
            return

        texto = lista.get(seleccion[0])

        # Extraer ISO o país de la cadena seleccionada
        iso = texto.split("(")[1].split(")")[0]

        registro = df[df["ISO_Code"] == iso].iloc[0]

        texto_info = (
            f"País: {registro['Country']}\n"
            f"ISO: {registro['ISO_Code']}\n"
            f"Año: {registro['Year']}\n"
            f"Reformas: {registro['Health_Reforms']}\n"
            f"Clase de gasto: {registro['Expenditure_Class']}\n"
            f"Gasto capital: {registro['Capital']}\n"
            f"% PIB Salud: {registro['Health_Expenditure_GDP_%']}\n"
            f"Gasto bolsillo: {registro['Out_of_Pocket_%']}\n"
            f"Expectativa de vida: {registro['Objective_Life_Expectancy']}\n"
        )
        info.config(text=texto_info)

    # Evento al seleccionar en la lista
    lista.bind("<<ListboxSelect>>", mostrar_detalle)

    # botón para volver 
    tk.Button(New_Reg, text="Volver al menú principal", width=30, command=New_Reg.destroy)\
        .pack(pady=15)

