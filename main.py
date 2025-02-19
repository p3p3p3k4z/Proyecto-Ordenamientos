import pygame
import sys
import random

import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent
src_path = project_root / "src"
sys.path.append(str(src_path))

from src.orders import *
from src.orders_font import *

from src.graficarAnim import Graficar
from src.rendimiento import mostrar_perfil
from src.GraficarOrdenamietos import GraficarOrds,GraficarOrds_time
from src.grafConteo import grafLlamadas
from src.graficarAnim_pab import graficarPalabra

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 608, 472
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("ANÁLISIS DE ALGORITMOS")

# Cargar las imágenes
imagen_conejo = pygame.image.load('./img/Fondo_Conejo.png')
imagen_fondo = pygame.image.load('./img/fondo_nieve.png')
imagen_simple = pygame.image.load('./img/fondo_n.png')
imagen_icono = pygame.image.load('./img/conejito.png')

# Colores
BLANCO = (255, 255, 255)
MORADO = (128, 0, 128)
VERDE = (0, 255, 0)
NEGRO = (0,0,0)

# Fuentes
FUENTE_TITULO = pygame.font.SysFont('Arial', 40)
FUENTE_SUBTITULO = pygame.font.SysFont('Arial', 30)
FUENTE_BOTON = pygame.font.SysFont('Arial', 40)

# Textos
TEXTO_TITULO = "ANÁLISIS DE ALGORITMOS"
TEXTO_SUBTITULO = "ordenamientos"
TEXTO_INICIO = "INICIO"
TEXTO_SALIR = "SALIR"
TEXTO_CONTINUAR = "Continuar"
TEXTO_REGRESO = "Regresar"
TEXTO_LISTA = "INSERTA LA LISTA"
TEXTO_LISTA_ALEATORIA = "INSERTAR LISTA ALEATORIA"

