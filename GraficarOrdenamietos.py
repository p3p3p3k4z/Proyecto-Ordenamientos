import time
import matplotlib.pyplot as plt
import cProfile
import pstats
import io
from orders import *

ordenamientos = {
    'bubble': bubble_sort,
    'insertion': insertion_sort,
    'selection': selection_sort,
    'merge': merge_sort,
    'quick': quick_sort,
    #'bogo': bogo_sort,
    'heap': heap_sort,
    'radix': radix_sort
}

def tiempo_y_llamadas_ejecucion(algoritmo, lista):
    pr = cProfile.Profile()
    pr.enable()
    inicio = time.time()
    algoritmo(lista)
    fin = time.time()
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('calls')
    ps.print_stats()
    
    numero_llamadas = 0
    for line in s.getvalue().splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0].isdigit():
            try:
                numero_llamadas += int(parts[0])
            except ValueError:
                pass

    return fin - inicio, numero_llamadas

def graficar_tiempos_pastel(tiempos, nombres_algoritmos):
    labels = [f"{nombres_algoritmos[i]} ({tiempos[i]:.6f} s)" for i in range(len(nombres_algoritmos))]
    plt.figure(figsize=(10, 6))
    plt.pie(tiempos, labels=labels, autopct='%1.2f%%', startangle=140)
    plt.title('Distribución de tiempos de ejecución de algoritmos de ordenamiento')
    plt.axis('equal')  
    plt.show()

def graficar_llamadas_bar(llamadas, nombres_algoritmos):
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    plt.bar(nombres_algoritmos, llamadas, color='purple')
    plt.xlabel('Algoritmo de ordenamiento')
    plt.ylabel('Número de llamadas')
    plt.title('Número de llamadas de funciones en algoritmos de ordenamiento')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def GraficarOrds(lista):
    tiempos = []
    llamadas = []
    nombres_algoritmos = list(ordenamientos.keys())

    for nombre, algoritmo in ordenamientos.items():
        tiempo, num_llamadas = tiempo_y_llamadas_ejecucion(algoritmo, lista.copy())  # Copia de la lista para evitar cambios permanentes
        tiempos.append(tiempo)
        llamadas.append(num_llamadas)

    graficar_llamadas_bar(llamadas, nombres_algoritmos)
    
def GraficarOrds_time(lista):
    tiempos = []
    llamadas = []
    nombres_algoritmos = list(ordenamientos.keys())

    for nombre, algoritmo in ordenamientos.items():
        tiempo, num_llamadas = tiempo_y_llamadas_ejecucion(algoritmo, lista.copy())  # Copia de la lista para evitar cambios permanentes
        tiempos.append(tiempo)
        llamadas.append(num_llamadas)
    
    graficar_tiempos_pastel(tiempos, nombres_algoritmos)
