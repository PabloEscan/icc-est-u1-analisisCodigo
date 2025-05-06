import bench_marking as bm;
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict


#Archivo principal o main
if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodosOrdenamiento()

    #tam = 10000
    tamanios = [0, 1000, 1500]
    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)

        metodos_dic =  {
            "Burbuja":metodosO.sort_burbble,
            "Burbuja_mejorado":metodosO.sort_burbuja_mejorado_optimizado,
            "Seleccion":metodosO.sort_seleccion,
            "Shell":metodosO.sort_shell,

        }

        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)


    
    for tamaño, nombre, tiempo in resultados:
        # Formateado a tiempo:.6f 6 decimales
        print(f"tamaño: {tamaño}, metodo: {nombre}, tiempo: {tiempo:.6f} segundos")

    #Preparar datos para ser graficados
    # 1 crear un diccionario o map para almacenar resultados por metodos
    tiempos_by_metodo ={
        "Burbuja": [],
        "Burbuja_mejorado": [],
        "Seleccion": [],
        "Shell": [],
    }

    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    plt.figure(figsize=(10,6))

    # Graficar los tiempos de ejecicion para cada metodo
    for nombre, tiempo in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempo, label= nombre, marker= "o")
    

# Datos del segundo gráfico
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Datos personalizados
fecha_actual = datetime.now().strftime("%d/%m/%Y")
mi_nombre = "Pablo Escandón" 
encabezado= f"{mi_nombre} - {fecha_actual}"


fig, axs = plt.subplots(1, 2, figsize=(10, 10))
fig.canvas.manager.set_window_title(f"{mi_nombre}-{fecha_actual}")
fig.suptitle(encabezado, fontsize=14, fontweight='bold')


for nombre, tiempo in tiempos_by_metodo.items():
    axs[0].plot(tamanios, tiempo, label=nombre, marker="o")

axs[0].set_title("Comparación de tiempos")
axs[0].set_xlabel("Tamaño de los arreglos")
axs[0].set_ylabel("Tiempo de ejecución (segundos)")
axs[0].legend()

axs[1].plot(x, y, label="Línea", color="blue")
axs[1].set_title("Mi primer gráfico")
axs[1].set_xlabel("Eje de la X")
axs[1].set_ylabel("Eje de la Y")
axs[1].legend()

plt.tight_layout()
plt.show()