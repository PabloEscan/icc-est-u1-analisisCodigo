from metodos_ordenamiento import MetodosOrdenamiento
import random
import time

class Benchmarking:

    #Constructor
    def __init__(self):
        print("Benchmarking instanciado")
        self.mO = MetodosOrdenamiento()

        arreglo = self.build_arreglo(10000)
        
        #lambda en base es ()->
        #Burbuja
        tarea_burbuja = lambda: self.mO.sort_burbble(arreglo)

        current_miles = self.contar_con_current_time_milles(tarea_burbuja)
        nano_times = self.contar_con_nano_time(tarea_burbuja)

        print(f"Tiempo con mili segundos (bubble sort): {current_miles}")
        print(f"Tiempo con nano segundos (bubble sort): {nano_times}")

        #Burbuja mejorado
        tarea_burbuja_mejorado = lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo)

        current_miles = self.contar_con_current_time_milles(tarea_burbuja_mejorado)
        nano_times = self.contar_con_nano_time(tarea_burbuja_mejorado)

        print(f"Tiempo con mili segundos (bubble sort mejorado): {current_miles}")
        print(f"Tiempo con nano segundos (bubble sort mejorado): {nano_times}")

        #Seleccion
        tarea_seleccion = lambda: self.mO.sort_seleccion(arreglo)

        current_miles = self.contar_con_current_time_milles(tarea_seleccion)
        nano_times = self.contar_con_nano_time(tarea_seleccion)

        print(f"Tiempo con mili segundos (selection sort): {current_miles}")
        print(f"Tiempo con nano segundos (selection sort): {nano_times}")


    def build_arreglo(self, tamano):
        arreglo = []
        for _ in range(tamano):
            numero = random.randrange(0, 99999)
            arreglo.append(numero)
        return arreglo

    def contar_con_current_time_milles(self, tarea):
        inicial = time.time()
        tarea()
        final = time.time()
        return (final - inicial)
        
    def contar_con_nano_time(self, tarea):
        inicial = time.time_ns()
        tarea()
        final = time.time_ns()
        return (final - inicial)/1_000_000_000.0