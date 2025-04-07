import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
archivo_csv = 'Ventas.csv'  # Reemplaza con la ruta de tu archivo
datos = pd.read_csv(archivo_csv)

# Calcular máximos, mínimos y promedios por producto
resultados = datos.groupby('Producto').agg(
    Cantidad_Maxima=('Cantidad', 'max'),
    Cantidad_Minima=('Cantidad', 'min'),
    Cantidad_Promedio=('Cantidad', 'mean'),
    Valor_Maximo=('Venta_Total', 'max'),
    Valor_Minimo=('Venta_Total', 'min'),
    Valor_Promedio=('Venta_Total', 'mean')
).reset_index()

# Mostrar resultados
print(resultados)


#Creamos archivo
resultados.to_csv('Estadisticas_Salida.csv', index=False)

# Graficar los resultados
ax = resultados.set_index('Producto')[['Cantidad_Maxima', 'Cantidad_Minima', 'Cantidad_Promedio']].plot(kind='bar')
plt.title('Estadísticas de Ventas por Producto')
plt.ylabel('Cantidad')
plt.xlabel('Producto')
plt.xticks(rotation=45)
plt.legend(title='Estadística')
plt.tight_layout()
plt.show()

resultados.set_index('Producto')[['Valor_Maximo', 'Valor_Minimo', 'Valor_Promedio']].plot(kind='bar')
plt.title('Estadísticas de Ventas por Producto')
plt.ylabel('Valor')
plt.xlabel('Producto')
plt.xticks(rotation=45)
plt.legend(title='Estadística')
plt.tight_layout()
plt.show()