import pygame
import random
from pygame.locals import *
import sys
from GameClass import *


WINDOW_WIDTH = 512
WINDOW_HEIGHT = 700
FRAMES_PER_SECOND = 30
ROAD_LINES = [[0, 128], [256, 384]]

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oCar = Car(window, WINDOW_WIDTH, WINDOW_HEIGHT, 256, 256, 'images/car.png')
oCar.isHealth = True
oRoad1 = Road(window, WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0)
oRoad2 = Road(window, WINDOW_WIDTH, WINDOW_HEIGHT, 0, 512)
oRoad3 = Road(window, WINDOW_WIDTH, WINDOW_HEIGHT, 0, -512)
enemyCar = Car(window, WINDOW_WIDTH, WINDOW_HEIGHT, random.randint(0, 128), -128, 'images/car.png')
test_collider = False

def UpdateRoads():
    oRoad1.Draw()
    oRoad1.Update()

    oRoad2.Draw()
    oRoad2.Update()

    oRoad3.Draw()
    oRoad3.Update()


while True:

    enemyCarRect = pygame.Rect(enemyCar.x, enemyCar.y, enemyCar.width, enemyCar.height)
    oCarRect = pygame.Rect(oCar.x, oCar.y, oCar.width, oCar.height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Прорисовка дороги
    UpdateRoads()

    if test_collider:
        oCar.health -= 1
        print(oCar.health)
        

    # Считывание клавиши и перерисовка машины
    keyPressedTuple = pygame.key.get_pressed()

    if keyPressedTuple[pygame.K_a]:
        oCar.MoveLeft()

    if keyPressedTuple[pygame.K_d]:
        oCar.MoveRight()

    oCar.Draw()

    # Создание машины-препядствия
    if enemyCar.y > WINDOW_HEIGHT:
        random_line = random.randint(0, 1)
        enemyCar = Car(window, WINDOW_WIDTH, WINDOW_HEIGHT, random.randint(*ROAD_LINES[random_line]), -128, 'images/car.png')

    enemyCar.Update()
    enemyCar.Draw()

    test_collider = pygame.Rect.colliderect(enemyCarRect, oCarRect)

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
