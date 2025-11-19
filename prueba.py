#Repositorio
#https://github.com/JacoboCuartas/DesafioU 

import pandas as pd
import os

# Obtener la ruta del archivo actual (donde está este script)
base_dir = os.path.dirname(__file__)

# Construir las rutas relativas
file_path = os.path.join(base_dir, "base_datos_salud.xlsx")
output_path = os.path.join(base_dir, "base_datos_salud_procesada.xlsx")

# Cargar datos
data = pd.read_excel(file_path, sheet_name="Sheet1")

# Promedio y desviación estándar de la columna "Capital"
promedio_capital = data["Capital"].mean()
desviacion_capital = data["Capital"].std()

print("Promedio de Capital:", promedio_capital)
print("Desviación estándar de Capital:", desviacion_capital)

# Cantidad de casos por clase de gasto
casos_por_clase = data["Expenditure_Class"].value_counts()
print("\nCantidad de casos por clase de gasto:")
print(casos_por_clase)

# Guardar el DataFrame en un nuevo archivo Excel
data.to_excel(output_path, index=False)

#filtro por año y promedio de gasto y esperanza de vida por país en ese rango
# Definir rango de años
inicio = 2010
fin = 2020

# Filtrar datos en ese rango
data_filtrada = data[(data["Year"] >= inicio) & (data["Year"] <= fin)]

# Calcular el promedio de gasto (Capital) y esperanza de vida por país
data_promedio = (
    data_filtrada.groupby("Country")[["Capital", "Objective_Life_Expectancy"]]
    .mean()
    .reset_index()
)

print(f"\nPromedio de gasto y esperanza de vida entre {inicio} y {fin}:")
print(data_promedio.head())

# filtro avanzado: países con gasto en salud per cápita superior al promedio
gasto_promedio = data_promedio["Capital"].mean()
paises_mayor_gasto = data_promedio[data_promedio["Capital"] > gasto_promedio]
paises_mayor_gasto = paises_mayor_gasto.sort_values(by="Capital", ascending=False)

print("\nPaíses con gasto en salud per cápita superior al promedio (promedio 2010–2020):")
print(paises_mayor_gasto[["Country", "Capital", "Objective_Life_Expectancy"]])

#visalización de datos
import matplotlib.pyplot as plt

# Histograma del gasto en salud per cápita promedio
plt.figure(figsize=(8, 5))
plt.hist(data_promedio["Capital"], bins=10, edgecolor='black')
plt.title(f"Distribución del gasto en salud per cápita ({inicio}-{fin})")
plt.xlabel("Gasto en salud per cápita (Capital promedio)")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de barras: gasto promedio por país
plt.figure(figsize=(10, 5))
plt.bar(data_promedio["Country"], data_promedio["Capital"], color='skyblue')
plt.title(f"Gasto promedio en salud per cápita por país ({inicio}-{fin})")
plt.xlabel("País")
plt.ylabel("Gasto promedio en salud per cápita")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Gráfico de dispersión: relación gasto promedio vs esperanza de vida promedio
plt.figure(figsize=(8, 5))
plt.scatter(data_promedio["Capital"], data_promedio["Objective_Life_Expectancy"], color='green')
plt.title(f"Relación entre gasto promedio en salud y esperanza de vida ({inicio}-{fin})")
plt.xlabel("Gasto en salud per cápita (promedio)")
plt.ylabel("Esperanza de vida (promedio)")
plt.show()

# Análisis de correlación
correlacion = data_promedio["Capital"].corr(data_promedio["Objective_Life_Expectancy"])
print(f"\nCoeficiente de correlación entre gasto y esperanza de vida ({inicio}-{fin}): {correlacion:.3f}")

if correlacion > 0.5:
    print("Existe una correlación positiva: a mayor gasto en salud, mayor esperanza de vida.")
elif correlacion < -0.5:
    print("Existe una correlación negativa: a mayor gasto en salud, menor esperanza de vida.")
else:
    print(" No hay una correlación fuerte entre ambas variables.")

# Guardar el archivo con los países de mayor gasto
filtro_output = os.path.join(base_dir, f"paises_mayor_gasto_{inicio}_{fin}.xlsx")
paises_mayor_gasto.to_excel(filtro_output, index=False)
print(f"\nArchivo con países de mayor gasto promedio guardado en: {filtro_output}")
