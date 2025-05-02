class MetodosOrdenamiento:

    def sort_burbble(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range(n):
            for j in range(i+1, n):
                if arreglo[j] < arreglo[i]:
                    #Doble asignacion en una linea
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

        return arreglo
    
    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range(n):
            intercambiado = False
            for j in range(0, n-1-i):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                    intercambiado = True
                if not intercambiado:
                    break
        return arreglo

    
    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range(0, n-1):
            iM = i
            
            for j in range(i-1, n):
                if arreglo[j] < arreglo[iM]:
                    iM = j

            if i != iM:
                arreglo[i], arreglo[iM] = arreglo[iM], arreglo[i]
        return arreglo

    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo
