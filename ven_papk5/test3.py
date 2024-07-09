from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img , x ,y):
        super().__init__()
        self.image = transform.scale(image.load(img),(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[K_s] and self.rect.y < 440:
            self.rect.y += 5
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[K_d] and self.rect.x < 640:
            self.rect.x += 5

class Enemy(GameSprite):
    def move(self):
        if self.rect.x <= 400:
            self.side = 'право'
        if self.rect.x >= 640:
            self.side = 'лево'

        if self.side == 'лево':
            self.rect.x -= 5
        else:
            self.rect.x += 5

class Wall(sprite.Sprite):
    def __init__(self,x,y,w,h):
        super().__init__()
        self.width = w
        self.height = h 
        self.wall = Surface((self.width,self.height))
        self.wall.fill((0,255,255))
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        window.blit(self.wall,(self.rect.x,self.rect.y))

wall_1 = Wall(20,20,20,500)
wall_2 = Wall(20,20,500,20)
wall_3 = Wall(100,100,400,20)

player = Player('frie_tank.png',300,300)
enemy = Enemy('enem_tank.png',350,200)
goal = GameSprite('bullet.png',600,400)

window = display.set_mode((700,500))
display.set_caption('ИГРА ЛАБИРИНТ')

background =  transform.scale(image.load('black_background.jpg'),(700,500))


font.init()
font_for_game = font.Font(None,100)
win = font_for_game.render('YOU WIN',1,(0,255,0))
lose = font_for_game.render('YOU LOSE',1,(255,0,0))

clock = time.Clock()

finish = False
game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        
        player.update()
        player.move()

        enemy.update()
        enemy.move()

        goal.update()

        wall_1.update()
        wall_2.update()
        wall_3.update()

        if sprite.collide_rect(player,goal):
            window.blit(win,(150,250))
            finish = True

        if sprite.collide_rect(player,enemy):
            window.blit(lose,(150,250))
            finish = True

    clock.tick(60)
    display.update()