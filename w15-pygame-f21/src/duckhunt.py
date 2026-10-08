import pygame
import time, math
from pygame.locals import *
import random
from src.image_manager import ImageManager
from src.sound_manager import SoundManager

"""
    This is the main class for the game.
    It handles the main game loop and the game state.
"""
class DuckHunt:
    def __init__(self, screensize=(1280, 768)):
        self.verbose = False
        self.black, self.white = (0,0,0), (255,255,255)
        self.screensize = screensize

        pygame.init()
        self.screensize = pygame.Rect(0,0, self.screensize[0], self.screensize[1])
        pygame.display.set_caption("Duck Hunt")
        self.screen = pygame.display.set_mode(self.screensize)
        self.sounds = SoundManager
        self.images = ImageManager
        self.mouse_position = (0,0)
        self.click_position = (-100, -100)
        self.shells, self.capacity, self.reloading_time = 3,3,0
        self.is_reloading = False
        self.is_game_over = False

        #self.sounds.gameover.play()

    def loop(self):
        pygame.mouse.set_visable(False)
        bg = pygame.transform.scale(self.images.background, self.screensize)
        self.screen.blit(bg, (0,0))
        #more
        self.screen.covert_alpha()
        pygame.display.update()
        self.handle_events()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTON:
                self.mouse_position = pygame.mouse.get_pos()
                self.images.sight_root.center = self.mouse_position

    def run(self):
        while True:
            self.loop()

    def new_game(self):
        self.score = 0
        self.duck_velocity = 1
        self.duck_angle = 60
        self.is_duck_alive = False
        self.lives = 3
        self.is_game_over = False



if __name__ == '__main__':
    game = DuckHunt
    game.sounds.gameover.play()
