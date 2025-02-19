import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ordersGraf import *

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

def CrearGrafica(frames, title):
    plt.style.use('dark_background')

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(frames[0])), frames[0], align="edge", color='purple')

    ax.set_xlim(0, len(frames[0]))
    ax.set_ylim(0, int(1.1 * max(max(frames))))

    text = [ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), f'{rect.get_height():.0f}', ha='center', va='bottom', color='white') for rect in bar_rects]

    def init():
        for rect, val, txt in zip(bar_rects, frames[0], text):
            rect.set_height(val)
            txt.set_text(f'{val:.0f}')
            txt.set_y(val)
        return (*bar_rects, *text)

    def update(frame):
        for rect, val, txt in zip(bar_rects, frame, text):
            rect.set_height(val)
            txt.set_text(f'{val:.0f}')
            txt.set_y(val)
        return (*bar_rects, *text)

    ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=100, repeat=False)

    plt.title(title)
    plt.show()

def Graficar(arr, nombre_ord):
    frames = ordenamientos[nombre_ord](arr.copy())
    CrearGrafica(frames, title= "Ordenamiento "+f"{nombre_ord.capitalize()}")