import pygame

pygame.init()

# Определение констант
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            self.direction = 'up'
        elif keys[pygame.K_s] and self.rect.y < 450:
            self.rect.y += self.speed
            self.direction = 'down'
        elif keys[pygame.K_d] and self.rect.x < 660:
            self.rect.x += self.speed
            self.direction = 'right'
        elif keys[pygame.K_a] and self.rect.x > 0:
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
        if keys[K_UP]:
            self.rect.y -= self.speed
            self.direction = 'up'
        elif keys[K_DOWN]:
            self.rect.y += self.speed
            self.direction = 'down'
        elif keys[K_RIGHT]:
            self.rect.x += self.speed
            self.direction = 'right'
        elif keys[K_LEFT]:
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
        else:  self.image = self.original_image

        def fire(self):
            bullet = Bullet(sprite_img='bullet.png',cord_x=self.rect.centerx,cord_y=self.rect.top,width=20,height=20,speed=20)
            bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
# Создание игровых объектов
player = Player('frie_tank.png', 5, 200, 40, 45, 7)

bullet = Bullet('bullet.png', 350, 200, 20, 10, 20)

bullets = pygame.sprite.Group()

enemys = pygame.sprite.Group()

# Создание окна и настройка отображения
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('танчики')

background = pygame.image.load('black_background.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

score_player = 0
score_enemy = 0

score = 0

finish = False
game_running = True

pygame.font.init()
font = pygame.font.Font(None, 35)

while game_running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_running = False
    # Отображение фона и очков игроков
    window.blit(background, (0, 0))
    player_label = font.render('Твои очки: ' + str(score_player), 1, WHITE)        
    enemy_label = font.render('Очки врага: ' + str(score_enemy), 1, WHITE)

    window.blit(player_label, (10, 20))
    window.blit(enemy_label, (530, 20))

    if pygame.sprite.groupcollide(enemys,bullets,True,True):
            score += 1
            enemy = Enemy('enem_tank.png', 650, 200, 50, 50, 7)
    # Сброс и отображение игровых объектов
        player.reset()
        bullet.reset()

    # Движение игрока и врага
        player.move()

    # Поворот изображений игрока и врага
        player.rotate()

    # Обновление экрана
        pygame.display.flip()

    # Ограничение частоты кадров
        clock.tick(30)

# Выход из Pygame
    pygame.quit()
