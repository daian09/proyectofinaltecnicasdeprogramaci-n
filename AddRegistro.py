import tkinter as tk
import pandas as pd
from tkinter import messagebox

print(">>> AddRegistro cargado desde:", __file__)

def Add_Registro():
    New_Reg = tk.Toplevel()
    New_Reg.title("Añadir Registro")
    New_Reg.geometry("520x580")
    New_Reg.resizable(False, False)

    # ------------------- FUNCIÓN GUARDAR -------------------
    def guardar():
        # Capturar datos con validación básica
        try:
            new_row = {
                "Country": entry_country.get(),
                "ISO_Code": entry_iso.get(),
                "Year": int(entry_year.get()),
                "Health_Reforms": int(entry_reforms.get()),
                "Expenditure_Class": entry_expenditure.get(),
                "Capital": float(entry_capital.get()),
                "Health_Expenditure_GDP_%": float(entry_gdp.get()),
                "Out_of_Pocket_%": float(entry_pocket.get()),
                "Objective_Life_Expectancy": float(entry_life.get())
            }
        except:
            messagebox.showerror("Error", "Verifique que los campos numéricos contengan valores válidos.")
            return

        # ---------------- CONFIRMACIÓN SIMPLE ----------------
        confirmar = messagebox.askyesno(
            "Confirmar guardado",
            "¿Desea guardar este registro?"
        )

        if not confirmar:
            return

        # ---------------- GUARDAR EN EXCEL ----------------
        try:
            df = pd.read_excel("base_datos_salud_procesada.xlsx")
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_excel("base_datos_salud_procesada.xlsx", index=False)

            messagebox.showinfo("Éxito", "Registro guardado exitosamente.")
            New_Reg.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el registro:\n{e}")

    # ------------------- LABELS Y ENTRADAS -------------------
    labels_es = [
        "País",
        "Código ISO (ej: COL, USA)",
        "Año (numérico)",
        "Reformas en salud (número)",
        "Clase de gasto (Alto / Medio / Bajo)",
        "Gasto de capital en salud",
        "% del PIB destinado a salud",
        "Gasto de bolsillo (%)",
        "Expectativa de vida"
    ]

    entries = []

    for i, lbl in enumerate(labels_es):
        tk.Label(New_Reg, text=lbl, anchor="w").grid(
            row=i, column=0, padx=10, pady=10, sticky="w"
        )
        entry = tk.Entry(New_Reg, width=35)
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)

    (entry_country,
     entry_iso,
     entry_year,
     entry_reforms,
     entry_expenditure,
     entry_capital,
     entry_gdp,
     entry_pocket,
     entry_life) = entries

    # ------------------- BOTONES -------------------
    tk.Button(New_Reg, text="Guardar Registro", width=20, height=2, command=guardar)\
        .grid(row=len(labels_es), column=0, padx=10, pady=20)

    tk.Button(New_Reg, text="Volver sin guardar", width=20, height=2, command=New_Reg.destroy)\
        .grid(row=len(labels_es), column=1, padx=10, pady=20)
