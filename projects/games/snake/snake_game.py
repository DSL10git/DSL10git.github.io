import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("games/snake/resources/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("games/snake/resources/block.jpg").convert()
        self.direction = 'down'
        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # shift body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # move head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        # draw segments
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        # draw two round eyes on head
        head_x, head_y = self.x[0], self.y[0]
        eye_r = SIZE // 8
        off_x = SIZE // 4
        off_y = SIZE // 4
        color = (0, 0, 0)
        pygame.draw.circle(self.parent_screen, color, (head_x + off_x, head_y + off_y), eye_r)
        pygame.draw.circle(self.parent_screen, color, (head_x + SIZE - off_x, head_y + off_y), eye_r)

    def draw_dead(self):
        # draw body segments
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        # draw X eyes on head
        head_x, head_y = self.x[0], self.y[0]
        eye_r = SIZE // 8
        off_x = SIZE // 4
        off_y = SIZE // 4
        color = (255, 0, 0)  # red X for dead

        ex1, ey1 = head_x + off_x, head_y + off_y
        ex2, ey2 = head_x + SIZE - off_x, head_y + off_y

        # first eye X
        pygame.draw.line(self.parent_screen, color, (ex1 - eye_r, ey1 - eye_r), (ex1 + eye_r, ey1 + eye_r), 3)
        pygame.draw.line(self.parent_screen, color, (ex1 - eye_r, ey1 + eye_r), (ex1 + eye_r, ey1 - eye_r), 3)
        # second eye X
        pygame.draw.line(self.parent_screen, color, (ex2 - eye_r, ey2 - eye_r), (ex2 + eye_r, ey2 + eye_r), 3)
        pygame.draw.line(self.parent_screen, color, (ex2 - eye_r, ey2 + eye_r), (ex2 + eye_r, ey2 - eye_r), 3)

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game - by Daniel L.")

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((1000, 800))
        self.snake   = Snake(self.surface)
        self.apple   = Apple(self.surface)

    def play_background_music(self):
        pygame.mixer.music.load('games/snake/resources/bg_music_1.mp3')
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, name):
        if name == "crash":
            s = pygame.mixer.Sound("games/snake/resources/crash.mp3")
        elif name == "ding":
            s = pygame.mixer.Sound("games/snake/resources/ding.mp3")
        pygame.mixer.Sound.play(s)

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        pygame.mixer.music.unpause()

    def is_collision(self, x1, y1, x2, y2):
        return x1 >= x2 and x1 < x2 + SIZE and y1 >= y2 and y1 < y2 + SIZE

    def render_background(self):
        bg = pygame.image.load("games/snake/resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.snake.walk()

        # ─── border collision ────────────────────────────────────────────────
        head_x, head_y = self.snake.x[0], self.snake.y[0]
        if head_x < 0 or head_x >= self.surface.get_width():
            self.play_sound("crash")
            raise Exception("Hit the wall")
        if head_y < 0 or head_y >= self.surface.get_height():
            self.play_sound("crash")
            raise Exception("Hit the wall")

        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # ─── apple eating ─────────────────────────────────────────────────
        if self.is_collision(head_x, head_y, self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()
            return    # skip self-collision this tick

        # ─── self-collision ────────────────────────────────────────────────
        for i in range(3, self.snake.length):
            if self.is_collision(head_x, head_y, self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise Exception("Bit itself")

    def display_score(self):
        font  = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self, reason: str):
        self.render_background()
        font  = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game over! Your score: {self.snake.length}", True, (255,255,255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render(f"Reason: {reason}", True, (255, 100, 100))
        self.surface.blit(line2, (200, 350))
        line3 = font.render("Enter to replay  •  Esc to quit", True, (255,255,255))
        self.surface.blit(line3, (200, 400))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        running = True
        pause   = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_RETURN:
                        pause = False
                        self.reset()
                    elif not pause:
                        if event.key in (K_LEFT, K_a):
                            self.snake.move_left()
                        elif event.key in (K_RIGHT, K_d):
                            self.snake.move_right()
                        elif event.key in (K_UP, K_w):
                            self.snake.move_up()
                        elif event.key in (K_DOWN, K_s):
                            self.snake.move_down()
                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                # show dead snake with X-eyes
                self.render_background()
                self.snake.draw_dead()
                pygame.display.flip()
                time.sleep(1)  # pause before game over

                # then show game-over with reason
                self.show_game_over(str(e))
                pause = True

            time.sleep(0.25)

if __name__ == '__main__':
    Game().run()
