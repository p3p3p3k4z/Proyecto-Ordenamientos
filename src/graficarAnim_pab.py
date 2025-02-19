import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import heapq

# Funciones de ordenamiento
def bubble_sort_characters_steps(s):
    arr = list(s)
    steps = [arr.copy()]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
    return steps

def insertion_sort_characters_steps(s):
    arr = list(s)
    steps = [arr.copy()]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            steps.append(arr.copy())
        arr[j + 1] = key
        steps.append(arr.copy())
    return steps

def selection_sort_characters_steps(s):
    arr = list(s)
    steps = [arr.copy()]
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
    return steps

def merge_sort_characters_steps(s):
    def merge(left, right, steps):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left)
        result.extend(right)
        steps.append(result.copy())
        return result
    
    def merge_sort(arr, steps):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            left_sorted = merge_sort(arr[:mid], steps)
            right_sorted = merge_sort(arr[mid:], steps)
            return merge(left_sorted, right_sorted, steps)

    arr = list(s)
    steps = [arr.copy()]
    merge_sort(arr, steps)
    return steps

def quick_sort_characters_steps(s):
    def quick_sort(arr, steps):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            sorted_arr = quick_sort(left, steps) + middle + quick_sort(right, steps)
            steps.append(sorted_arr.copy())
            return sorted_arr
    
    arr = list(s)
    steps = [arr.copy()]
    quick_sort(arr, steps)
    return steps

def heap_sort_characters_steps(s):
    arr = list(s)
    steps = [arr.copy()]
    heapq.heapify(arr)
    steps.append(arr.copy())
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
        steps.append(sorted_arr + arr)
    return steps

# Nuevas funciones agregadas
def radix_sort_characters_steps(s):
    def counting_sort(arr, exp, steps):
        n = len(arr)
        output = [0] * n
        count = [0] * 256

        # Count occurrences of each character
        for char in arr:
            count[(ord(char) // exp) % 256] += 1

        # Calculate cumulative count
        for i in range(1, 256):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            output[count[(ord(arr[i]) // exp) % 256] - 1] = arr[i]
            count[(ord(arr[i]) // exp) % 256] -= 1
            i -= 1

        # Copy the sorted characters back to the original array
        for i in range(n):
            arr[i] = output[i]

        steps.append(arr.copy())

    arr = list(s)
    steps = [arr.copy()]
    max_digit = max(map(ord, arr))
    exp = 1
    while max_digit // exp > 0:
        counting_sort(arr, exp, steps)
        exp *= 256

    return steps

def bogo_sort_characters_steps(s):
    def is_sorted_characters(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    arr = list(s)
    steps = [arr.copy()]
    while not is_sorted_characters(arr):
        random.shuffle(arr)
        steps.append(arr.copy())
    return steps

# Visualización
def visualize_sorting(steps):
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.set_title('Ordenar Oracion')
    bar_rects = ax.bar(range(len(steps[0])), list(range(len(steps[0]))), align="center")
    
    # Configurar los ejes
    ax.set_xticks(range(len(steps[0])))
    ax.set_yticks([])  # Ocultar los valores del eje Y
    
    # Lista para almacenar los textos
    text_elements = []

    # Función para actualizar la gráfica en cada frame
    def update_fig(step):
        # Limpiar textos anteriores
        while text_elements:
            text_element = text_elements.pop()
            text_element.remove()
        
        for rect, val in zip(bar_rects, step):
            rect.set_height(1)  # Establecer la altura de las barras en 1
            rect.set_color('purple')  # Establecer el color de las barras en azul
            rect.set_edgecolor('white')  # Establecer el borde de las barras en blanco
            # Agregar texto en el centro de cada barra
            text = ax.text(rect.get_x() + rect.get_width() / 2.0, 0.5, val, ha='center', va='center', color='white', fontsize=12)
            text_elements.append(text)
        return bar_rects

    # Crear la animación
    ani = animation.FuncAnimation(fig, update_fig, frames=steps, interval=500, repeat=False)
    #plt.xlabel('Index')
    plt.show()

# Función general
def graficarPalabra(cadena, metodo):
    if metodo == "bubble":
        steps = bubble_sort_characters_steps(cadena)
    elif metodo == "insertion":
        steps = insertion_sort_characters_steps(cadena)
    elif metodo == "selection":
        steps = selection_sort_characters_steps(cadena)
    elif metodo == "merge":
        steps = merge_sort_characters_steps(cadena)
    elif metodo == "quick":
        steps = quick_sort_characters_steps(cadena)
    elif metodo == "heap":
        steps = heap_sort_characters_steps(cadena)
    elif metodo == "radix":
        steps = radix_sort_characters_steps(cadena)
    elif metodo == "bogo":
        steps = bogo_sort_characters_steps(cadena)
    else:
        raise ValueError("Método de ordenamiento no soportado.")
    
    visualize_sorting(steps)
'''
# Ejemplo de uso
cadena = 'pepe pecas'
graficarPalabra(cadena, 'bogo')  # Cambiar 'bubble' por el algoritmo deseado
'''
