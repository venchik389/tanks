from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img ,cord_x ,cord_y ,width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_img),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y
        self.speed = speed

    def reset(self):
        rotated_pla_rect = self.image.get_rect(center=(self.rect.x + self.image.get_width() // 2, self.rect.y + self.image.get_height() // 2))
        window.blit(self.image, rotated_pla_rect)


    def move(self):
        global direction

        povorot = False

        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= 7
            direction = 'up'
            povorot = True
        if keys[K_s]:
            self.rect.y += 7
            direction = 'down'
            povorot = True
        if keys[K_d]:
            self.rect.x += 7
            direction = 'right'
            povorot = True
        if keys[K_a]:
            self.rect.x -= 7
            direction = 'left'
            povorot = True

        if direction == 'left' and povorot == True:
            self.image = transform.rotate(self.image, 90)
        elif direction == 'right' and povorot == True:
            self.image = transform.rotate(self.image, -90)
        elif direction == 'down' and povorot == True:
            self.image = transform.rotate(self.image, 180)
        else:
            self.image = player.image  # Направление вверх
        
player = GameSprite('frie_tank.png',5,200,40,45,10)
enemy = GameSprite('enem_tank.png',650,200,50,50,10)
bullet = GameSprite('bullet.png',350,200,20,10,20)


window = display.set_mode((700,500))
display.set_caption('танчики')

background = image.load('black_background.jpg')
background = transform.scale(background,(700,500))

clock = time.Clock()

score_player = 0
score_enemy = 0

finish = False
game = True

font.init()
font1 = font.Font(None,35)


direction = ' '

while game:

    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        window.fill( (0,0,0))

    player_label = font1.render('Твои очки:' + str(score_player),1,(255,255,255))
    enemy_label = font1.render('Очки врага:' + str(score_enemy),1,(255,255,255))

    window.blit(player_label,(10,20))
    window.blit(enemy_label,(530,20))

    player.reset()
    enemy.reset()
    bullet.reset()

    player.move()
    
    clock.tick(30)
    display.flip()



