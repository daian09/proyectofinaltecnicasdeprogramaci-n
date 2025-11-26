import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def Visualizar():
    New_Reg = tk.Toplevel()
    New_Reg.title("Graficas")
    New_Reg.geometry("600x600")
    New_Reg.resizable(False, False)

    def volver():
        New_Reg.destroy()

    # Crear la figura y los ejes de Matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111) # Crea un único subplot

    # Generar y dibujar la gráfica (ejemplo con una función seno)
    x = [i * 0.1 for i in range(100)]
    y = [i * 0.1 for i in range(100)]
    ax.plot(x, y)
    ax.set_title("Gráfico de línea de ejemplo")

    # Integrar el gráfico en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas_widget = canvas.get_tk_widget()

    text1 = tk.Label(New_Reg, text="Seleccione una estadistica para visualizar")

    # === Crear un frame para el gráfico ===
    frame_grafica = tk.Frame(New_Reg)
    frame_grafica.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    btn1 = tk.Button(New_Reg, text="Grafica 1", width=20, height=3)
    btn2 = tk.Button(New_Reg, text="Grafica 2", width=20, height=3)
    btn3 = tk.Button(New_Reg, text="Grafica 3", width=20, height=3)
    botonSalir = tk.Button(New_Reg, text="Volver al menu\n principal", width=20, height=3, command=volver)

    text1.grid(row=0, column=1, padx=10, pady=10)

    btn1.grid(row=1, column=0, padx=10, pady=10)
    btn2.grid(row=1, column=1, padx=10, pady=10)
    btn3.grid(row=1, column=2, padx=10, pady=10)
    botonSalir.grid(row=2, column=1, padx=10, pady=10)