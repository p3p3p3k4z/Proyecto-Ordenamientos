import matplotlib.pyplot as plt
from conteo import *

ordenamientos = {
    'bubble': bubble_sort,
    'insertion': insertion_sort,
    'selection': selection_sort,
    'merge': merge_sort,
    'quick': quick_sort,
  #  'bogo': bogo_sort,
    'heap': heap_sort,
    'radix': radix_sort
}

def obtener_num_llamadas(algoritmo, lista):
    return algoritmo(lista.copy())

def graficar_llamadas(llamadas_por_algoritmo, nombres_algoritmos):
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    plt.barh(nombres_algoritmos, llamadas_por_algoritmo, color='purple')
    for index, value in enumerate(llamadas_por_algoritmo):
        plt.text(value, index, f'{value:.2f}')
    plt.xlabel('Número total de llamadas')
    plt.title('Número total de llamadas de algoritmos de ordenamiento')
    plt.show()

def grafLlamadas(lista):
    nombres_algoritmos = list(ordenamientos.keys())
    llamadas_por_algoritmo = []

    for nombre in nombres_algoritmos:
        algoritmo = ordenamientos[nombre]
        num_llamadas = obtener_num_llamadas(algoritmo, lista)
        llamadas_por_algoritmo.append(num_llamadas)
    
    graficar_llamadas(llamadas_por_algoritmo, nombres_algoritmos)