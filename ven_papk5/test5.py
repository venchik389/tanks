import pygame
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
score_player = 0
score_enemy = 0

# Класс GameSprite
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_img, cord_x, cord_y, width, height, speed):
        super().__init__()
        self.original_image = pygame.transform.scale(pygame.image.load(sprite_img), (width, height))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y
        self.speed = speed
        self.direction = 'up'  # Начальное направление танка

    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    
    def move(self):
        keys = pygame.key.get_pressed()
        
        # Проверяем направление движения и меняем изображение при необходимости
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            self.direction = 'up'
        elif keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
            self.direction = 'down'
        elif keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
            self.direction = 'right'
        elif keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.direction = 'left'

    def rotate(self):
        # Поворот изображения только при изменении направления
        if self.direction == 'left':
            self.image = pygame.transform.rotate(self.original_image, 90)
        elif self.direction == 'right':
            self.image = pygame.transform.rotate(self.original_image, -90)
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(self.original_image, 180)
        else:
            self.image = self.original_image

    def fire(self):
        bullet = Bullet(sprite_img='bullet.png',cord_x=self.rect.centerx,cord_y=self.rect.top,width=20,height=20,speed=20)
        bullets.add(bullet)

class Enemy(GameSprite):
    
    def move(self):
        keys = pygame.key.get_pressed()
        
        # Проверяем направление движения и меняем изображение при необходимости
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            self.direction = 'up'
        elif keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
            self.direction = 'down'
        elif keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
            self.direction = 'right'
        elif keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.direction = 'left'

    def shoot(self):
        if self.direction == 'left':
            self.image = self.rect.x = -5
        if self.direction == 'right':
            self.image = self.rect.x = 5
        if self.direction == 'down':
            self.image = self.rect.y = -5
        else:
            self.image = self.rect.y = 5

    def rotate(self):
        # Поворот изображения только при изменении направления
        if self.direction == 'left':
            self.image = pygame.transform.rotate(self.original_image, 90)
        elif self.direction == 'right':
            self.image = pygame.transform.rotate(self.original_image, -90)
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(self.original_image, 180)
        else:
            self.image = self.original_image

    def fire(self):
        bullet = Bullet(sprite_img='bullet.png',cord_x=self.rect.centerx,cord_y=self.rect.top,width=20,height=20,speed=20)
        bullets.add(bullet)

class Bullet(GameSprite):
        def update(self):
            if self.rect.y < 0:
                self.kill()
            if self.rect.y > 500:
                self.kill()
            if self.rect.x < 0:
                self.kill()
            if self.rect.x > 700:
                self.kill()
            if self.direction == 'up':
                self.rect.y -= self.speed
            elif self.direction == 'down':
                self.rect.y += self.speed
            elif self.direction == 'left':
                self.rect.x -= self.speed
            elif self.direction == 'right':
                self.rect.x += self.speed
            # Check for collision with enemy tank
           
            
            # Rotate the bullet's image based on direction
            if player.direction == 'left':
                self.image = pygame.transform.rotate(self.original_image, 0)
                self.direction = 'left'
            elif player.direction == 'right':
                self.image = pygame.transform.rotate(self.original_image, 180)
                self.direction = 'right'
            elif player.direction == 'down':
                self.image = pygame.transform.rotate(self.original_image, 90)
                self.direction = 'down'
            else:
                self.image = pygame.transform.rotate(self.original_image, -90)
                self.direction = 'up'
             # Increase player's score (or decrease enemy's score)



# Создание игровых объектов
player = Player('frie_tank.png', 5, 200, 40, 45, 7)
enemy = Enemy('enem_tank.png', 650, 200, 50, 50, 7)

bullets = pygame.sprite.Group()

# Создание окна и настройка отображения
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('танчики')

background = pygame.image.load('black_background.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()



game_running = True

font = pygame.font.Font(None, 35)

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == KEYDOWN:
            if event.key == K_f:
                #fire_sound.play()
                player.fire()
            if event.key == K_SPACE:
                #fire_sound.play()
                enemy.fire()

    # Отображение фона и очков игроков
    window.blit(background, (0, 0))

    player_label = font.render('очки зелёного: ' + str(score_player), 1, WHITE)
    enemy_label = font.render('очки желтого: ' + str(score_enemy), 1, WHITE)

    window.blit(player_label, (10, 20))
    window.blit(enemy_label, (505, 20))

    # Сброс и отображение игровых объектов
    player.reset()
    enemy.reset()

    bullets.draw(window)
# Detect collision between bullets and enemy


# Update bullets
    bullets.update()

    # Движение игрока и врага
    player.move()
    enemy.move()

    # Поворот изображений игрока и врага
    player.rotate()
    enemy.rotate()




    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(30)

# Выход из Pygame
pygame.quit()
