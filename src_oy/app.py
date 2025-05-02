import bench_marking as bm;
from metodos_ordenamiento import MetodosOrdenamiento

#Archivo principal o main
if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodosOrdenamiento()

    #tam = 10000
    tamanios = [5000, 10000, 10500]
    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)

        metodos_dic =  {
            "burbuja":metodosO.sort_burbble,
            "burbuja mejorado":metodosO.sort_burbuja_mejorado_optimizado,
            "seleccion":metodosO.sort_seleccion,
            "shell":metodosO.sort_shell,

        }

        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)


    
    for tamaño, nombre, tiempo in resultados:
        # Formateado a tiempo:.6f 6 decimales
        print(f"tamaño: {tamaño}, metodo: {nombre}, tiempo: {tiempo:.6f} segundos")
