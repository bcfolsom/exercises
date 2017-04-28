import pygame
import random

class Monster:
    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

monster = Monster('Monster', 112, 105)

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((512, 480))
    pygame.display.set_caption('Monster Reign')
    clock = pygame.time.Clock()
    background = pygame.image.load('images/background.png').convert_alpha()
    hero = pygame.image.load('images/hero.png')
    monster = pygame.image.load('images/monster.png')
    goblin = pygame.image.load('images/goblin.png')
    hero_x = 240
    hero_y = 224
    # self.x = 112
    # self.y = 105
    goblin_x = 368
    goblin_y = 344
    win_sound = pygame.mixer.Sound('sounds/win.wav')
    lose_sound = pygame.mixer.Sound('sounds/lose.wav')
    music = pygame.mixer.Sound('sounds/music.wav')
    change_dir_countdown = 100
    x_dir = 32
    y_dir = 32

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Tutorial video 8, moving objects
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.y -= 5
            if event.key == pygame.K_DOWN:
                self.y += 5
            if event.key == pygame.K_LEFT:
                self.x -= 5
            if event.key == pygame.K_RIGHT:
                self.x += 5
            if self.x > 512:
                self.x -= 512
            if self.x < 0:
                self.x += 512
            if self.y > 480:
                self.y -= 480
            if self.y < 0:
                self.y += 480
            change_dir_countdown -= 1
            if change_dir_countdown == 0:
                change_dir_countdown += 120
                movement = random.randint(0, 3)
                if movement == 0:
                    self.x = self.x - x_dir
                    self.y = self.y + y_dir
                if movement == 1:
                    self.x = self.x + x_dir
                    self.y = self.y - y_dir
                if movement == 2:
                    self.x = self.x - x_dir
                    self.y = self.y - y_dir
                if movement == 3:
                    self.x = self.x + x_dir
                    self.y = self.y + y_dir

        # Draw background

        screen.blit(background, (0, 0))

        # Game display

        screen.blit(hero, (hero_x, hero_y))
        screen.blit(monster, (112, 105))
        screen.blit(goblin, (goblin_x, goblin_y))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
