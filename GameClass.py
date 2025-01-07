import pygame
from pygame.locals import *

class Car():
    def __init__(self, window, width_window, height_window, x, y, image_path):
        self.window = window
        self.width_window = width_window
        self.height_window = height_window
        self.image = pygame.image.load(image_path)

        carRect = self.image.get_rect()
        self.width = carRect.width
        self.height = carRect.height

        self.max_width = width_window - self.width
        self.max_height = height_window - self.height

        self.x = x
        self.y = y

        self.speed_x = 10
        self.speed_y = 10
    
    def Update(self):
        if self.y < self.height_window:
            self.y += self.speed_y * 2

    def MoveLeft(self):
        
        if self.x > 0:
            self.x -= self.speed_x

    def MoveRight(self):

        if self.x <=  self.max_width:
            self.x += self.speed_x

    def Draw(self):
        self.window.blit(self.image, (self.x, self.y))


class Road():
    def __init__(self, window, window_width, window_height, x, y):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        self.image = pygame.image.load('images/road.jpg')
        self.roadRect = self.image.get_rect()

        self.width = self.roadRect.width
        self.height = self.roadRect.height

        self.x = x
        self.y = y

        self.speed_y = 10

    def Update(self):

        if self.y < self.window_height:
            self.y += self.speed_y
        else:
            self.y = -512
    
    def Draw(self):
        # self.window.fill((0,0,0))
        self.window.blit(self.image, (self.x, self.y))
        