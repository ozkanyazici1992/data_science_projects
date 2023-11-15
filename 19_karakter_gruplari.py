import pygame
import random

pygame.init()

genislik = 1000
yukseklik = 750

goruntu_yuzeyi = pygame.display.set_mode((genislik,yukseklik))

FPS = 30
saat = pygame.time.Clock()

class Canavar(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("hayalet.png")
        self.rect = self.image.get_rect()
        self.rect.topleft ( x,y)
        self.hiz = random.randint(1,10)

durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False
pygame.quit()