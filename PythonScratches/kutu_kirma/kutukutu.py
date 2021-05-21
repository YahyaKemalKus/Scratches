import pygame
from sys import exit

window = pygame.display.set_mode((800,600))
pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 10)
class Block(pygame.sprite.Sprite):
    _image = pygame.image.load("kutu.png")
    _health = 100
    _blocks = pygame.sprite.Group()
    def __init__(self):
        super().__init__()
        self.image = Block._image
        self.rect = self.image.get_rect()
        self.health = Block._health
        self.text = font.render(str(self.health),False,(255,0,0))
        Block._blocks.add(self)

    @classmethod
    def create(cls, x, y):
        new = cls()
        new.rect.x = x
        new.rect.y = y

    @classmethod
    def main(cls,screen):
        Block._blocks.draw(screen)
        for block in cls._blocks:  #bloklarin canlarini ekrana ekleme
            screen.blit(block.text, (block.rect.x+2,block.rect.y))

class Shooter(pygame.sprite.Sprite):
    _image = pygame.image.load("kutu.png")
    def __init__(self):
        super().__init__()
        self.image = Block._image
        self.rect = self.image.get_rect()

class Bullet(pygame.sprite.Sprite):
    _image = pygame.image.load("mermi.png")
    _bullets = pygame.sprite.Group()
    _bulletdamage = 10
    def __init__(self):
        super().__init__()
        self.image = Bullet._image
        self.rect = self.image.get_rect()
        self.vector = [1,-1]
        Bullet._bullets.add(self)

    @classmethod
    def create(cls,x,y):
        new_bullet = cls()
        new_bullet.rect.x=x
        new_bullet.rect.y=y

    @classmethod
    def main(cls,screen):
        for bullet in cls._bullets:
            collided = pygame.sprite.spritecollideany(bullet, Block._blocks)
            if collided:
                collided.health -= Bullet._bulletdamage #blok topla carpistigi icin cani azaldi
                if collided.health <= 0:
                    collided.kill()
                collided.text = font.render(str(collided.health),False,(255,0,0)) #kutunun ekrandaki canini degistirme
                if collided.rect.x + collided.rect.width - 1 == bullet.rect.x:#soldan gelip sag tarafa carptiysa
                    bullet.vector[0] = 1

                if collided.rect.x == bullet.rect.x + bullet.rect.width - 1:#sagdan sola carpma
                    bullet.vector[0] = -1

                if collided.rect.y + collided.rect.height - 1 == bullet.rect.y:#asagidan yukari carpma
                    bullet.vector[1] = 1

                if collided.rect.y == bullet.rect.y + bullet.rect.height - 1:#yukaridan asagi carpma
                    bullet.vector[1] = -1

            bullet.rect.x += bullet.vector[0]
            bullet.rect.y += bullet.vector[1]

        cls._bullets.draw(screen)

clock = pygame.time.Clock()
map1 = str("10"*20+"\n"+"01" *20+"\n")*30

def map_maker(seed,grid_size):
    x, y=0, 0

    for block in seed:
        if block == "1":
            Block.create(x,y)
            x += grid_size
        elif block == "0":
            x += grid_size
        else:
            y += 20
            x = 0

map_maker(map1,20)
def update(screen,fps):
    window.fill((0, 0, 0))
    Bullet.main(screen)
    Block.main(screen)
    pygame.display.update()
    clock.tick(fps)

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                Bullet.create(mx , my)

        update(window,60)