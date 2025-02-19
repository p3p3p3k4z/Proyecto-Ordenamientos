import pygame
import sys

# Inicializa Pygame y sus módulos
pygame.init()

# Constantes para el ejemplo (simuladas)
pantalla = pygame.display.set_mode((800, 600))
BLANCO = (255, 255, 255)
MORADO = (128, 0, 128)
TEXTO_CONTINUAR = "Continuar"
COORD_BOTON_CONTINUAR = (600, 500)
BOTON_CONTINUAR_TAMANO = (150, 50)

# Inicializa la fuente de Pygame
pygame.font.init()
FUENTE_SUBTITULO = pygame.font.SysFont('Arial', 20)

def lista_ingresar():
    sentences = []
    user_input = ''
    rect_boton_continuar = pygame.Rect(COORD_BOTON_CONTINUAR, BOTON_CONTINUAR_TAMANO)
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    sentences.append(user_input)
                    user_input = ''
                elif evento.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif evento.unicode.isprintable():
                    user_input += evento.unicode
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_boton_continuar.collidepoint(evento.pos):
                    print("Continuar para seleccionar ordenamientos")
                    menu_orders(sentences)
        
        pantalla.fill(BLANCO)
        # Dibuja los elementos en pantalla
        dibuTexContorno(pantalla, "Ingrese una oración y presione Enter:", FUENTE_SUBTITULO, (20, 20), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, user_input, FUENTE_SUBTITULO, (20, 60), BLANCO, MORADO, 2, centrado=False)
        dibuTexContorno(pantalla, "Oraciones ingresadas: " + str(sentences), FUENTE_SUBTITULO, (20, 100), BLANCO, MORADO, 2, centrado=False)
        rect_boton_continuar = crear_boton(pantalla, TEXTO_CONTINUAR, 'Arial', COORD_BOTON_CONTINUAR, BLANCO, MORADO, 20, BOTON_CONTINUAR_TAMANO)
        pygame.display.flip()

# Ejemplo de función que simula la función de dibujo
def dibuTexContorno(pantalla, texto, fuente, posicion, color_texto, color_fondo, grosor_borde, centrado=True):
    texto_renderizado = fuente.render(texto, True, color_texto, color_fondo)
    rect_texto = texto_renderizado.get_rect()
    if centrado:
        rect_texto.center = posicion
    else:
        rect_texto.topleft = posicion
    pygame.draw.rect(pantalla, color_fondo, rect_texto, border_radius=grosor_borde)
    pantalla.blit(texto_renderizado, rect_texto)

# Función simulada para pasar a la siguiente etapa
def menu_orders(sentences):
    print("Implementa aquí la lógica para seleccionar ordenamientos")
    print("Oraciones ingresadas:", sentences)
    # Aquí se debería implementar la lógica para seleccionar los ordenamientos

# Función simulada para crear un botón
def crear_boton(pantalla, texto, fuente, coordenadas, color_texto, color_fondo, tamaño_fuente, tamaño_boton):
    rect_boton = pygame.Rect(coordenadas, tamaño_boton)
    pygame.draw.rect(pantalla, color_fondo, rect_boton)
    fuente_boton = pygame.font.SysFont(fuente, tamaño_fuente)
    texto_renderizado = fuente_boton.render(texto, True, color_texto)
    rect_texto = texto_renderizado.get_rect(center=rect_boton.center)
    pantalla.blit(texto_renderizado, rect_texto)
    return rect_boton

# Ejecución de la función para ingresar oraciones
lista_ingresar()
