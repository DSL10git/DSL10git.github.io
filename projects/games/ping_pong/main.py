import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 8
PADDLE_SPEED = 5
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

# Fonts
default_font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Utility to draw centered text
def draw_text(text, font, color, x, y):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(x, y))
    screen.blit(surf, rect)

# Main game function
def main():
    state = 'menu'            # menu, help, play, gameover
    input_text = ''           # score limit input
    score_limit = None
    left_score, right_score = 0, 0
    winner = ''
    modes = ['AI vs You', '2 Players']
    mode_index = 0

    # Game objects
    left_paddle = pygame.Rect(50, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect((WIDTH - BALL_RADIUS * 2) // 2, (HEIGHT - BALL_RADIUS * 2) // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
    ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y
    reset_btn = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2 + 50, 120, 50)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if state == 'menu':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        mode_index = (mode_index + 1) % len(modes)
                    elif event.key == pygame.K_h:
                        state = 'help'
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if input_text.isdigit() and int(input_text) > 0:
                            score_limit = int(input_text)
                            mode = modes[mode_index]
                            left_score, right_score = 0, 0
                            ball.center = (WIDTH // 2, HEIGHT // 2)
                            ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y
                            state = 'play'
                    elif event.unicode.isdigit():
                        input_text += event.unicode

            elif state == 'help':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    state = 'menu'

            elif state == 'gameover':
                if event.type == pygame.MOUSEBUTTONDOWN and reset_btn.collidepoint(event.pos):
                    state = 'menu'
                    input_text = ''
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    state = 'menu'
                    input_text = ''

        screen.fill(BLACK)

        if state == 'menu':
            draw_text("Ping Pong", default_font, WHITE, WIDTH // 2, HEIGHT // 4)
            draw_text(f"Mode: {modes[mode_index]}", small_font, WHITE, WIDTH // 2, HEIGHT // 4 + 60)
            draw_text("Press M to toggle mode", small_font, WHITE, WIDTH // 2, HEIGHT // 4 + 100)
            draw_text(f"Enter points to win: {input_text}", small_font, WHITE, WIDTH // 2, HEIGHT // 2)
            draw_text("Press ENTER to start", small_font, WHITE, WIDTH // 2, HEIGHT // 2 + 40)
            draw_text("Press H for Help", small_font, WHITE, WIDTH // 2, HEIGHT // 2 + 80)

        elif state == 'help':
            draw_text("How to Play", default_font, WHITE, WIDTH // 2, HEIGHT // 6)
            draw_text("M: Toggle AI/2P in menu", small_font, WHITE, WIDTH // 2, HEIGHT // 6 + 60)
            draw_text("Type digits + Enter: Set points to win", small_font, WHITE, WIDTH // 2, HEIGHT // 6 + 100)
            draw_text("In-game Controls:", small_font, WHITE, WIDTH // 2, HEIGHT // 6 + 160)
            draw_text("Player 2 (Right): Up/Down arrows", small_font, WHITE, WIDTH // 2, HEIGHT // 6 + 200)
            draw_text("Player 1 (Left in 2P): W/S keys", small_font, WHITE, WIDTH // 2, HEIGHT // 6 + 240)
            draw_text("Reset (after win): Click Reset or press R", small_font, WHITE, WIDTH // 2, HEIGHT // 6 + 280)
            draw_text("Press B to go back", small_font, WHITE, WIDTH // 2, HEIGHT // 6 + 340)

        elif state == 'play':
            # Left paddle
            if mode == 'AI vs You':
                if left_paddle.centery < ball.centery and left_paddle.bottom < HEIGHT:
                    left_paddle.y += PADDLE_SPEED
                if left_paddle.centery > ball.centery and left_paddle.top > 0:
                    left_paddle.y -= PADDLE_SPEED
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and left_paddle.top > 0:
                    left_paddle.y -= PADDLE_SPEED
                if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
                    left_paddle.y += PADDLE_SPEED

            # Right paddle
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and right_paddle.top > 0:
                right_paddle.y -= PADDLE_SPEED
            if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
                right_paddle.y += PADDLE_SPEED

            # Ball movement
            ball.x += ball_speed_x
            ball.y += ball_speed_y
            if ball.top <= 0 or ball.bottom >= HEIGHT:
                ball_speed_y *= -1
            if ball.colliderect(left_paddle) and ball_speed_x < 0:
                ball_speed_x *= -1
            if ball.colliderect(right_paddle) and ball_speed_x > 0:
                ball_speed_x *= -1

            # Scoring
            if ball.left <= 0:
                right_score += 1
                ball.center = (WIDTH // 2, HEIGHT // 2)
                ball_speed_x = BALL_SPEED_X
            if ball.right >= WIDTH:
                left_score += 1
                ball.center = (WIDTH // 2, HEIGHT // 2)
                ball_speed_x = -BALL_SPEED_X

            # Win check
            if score_limit and (left_score >= score_limit or right_score >= score_limit):
                if mode == 'AI vs You':
                    winner = 'AI' if left_score >= score_limit else 'You'
                else:
                    winner = 'Left Player' if left_score >= score_limit else 'Right Player'
                state = 'gameover'

            # Draw
            pygame.draw.rect(screen, WHITE, left_paddle)
            pygame.draw.rect(screen, WHITE, right_paddle)
            pygame.draw.ellipse(screen, WHITE, ball)
            pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
            draw_text(str(left_score), default_font, WHITE, WIDTH // 4, 50)
            draw_text(str(right_score), default_font, WHITE, WIDTH * 3 // 4, 50)

        elif state == 'gameover':
            draw_text(f"{winner} wins!", default_font, WHITE, WIDTH // 2, HEIGHT // 2)
            pygame.draw.rect(screen, GRAY, reset_btn)
            draw_text("Reset", small_font, BLACK, reset_btn.centerx, reset_btn.centery)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