# Coordenadas de los botones
COORD_BOTON_INICIO = (150, 200)
COORD_BOTON_SALIR = (150, 300)
COORD_BOTON_CONTINUAR = (ANCHO // 2 - 75, 350)
COORD_BOTON_LISTA = (60,50)
COORD_BOTON_LISTALE = (30,150)

BOTON_TAMANO = (150, 60)
BOTON_CONTINUAR_TAMANO = (150, 50)
BOTON_LARGO = (500,60)
BOTON_LARGO2 = (550,60)

#Icono
pygame.display.set_icon(imagen_icono)

# Coordenadas del conejo
RECT_CONEJO = pygame.Rect(472, 372, 100, 100)

# Cargar el sonido
sonido_click = pygame.mixer.Sound('./sound/salto.wav')

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

ordenamientos_cadena = {
    'bubble': bubble_sort_characters,
    'insertion': insertion_sort_characters,
    'selection': selection_sort_characters,
    'merge': merge_sort_characters,
    'quick': quick_sort_characters,
    'bogo': bogo_sort_characters,
    'heap': heap_sort_characters,
    'radix': radix_sort_characters
}

def generar_lista_aleatoria():
    return [random.randint(1, 100) for _ in range(10)]

def convert_to_ascii(char_list):
    ascii_values = [ord(char) for string in char_list for char in string]
    return ascii_values
################################################################################################################3
def dibuTexContorno(surface, texto, fuente, posicion, color_texto, color_contorno, grosor, centrado=False):
    texto_renderizado = fuente.render(texto, True, color_texto)
    rectangulo_texto = texto_renderizado.get_rect()

    if centrado:
        rectangulo_texto.center = posicion
    else:
        rectangulo_texto.topleft = posicion

    for dx in range(-grosor, grosor + 1):
        for dy in range(-grosor, grosor + 1):
            if dx != 0 or dy != 0:
                rect_contorno = rectangulo_texto.copy()
                rect_contorno.x += dx
                rect_contorno.y += dy
                surface.blit(fuente.render(texto, True, color_contorno), rect_contorno)

    surface.blit(texto_renderizado, rectangulo_texto)

def dibuText(surface, texto, posicion, color, fuente, centrado=False):
    texto_renderizado = fuente.render(texto, True, color)
    rectangulo_texto = texto_renderizado.get_rect()

    if centrado:
        rectangulo_texto.center = posicion
    else:
        rectangulo_texto.topleft = posicion

    surface.blit(texto_renderizado, rectangulo_texto)
###########################################################################################################
def crear_boton(pantalla, texto, fuente, posicion, color_texto, color_boton, tamano_fuente, tamano_boton):
    fuente_boton = pygame.font.SysFont(fuente, tamano_fuente)
    texto_renderizado = fuente_boton.render(texto, True, color_texto)
    ancho_texto, alto_texto = texto_renderizado.get_size()

    rect_boton = pygame.Rect(posicion[0], posicion[1], tamano_boton[0], tamano_boton[1])
    pygame.draw.rect(pantalla, color_boton, rect_boton)

    texto_x = rect_boton.x + (rect_boton.width - ancho_texto) // 2
    texto_y = rect_boton.y + (rect_boton.height - alto_texto) // 2
    pantalla.blit(texto_renderizado, (texto_x, texto_y))

    return rect_boton
###########################################################################################################
def dibujar_menu_principal():
    pantalla.blit(imagen_conejo, (0, 0))
    dibuTexContorno(pantalla, TEXTO_TITULO, FUENTE_TITULO, (ANCHO // 2, 80), BLANCO, MORADO, 2, centrado=True)
    dibuTexContorno(pantalla, TEXTO_SUBTITULO, FUENTE_SUBTITULO, (ANCHO // 2, 140), BLANCO, MORADO, 2, centrado=True)
    rect_boton_inicio = crear_boton(pantalla, TEXTO_INICIO, 'Arial', COORD_BOTON_INICIO, BLANCO, MORADO, 40, BOTON_TAMANO)
    rect_boton_salir = crear_boton(pantalla, TEXTO_SALIR, 'Arial', COORD_BOTON_SALIR, BLANCO, MORADO, 40, BOTON_TAMANO)
    return rect_boton_inicio, rect_boton_salir

def dibujar_menu_lista():
    pantalla.blit(imagen_fondo, (0, 0))
    rect_boton_lista = crear_boton(pantalla, TEXTO_LISTA, 'Arial', COORD_BOTON_LISTA, BLANCO, MORADO, 40, BOTON_LARGO)
    rect_boton_lista_aleatoria = crear_boton(pantalla, TEXTO_LISTA_ALEATORIA, 'Arial', COORD_BOTON_LISTALE, BLANCO, MORADO, 40, BOTON_LARGO2)
    rect_boton_lista_palabra = crear_boton(pantalla,"INSERTAR ORACION", 'Arial', (30,250), BLANCO, MORADO, 40, BOTON_LARGO2)
    rect_boton_continuar = crear_boton(pantalla, TEXTO_REGRESO, 'Arial', COORD_BOTON_CONTINUAR, BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    return rect_boton_lista, rect_boton_lista_aleatoria, rect_boton_lista_palabra, rect_boton_continuar

def dibujar_menu_ord():
    pantalla.blit(imagen_fondo, (0, 0))
    dibuTexContorno(pantalla, "SELECCIONA EL ORDENAMIENTO", FUENTE_SUBTITULO, (80, 10), BLANCO, MORADO, 2, centrado=False)
    boton_a = crear_boton(pantalla,"BUBBLE ITE",'Arial',(20,50),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_b = crear_boton(pantalla,"INSERTION ITE",'Arial',(20,150),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_c = crear_boton(pantalla,"SELECTION ITE",'Arial',(20,250),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_d = crear_boton(pantalla,"MERGE ITE",'Arial',(230,50),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_e = crear_boton(pantalla,"QUICK RCS",'Arial',(230,150),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_f = crear_boton(pantalla,"BOGO ITE",'Arial',(450,50),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_g = crear_boton(pantalla,"HEAP ITE",'Arial',(450,150),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_h = crear_boton(pantalla,"RADIX ITE",'Arial',(450,250),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_regreso = crear_boton(pantalla, "Regreso", 'Arial', COORD_BOTON_CONTINUAR, BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    boton_gra = crear_boton(pantalla,"GRAFICAR",'Arial',(230,250),BLANCO,VERDE,20,BOTON_TAMANO)
    
    return boton_a, boton_b, boton_c,boton_d,boton_e,boton_f,boton_g,boton_h,boton_regreso,boton_gra

def dibujar_menu_graf():
    pantalla.blit(imagen_fondo, (0, 0))
    pantalla.blit(imagen_icono,(205,155))
    dibuTexContorno(pantalla, "SELECCIONA QUE QUIERES GRAFICAR", FUENTE_SUBTITULO, (20, 30), BLANCO, MORADO, 2, centrado=False)
    
    boton_conteo = crear_boton(pantalla, "LLAMADAS", 'Arial', (20,250),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_funcion = crear_boton(pantalla, "FUNCION", 'Arial', (230,80),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_tiempo = crear_boton(pantalla, "TIEMPOS", 'Arial', (450,250),BLANCO,MORADO,20,BOTON_TAMANO)
    boton_regreso = crear_boton(pantalla, "REGRESAR", 'Arial', COORD_BOTON_CONTINUAR,BLANCO,MORADO,20,BOTON_TAMANO)
    
    return boton_conteo,boton_funcion,boton_tiempo,boton_regreso
###########################################################################################################
def lista_ingresar_palabra():
    pygame.display.set_caption("Ingresar Oraciones")
    sentences = []
    user_input = ''
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if user_input.strip():  # Solo agregar entrada no vacía
                        sentences.append(user_input)
                        print(f"Oración agregada: {user_input}")  # Verificación de agregado
                        user_input = ''
                elif evento.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += evento.unicode
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_continuar.collidepoint(evento.pos):
                    print("Continuar para seleccionar ordenamientos")
                    menu_orders_palabra(sentences)
        
        pantalla.fill(NEGRO)
        dibuTexContorno(pantalla, "Ingrese una oración y presione Enter:", FUENTE_SUBTITULO, (20, 20), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, user_input, FUENTE_SUBTITULO, (20, 60), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, "Oraciones ingresadas: " + ', '.join(sentences), FUENTE_SUBTITULO, (20, 150), BLANCO, MORADO, 2, centrado=False)
        rect_boton_continuar = crear_boton(pantalla, TEXTO_CONTINUAR, 'Arial', COORD_BOTON_CONTINUAR, BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
        print(str(sentences))
        pygame.display.flip()

def lista_ingresar():
    numbers = []
    user_input = ''
    rect_boton_continuar = crear_boton(pantalla, TEXTO_CONTINUAR, 'Arial', COORD_BOTON_CONTINUAR, BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    try:
                        number = int(user_input)
                        numbers.append(number)
                    except ValueError:
                        pass
                    user_input = ''
                elif evento.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif evento.unicode.isdigit():
                    user_input += evento.unicode
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_continuar.collidepoint(evento.pos):
                    print("Continuar para seleccionar ordenamientos")
                    menu_orders(numbers)
        
        pantalla.blit(imagen_simple, (0, 0))
        dibuTexContorno(pantalla, "Ingrese números y presione Enter:", FUENTE_SUBTITULO, (20, 20), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, user_input, FUENTE_SUBTITULO, (20, 60), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, "Lista actual: " + str(numbers), FUENTE_SUBTITULO, (20, 100), BLANCO, MORADO, 2, centrado=False)
        rect_boton_continuar = crear_boton(pantalla, TEXTO_CONTINUAR, 'Arial', COORD_BOTON_CONTINUAR, BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
        pygame.display.flip()

def lista_aleatoria():
    numbers = generar_lista_aleatoria()
    pantalla.blit(imagen_simple, (0, 0))
    dibuTexContorno(pantalla, "LISTA GENERADA", FUENTE_TITULO, (130, 60), BLANCO, MORADO, 2, centrado=False)
    dibuTexContorno(pantalla, str(numbers), FUENTE_SUBTITULO, (60, 180), BLANCO, MORADO, 2, centrado=False)
    rect_boton_continuar = crear_boton(pantalla, TEXTO_CONTINUAR, 'Arial', COORD_BOTON_CONTINUAR, BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    pygame.display.flip()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_continuar.collidepoint(evento.pos):
                    print("Continuar para seleccionar ordenamientos")
                    menu_orders(numbers)
###########################################################################################################
def menu_graficas(ls):
    ls_w=ls.copy()
    boton_conteo,boton_funcion,boton_tiempo,boton_regreso = dibujar_menu_graf()
    pygame.display.flip()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                 if boton_regreso.collidepoint(evento.pos):
                    print("REGRESO")
                    menu_orders(ls)
                 elif boton_funcion.collidepoint(evento.pos):
                    print("GRAFICAR FUNCIONES")
                    GraficarOrds(ls_w)
                 elif boton_tiempo.collidepoint(evento.pos):
                    print("GRAFICAR TIEMPOS")
                    GraficarOrds_time(ls_w)
                 elif boton_conteo.collidepoint(evento.pos):
                    print("GRAFICAR CONTEO DE GRAFICAS")
                    grafLlamadas(ls_w)
                    
def menu_graficas_palabra(ls):
    ls_m=ls.copy()
    ls_w=(convert_to_ascii(ls_m))
    print(str(ls_w))
    boton_conteo,boton_funcion,boton_tiempo,boton_regreso = dibujar_menu_graf()
    pygame.display.flip()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                 if boton_regreso.collidepoint(evento.pos):
                    print("REGRESO")
                    menu_orders(ls)
                 elif boton_funcion.collidepoint(evento.pos):
                    print("GRAFICAR FUNCIONES")
                    GraficarOrds(ls_w)
                 elif boton_tiempo.collidepoint(evento.pos):
                    print("GRAFICAR TIEMPOS")
                    GraficarOrds_time(ls_w)
                 elif boton_conteo.collidepoint(evento.pos):
                    print("GRAFICAR CONTEO DE GRAFICAS")
                    grafLlamadas(ls_w)

def menu_lista_final_cadena(ls, ordenar):
    ls2 = ls.copy()
    
    pantalla.blit(imagen_simple, (0, 0))
    boton_regreso = crear_boton(pantalla, "Regresar MENU", 'Arial', (20, 400), BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    boton_grafica = crear_boton(pantalla, "GRAFICAR", 'Arial', (240, 400), BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    boton_procesos = crear_boton(pantalla, "VER PROCESOS", 'Arial', (450, 400), BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    
    funcion_ordenamiento = ordenamientos_cadena[ordenar]
    ls2_n = funcion_ordenamiento(ls2)
    
    print(str(ls))
    print("\n")
    print(str(ls2))
    print(str(ls2_n))
    
    ls_a=convert_to_ascii(ls)
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_regreso.collidepoint(evento.pos):
                    print("REGRESO")
                    menu_principal()
                elif boton_grafica.collidepoint(evento.pos):
                    print("GRAFICAR")
                    graficarPalabra(ls2, ordenar)
                elif boton_procesos.collidepoint(evento.pos):
                    print("PROCESOS")
                    mostrar_perfil(ls_a, ordenar)
    
        dibuTexContorno(pantalla, "LISTA USADA", FUENTE_TITULO, (170, 40), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, str(ls), FUENTE_SUBTITULO, (60, 120), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, "LISTA ORDENADA", FUENTE_TITULO, (140, 220), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, str(ls2_n), FUENTE_SUBTITULO, (60, 300), BLANCO, MORADO, 2, centrado=False)
        pygame.display.flip()

def menu_lista_final(ls, ordenar):
    ls2 = ls.copy()
    
    pantalla.blit(imagen_simple, (0, 0))
    boton_regreso = crear_boton(pantalla, "Regresar MENU", 'Arial', (20, 400), BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    boton_grafica = crear_boton(pantalla, "GRAFICAR", 'Arial', (240, 400), BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    boton_procesos = crear_boton(pantalla, "VER PROCESOS", 'Arial', (450, 400), BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
    
    funcion_ordenamiento = ordenamientos[ordenar]
    ls2 = funcion_ordenamiento(ls2)
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_regreso.collidepoint(evento.pos):
                    print("REGRESO")
                    menu_principal()
                elif boton_grafica.collidepoint(evento.pos):
                    print("GRAFICAR")
                    Graficar(ls, ordenar)
                elif boton_procesos.collidepoint(evento.pos):
                    print("PROCESOS")
                    mostrar_perfil(ls, ordenar)
        
        dibuTexContorno(pantalla, "LISTA USADA", FUENTE_TITULO, (170, 40), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, str(ls), FUENTE_SUBTITULO, (60, 120), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, "LISTA ORDENADA", FUENTE_TITULO, (140, 220), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, str(ls2), FUENTE_SUBTITULO, (60, 300), BLANCO, MORADO, 2, centrado=False)
        pygame.display.flip()
    

def menu_orders_palabra(ls): 
    BOTON1,BOTON2,BOTON3,BOTON4,BOTON5,BOTON6,BOTON7,BOTON8,BOTONR,BOTONG = dibujar_menu_ord()
    pygame.display.flip()
    print(str(ls))
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if BOTONR.collidepoint(evento.pos):
                    print("REGRESO")
                    menu_lista()
                elif BOTONG.collidepoint(evento.pos):
                    print("Graficar todos los ordenamientos")
                    menu_graficas_palabra(ls)
                elif BOTON1.collidepoint(evento.pos):
                    print("BUBBLE")
                    menu_lista_final_cadena(ls,"bubble")
                elif BOTON2.collidepoint(evento.pos):
                    print("INSERTION")
                    menu_lista_final_cadena(ls,"insertion")
                elif BOTON3.collidepoint(evento.pos):
                    print("SELECTION")
                    menu_lista_final_cadena(ls,"selection")
                elif BOTON4.collidepoint(evento.pos):
                    print("MERGE")
                    menu_lista_final_cadena(ls,"merge")
                elif BOTON5.collidepoint(evento.pos):
                    print("QUICK")
                    menu_lista_final_cadena(ls,"quick")
                elif BOTON6.collidepoint(evento.pos):
                    print("BOGO")
                    menu_lista_final_cadena(ls,"bogo")
                elif BOTON7.collidepoint(evento.pos):
                    print("HEAP")
                    menu_lista_final_cadena(ls,"heap")
                elif BOTON8.collidepoint(evento.pos):
                    print("RADIX")
                    menu_lista_final_cadena(ls,"radix")
    

def menu_orders(ls): 
    BOTON1,BOTON2,BOTON3,BOTON4,BOTON5,BOTON6,BOTON7,BOTON8,BOTONR,BOTONG = dibujar_menu_ord()
    pygame.display.flip()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if BOTONR.collidepoint(evento.pos):
                    print("REGRESO")
                    menu_lista()
                elif BOTONG.collidepoint(evento.pos):
                    print("Graficar todos los ordenamientos")
                    menu_graficas(ls)
                elif BOTON1.collidepoint(evento.pos):
                    print("BUBBLE")
                    menu_lista_final(ls,"bubble")
                elif BOTON2.collidepoint(evento.pos):
                    print("INSERTION")
                    menu_lista_final(ls,"insertion")
                elif BOTON3.collidepoint(evento.pos):
                    print("SELECTION")
                    menu_lista_final(ls,"selection")
                elif BOTON4.collidepoint(evento.pos):
                    print("MERGE")
                    menu_lista_final(ls,"merge")
                elif BOTON5.collidepoint(evento.pos):
                    print("QUICK")
                    menu_lista_final(ls,"quick")
                elif BOTON6.collidepoint(evento.pos):
                    print("BOGO")
                    menu_lista_final(ls,"bogo")
                elif BOTON7.collidepoint(evento.pos):
                    print("HEAP")
                    menu_lista_final(ls,"heap")
                elif BOTON8.collidepoint(evento.pos):
                    print("RADIX")
                    menu_lista_final(ls,"radix")
                
def menu_lista():
    rect_boton_lista, rect_boton_lista_aleatoria, rect_boton_lista_palabra, rect_boton_continuar = dibujar_menu_lista()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_lista.collidepoint(evento.pos):
                    lista_ingresar()
                elif rect_boton_lista_aleatoria.collidepoint(evento.pos):
                    lista_aleatoria()
                elif rect_boton_lista_palabra.collidepoint(evento.pos):
                    lista_ingresar_palabra()
                elif rect_boton_continuar.collidepoint(evento.pos):
                    print("Volver al menú principal")
                    menu_principal()
        
        pygame.display.flip()

def menu_principal():
    pantalla_actual = 'menuPrincipal'
    corriendo = True
    rect_boton_inicio, rect_boton_salir = dibujar_menu_principal()
    
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if pantalla_actual == 'menuPrincipal':
                    if rect_boton_inicio.collidepoint(evento.pos):
                        print("Click en inicio")
                        pantalla_actual = 'lista'
                        menu_lista()
                    elif rect_boton_salir.collidepoint(evento.pos):
                        corriendo = False
                elif pantalla_actual == 'lista':
                    menu_lista()
                if RECT_CONEJO.collidepoint(evento.pos):
                    sonido_click.play()
        
        if pantalla_actual == 'menuPrincipal':
            rect_boton_inicio, rect_boton_salir = dibujar_menu_principal()
        elif pantalla_actual == 'lista':
            menu_lista()
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    menu_principal()

