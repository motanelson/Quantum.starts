import pygame
import random
import sys

# Inicialização do pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Avião com Unicode")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



# Fonte para o avião
FONT = pygame.font.Font(None, 50)

# Configurações do avião
PLANE = "✈"  # Avião em Unicode
plane_width = 50
plane_height = 50
plane_x = WIDTH // 2
plane_y = HEIGHT - 100
plane_speed = 5

# Configurações das bolas
BALL_RADIUS = 10
BALL_SPEED = 3
balls = [{"x": random.randint(0, WIDTH), "y": random.randint(HEIGHT, HEIGHT * 2)} for _ in range(10)]

# Velocidade do fundo
SCROLL_SPEED = 2
bg_offset = 0

# Função principal
def main():
    global plane_x, bg_offset
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentação do avião
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and plane_x > 0:
            plane_x -= plane_speed
        if keys[pygame.K_RIGHT] and plane_x < WIDTH - plane_width:
            plane_x += plane_speed

        # Atualizar as posições das bolas
        for ball in balls:
            ball["y"] -= BALL_SPEED
            if ball["y"] < -BALL_RADIUS:  # Reseta a bola quando sai da tela
                ball["x"] = random.randint(0, WIDTH)
                ball["y"] = random.randint(HEIGHT, HEIGHT * 2)

        # Atualizar o fundo
        bg_offset = (bg_offset + SCROLL_SPEED) % HEIGHT

        # Desenhar na tela
        WINDOW.fill(BLACK)

        # Fundo com efeito de movimento
        for i in range(2):
            pygame.draw.rect(WINDOW, BLACK, (0, -HEIGHT + bg_offset + i * HEIGHT, WIDTH, HEIGHT))

        # Desenhar bolas
        for ball in balls:
            pygame.draw.circle(WINDOW, WHITE, (ball["x"], ball["y"]), BALL_RADIUS)

        # Desenhar avião
        plane_surface = FONT.render(PLANE, True, WHITE)
        WINDOW.blit(plane_surface, (plane_x, plane_y))

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

