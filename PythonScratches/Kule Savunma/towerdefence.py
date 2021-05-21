"""
    Evde can sikintisindan yaptim piyuv piyuv
    Dusmanlarin gidecegi yollar/mapler eklenebilir.Mermiler zaten gudumlu gidiyor.
    Yeni can ve goruntuye sahip dusmanlar eklenebilir.Mekanizmasi hazir oldugundan kalitim kullanilabilir.

"""
import pygame
from sys import exit
import math
from time import time

window=pygame.display.set_mode((800,600))


class Bullet(pygame.sprite.Sprite):
    _image = pygame.image.load("mermi.png")
    _bullets = pygame.sprite.Group()
    _bulletspeed = 10  #istenen mermi hizi verilebilir
    _bulletdamage = 50 #istenen mermi hasari verilebilir

    def __init__(self,target):
        super().__init__()
        self.image = self._image
        self.rect = self.image.get_rect()
        self.target = target
        Bullet._bullets.add(self)

    @classmethod
    def all_track(cls):
        for bullet in cls._bullets:
            if not bullet.target.alive():
                if not Enemy._enemies:# haritada dusman kalmadiysa havadaki mermiler ne yapilacak?
                    bullet.kill() #belki baska bi zaman yaparim bu kismi
                    continue
                bullet.target = Enemy._enemies.sprites()[0]
            target = bullet.target
            rel_x, rel_y = target.rect.x - bullet.rect.x, target.rect.y - bullet.rect.y
            x = int(math.atan2(rel_y, rel_x) * cls._bulletspeed)
            y = int(1.5*cls._bulletspeed) - abs(x)
            bullet.rect.x += y
            bullet.rect.y += x

    @classmethod
    def from_tower(cls,tower,target):
        new_bullet = cls(target)
        new_bullet.rect.x = tower.rect.centerx
        new_bullet.rect.y = tower.rect.centery



class Tower(pygame.sprite.Sprite):
    _image = pygame.image.load("tower.png")
    _towers = pygame.sprite.Group()
    _firespeed = 20 # her saniye atilacak mermi sayisi degistirilebilir.

    def __init__(self,x,y):
        super().__init__()
        self.image = Tower._image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lastfiretime = 0
        self.target = None
        Tower._towers.add(self)

    def aim(self):
        if Bullet._bullets:
            self.target = Bullet._bullets.sprites()[-1].target
        else:
            self.target = None
    def fire(self):
        self.lastfiretime = time()
        if Enemy._enemies.sprites():
            Bullet.from_tower(self,Enemy._enemies.sprites()[0])


    @classmethod
    def all_fire(cls):
        t = time()
        for tower in cls._towers:
            if t - tower.lastfiretime > 1 / cls._firespeed:
                tower.fire()
            tower.aim()
            if  tower.target:
                target = tower.target
                rel_x, rel_y = target.rect.x - tower.rect.x, target.rect.y - tower.rect.y
                angle = (180 / math.pi) * -math.atan2(rel_x, rel_y)
                tower.image = pygame.transform.rotate(Tower._image,-angle)
                tower.image = pygame.transform.flip(tower.image,True,True)


class Enemy(pygame.sprite.Sprite):
    _image = pygame.image.load("dusman.png")
    _enemies = pygame.sprite.Group()
    _lastspawntime = time()
    _spawnspeed = 30 # her saniye spawn olucak dusman sayisi degistirilebilir
    _movement_speed = 4

    def __init__(self):
        super().__init__()
        self.image = self._image
        self.rect = self.image.get_rect()
        self.health = 100
        Enemy._enemies.add(self)


    def move(self):
        self.rect.x += Enemy._movement_speed


    @classmethod
    def main(cls):
        if time() - Enemy._lastspawntime > 1 / cls._spawnspeed:
            Enemy()
            Enemy._lastspawntime = time()

        for enemy in cls._enemies:
            if pygame.sprite.spritecollide(enemy,Bullet._bullets,dokill=True):
                enemy.health -= Bullet._bulletdamage

            if enemy.health <=0:
                Enemy._enemies.remove(enemy)
                continue

            if enemy.rect.x>800:
                Enemy._enemies.remove(enemy)
                continue

            enemy.move()



def draw_all():
    Tower.all_fire()
    Bullet.all_track()
    Enemy.main()
    Tower._towers.draw(window)
    Bullet._bullets.draw(window)
    Enemy._enemies.draw(window)

clock = pygame.time.Clock()

if __name__ == '__main__':
    while True:
        window.fill((0,0,0))
        clock.tick(60)
        draw_all()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
                Tower(mpos[0],mpos[1])

