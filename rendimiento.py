import cProfile
import pstats
import io
import tkinter as tk
from tkinter import scrolledtext

from orders import *

ordenamientos = {
    'bubble': bubble_sort,
    'insertion': insertion_sort,
    'selection': selection_sort,
    'merge': merge_sort,
    'quick': quick_sort,
    'bogo': bogo_sort,
    'heap': heap_sort,
    'radix': radix_sort
}

def mostrar_perfil(arr,ordenamiento):
    if ordenamiento not in ordenamientos:
        print("El algoritmo de ordenamiento especificado no está disponible.")
        return

    funcion_ordenamiento = ordenamientos[ordenamiento]

    pr = cProfile.Profile()
    pr.enable()
    funcion_ordenamiento(arr.copy())
    pr.disable()

    # Crear un flujo de salida
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    # Crear la ventana de Tkinter
    root = tk.Tk()
    root.title("cProfile")

    # Crear un widget de texto con desplazamiento
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Insertar el texto del perfil en el widget de texto
    text_area.insert(tk.END, s.getvalue())

    # Deshabilitar la edición del widget de texto
    text_area.config(state=tk.DISABLED)

    # Ejecutar la ventana de Tkinter
    root.mainloop()