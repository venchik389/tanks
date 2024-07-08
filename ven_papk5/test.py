import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Танки на Pygame')

# Загрузка изображения танка
pla_img = pygame.image.load('frie_tank.png')
pla_img = pygame.transform.scale(pla_img, (46, 50))  # Масштабируем изображение танка

ene_img = pygame.image.load('enem_tank.png')
ene_img = pygame.transform.scale(ene_img, (50, 50))

# Переменные для координат танка и направления
pla_x = SCREEN_WIDTH // 2
pla_y = SCREEN_HEIGHT // 2
pla_direction = 'p_up'  # Начальное направление танка

# Скорость движения танка
pla_speed = 5

ene_x = SCREEN_WIDTH // 2
ene_y = SCREEN_HEIGHT // 2
ene_direction = 'e_up' 

ene_speed = 5

# Основной игровой цикл
running = True
while running:


    screen.fill((0,0,0))
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Получаем нажатые клавиши
    keys = pygame.key.get_pressed()
    
    # Обработка управления танком и поворота изображения
    if keys[pygame.K_a]:
        pla_x -= pla_speed
        pla_direction = 'p_left'
    elif keys[pygame.K_d]:
        pla_x += pla_speed
        pla_direction = 'p_right'
    elif keys[pygame.K_w]:
        pla_y -= pla_speed
        pla_direction = 'p_up'
    elif keys[pygame.K_s]:
        pla_y += pla_speed
        pla_direction = 'p_down'

    # Ограничиваем движение танка в пределах экрана
    pla_x = max(0, min(SCREEN_WIDTH - pla_img.get_width(), pla_x))
    pla_y = max(0, min(SCREEN_HEIGHT - pla_img.get_height(), pla_y))
    
    # Поворот изображения танка в зависимости от направления
    if pla_direction == 'p_left':
        rotated_pla_img = pygame.transform.rotate(pla_img, 90)
    elif pla_direction == 'p_right':
        rotated_pla_img = pygame.transform.rotate(pla_img, -90)
    elif pla_direction == 'p_down':
        rotated_pla_img = pygame.transform.rotate(pla_img, 180)
    else:
        rotated_pla_img = pla_img  # Направление вверх
    
    # Отображение повернутого танка на экране
    rotated_pla_rect = rotated_pla_img.get_rect(center=(pla_x + pla_img.get_width() // 2, pla_y + pla_img.get_height() // 2))
    screen.blit(rotated_pla_img, rotated_pla_rect)
    
    if keys[pygame.K_LEFT]:
        ene_x -= ene_speed
        ene_direction = 'e_left'
    elif keys[pygame.K_RIGHT]:
        ene_x += ene_speed
        ene_direction = 'e_right'
    elif keys[pygame.K_UP]:
        ene_y -= ene_speed
        ene_direction = 'e_up'
    elif keys[pygame.K_DOWN]:
        ene_y += ene_speed
        ene_direction = 'e_down'

    # Ограничиваем движение танка в пределах экрана
    ene_x = max(0, min(SCREEN_WIDTH - ene_img.get_width(), ene_x))
    ene_y = max(0, min(SCREEN_HEIGHT - ene_img.get_height(), ene_y))
    
    # Поворот изображения танка в зависимости от направления
    if ene_direction == 'e_left':
        rotated_ene_img = pygame.transform.rotate(ene_img, 90)
    elif ene_direction == 'e_right':
        rotated_ene_img = pygame.transform.rotate(ene_img, -90)
    elif ene_direction == 'e_down':
        rotated_ene_img = pygame.transform.rotate(ene_img, 180)
    else:
        rotated_ene_img = ene_img  # Направление вверх
    
    # Отображение повернутого танка на экране
    rotated_ene_rect = rotated_ene_img.get_rect(center=(ene_x + ene_img.get_width() // 2, ene_y + ene_img.get_height() // 2))
    screen.blit(rotated_ene_img, rotated_ene_rect)

    # Обновление экрана
    pygame.display.flip()
    
    # Задержка, чтобы не грузить процессор слишком сильно
    pygame.time.Clock().tick(30)

# Выход из Pygame
pygame.quit()
sys.exit()
