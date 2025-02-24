import pygame
import sys
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Ruleta")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROJO = (255, 0, 0)
GREEN = (0, 255, 0)

RED = (173, 216, 230)
BLUE = (128, 128, 128)

font = pygame.font.Font(None, 15)

# Cargar sonidos
spin_sound = pygame.mixer.Sound('spin_sound.wav')
win_sound = pygame.mixer.Sound('win_sound.wav')
lose_sound = pygame.mixer.Sound('lose_sound.wav')

# Definir los arreglos de opciones
red_options = ["NO DORMIR", "NO DORMIR", "NO DORMIR", "NO DORMIR", "NO DORMIR", "NO DORMIR"]
blue_options = ["PROGRAMAR", "PROGRAMAR", "PROGRAMAR", "PROGRAMAR", "PROGRAMAR", "PROGRAMAR"]

# Calcular el número total de secciones
sections = len(red_options) + len(blue_options)

def draw_ruleta(surface, center, radius, red_options, blue_options, angle):
    for i in range(sections):
        start_angle = (i * (360 / sections)) + angle
        end_angle = start_angle + (360 / sections)
        
        # Alternar entre colores rojo y azul
        if i % 2 == 0:
            color = RED
            text = red_options[i // 2]
        else:
            color = BLUE
            text = blue_options[i // 2]

        pygame.draw.polygon(
            surface, color, 
            [
                center,
                (
                    center[0] + radius * math.cos(math.radians(start_angle)),
                    center[1] - radius * math.sin(math.radians(start_angle))
                ),
                (
                    center[0] + radius * math.cos(math.radians(end_angle)),
                    center[1] - radius * math.sin(math.radians(end_angle))
                )
            ]
        )
        
        text_surface = font.render(text, True, BLACK)
        text_angle = math.radians((start_angle + end_angle) / 2)
        text_x = center[0] + int(math.cos(text_angle) * (radius / 1.5)) - text_surface.get_width() // 2
        text_y = center[1] - int(math.sin(text_angle) * (radius / 1.5)) - text_surface.get_height() // 2
        surface.blit(text_surface, (text_x, text_y))

def draw_ganchito(surface, center, radius):
    pygame.draw.polygon(surface, BLACK, [
        (center[0], center[1] - radius + 10),  # Punto superior
        (center[0] - 20, center[1] - radius - 10),  # Esquina izquierda
        (center[0] + 20, center[1] - radius - 10)  # Esquina derecha
    ])

def main():
    running = True
    clock = pygame.time.Clock()
    center = (WIDTH // 2, HEIGHT // 2)
    radius = 200
    angle = 0
    spinning = False
    spin_speed = 10
    slowing_down = False

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] > HEIGHT - 100:  # Click en los botones
                    if event.pos[0] < WIDTH // 2:  # Botón Girar
                        if not spinning:
                            spinning = True
                            slowing_down = False
                            spin_speed = random.uniform(7, 12)  # Ajuste de velocidad inicial al azar
                            spin_sound.play(-1)  # Reproducir sonido de giro en bucle
                    else:  # Botón Detener
                        if spinning:
                            slowing_down = True

        if spinning:
            angle = (angle + spin_speed) % 360
            if slowing_down:
                spin_speed *= 0.99  # Desacelerar gradualmente
                if spin_speed < 0.1:  # Cuando la velocidad es muy baja, detener
                    spinning = False
                    slowing_down = False
                    spin_speed = 0
                    spin_sound.stop()  # Detener el sonido de giro

                    # Determinar en qué sección cayó la ruleta
                    final_angle = (angle + 360 / (2 * sections)) % 360
                    index = int(final_angle // (360 / sections))
                    if index % 2 == 0:
                        win_sound.play()  # Reproducir sonido de ganar
                    else:
                        lose_sound.play()  # Reproducir sonido de perder

        draw_ruleta(screen, center, radius, red_options, blue_options, angle)
        draw_ganchito(screen, center, radius)

        # Dibujar los botones de "Girar" y "Parar"
        girar_button_rect = pygame.draw.rect(screen, BLUE, (WIDTH // 2 - 150, HEIGHT - 100, 100, 50))
        parar_button_rect = pygame.draw.rect(screen, RED, (WIDTH // 2 + 50, HEIGHT - 100, 100, 50))

        # Centrar el texto en los botones
        text_girar = font.render("Girar", True, BLACK)
        text_detener = font.render("Parar", True, BLACK)
        
        girar_text_x = girar_button_rect.x + (girar_button_rect.width - text_girar.get_width()) // 2
        girar_text_y = girar_button_rect.y + (girar_button_rect.height - text_girar.get_height()) // 2
        
        parar_text_x = parar_button_rect.x + (parar_button_rect.width - text_detener.get_width()) // 2
        parar_text_y = parar_button_rect.y + (parar_button_rect.height - text_detener.get_height()) // 2
        
        screen.blit(text_girar, (girar_text_x, girar_text_y))
        screen.blit(text_detener, (parar_text_x, parar_text_y))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
