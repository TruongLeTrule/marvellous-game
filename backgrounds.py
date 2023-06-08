import pygame
from config import *


class Background():
    """
    A class contain all backgrounds of the game
    , will change the background to suit with the current round
    ...
    Attributes:
    -----------
    round: the current round of game class
        string
    all round surf: the background of each round
        png
    background: the current background
        pygame image

    Methods:
    update: update current background
    draw: draw the background on the game screen
    """

    def __init__(self, round):
        """
        Initialize background when the game is played
        """
        self.round = round

        self.start_screen_surf = pygame.image.load(
            'graphics/backgrounds/start_screen.png').convert()
        self.intro_surf = pygame.image.load(
            'graphics/backgrounds/intro_screen.png').convert()
        self.round1_1_surf = pygame.image.load(
            'graphics/backgrounds/round1_1.png').convert()
        self.round1_2_surf = pygame.image.load(
            'graphics/backgrounds/round1_2.png').convert()
        self.round2_surf = pygame.image.load(
            'graphics/backgrounds/round2.png').convert()
        self.round3_surf = pygame.image.load(
            'graphics/backgrounds/round3.png').convert()
        self.round4_surf = pygame.image.load(
            'graphics/backgrounds/round4.png').convert_alpha()
        self.round5_surf = pygame.image.load(
            'graphics/backgrounds/round5.png').convert()
        self.round6_1_surf = pygame.image.load(
            'graphics/backgrounds/round6_1.png').convert()
        self.round6_2_surf = pygame.image.load(
            'graphics/backgrounds/round6_2.png').convert()
        self.round7_surf = pygame.image.load(
            'graphics/backgrounds/round7.png').convert()
        self.end_screen_surf = pygame.image.load(
            'graphics/backgrounds/end_screen.png').convert()
        self.game_over_surf = pygame.image.load(
            'graphics/backgrounds/game_over_screen.png').convert()

        if self.round == 'start_screen':
            self.background = self.start_screen_surf
        if self.round == 'intro':
            self.background = self.intro_surf
        if self.round == 'round1_1':
            self.background = self.round1_1_surf
        if self.round == 'round1_2':
            self.background = self.round1_2_surf
        if self.round == 'round2':
            self.background = self.round2_surf
        if self.round == 'round3':
            self.background = self.round3_surf
        if self.round == 'round4':
            self.background = self.round4_surf
        if self.round == 'round5':
            self.background = self.round5_surf
        if self.round == 'round6_1':
            self.background = self.round6_1_surf
        if self.round == 'round6_2':
            self.background = self.round6_2_surf
        if self.round == 'round7':
            self.background = self.round7_surf
        if self.round == 'game_over':
            self.background = self.game_over_surf
        if self.round == 'end_screen':
            self.background = self.end_screen_surf

        self.background = pygame.transform.scale(
            self.background, (WIN_WIDTH, WIN_HEIGHT))

    def update(self, round):
        """
        Update current background
        """
        self.round = round
        if self.round == 'start_screen':
            self.background = self.start_screen_surf
        if self.round == 'intro':
            self.background = self.intro_surf
        if self.round == 'round1_1':
            self.background = self.round1_1_surf
        if self.round == 'round1_2':
            self.background = self.round1_2_surf
        if self.round == 'round2':
            self.background = self.round2_surf
        if self.round == 'round3':
            self.background = self.round3_surf
        if self.round == 'round4':
            self.background = self.round4_surf
        if self.round == 'round5':
            self.background = self.round5_surf
        if self.round == 'round6_1':
            self.background = self.round6_1_surf
        if self.round == 'round6_2':
            self.background = self.round6_2_surf
        if self.round == 'round7':
            self.background = self.round7_surf
        if self.round == 'game_over':
            self.background = self.game_over_surf
        if self.round == 'end_screen':
            self.background = self.end_screen_surf

        self.background = pygame.transform.scale(
            self.background, (WIN_WIDTH, WIN_HEIGHT))

    def draw(self, screen, round):
        """
        Draw the background on the game screen
        """
        if round == 'round4':
            screen.fill((255, 255, 255))
        screen.blit(self.background, (0, 0))
