import pygame
import time
import threading
from config import *

# ==============Player================


class Player(pygame.sprite.Sprite):
    """
    Player sprite class will create a main player
    ...
    Attributes
    ----------
    game: access all game class attribute
        game class of main file
    facing: player direction
        string
    _layer: order of draw sprites
        int
    groups: all sprites of the game
        game sprites
    round_updated: control player update in new round
        bool
    player_index: control player images
        int
    image: player's current image
        png file
    rect: image with rectangle around to control position more easily
        pygame rect
    all sound attribute: player's sound each round

    Methods
    -------
    player_input: 
        receive player input and do the request
    animation_state:
        make player move by direction
    new_round:
        set all attribute to default
    play_sound:
        play player sound
    all round function: 
        control specific round
    round_update:
        run all round function if its condition is true
    update:
        run all function 
    """

    def __init__(self, game):
        """
        Initialize player sprite

            Parameter:
                game (Game class): Game class in main file  
        """
        super().__init__()

        self.game = game
        self.facing = 'right'
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.round_updated = False

        player_run1 = pygame.transform.scale_by(pygame.image.load(
            'graphics/player/player_run1.png').convert_alpha(), (0.8, 0.8))
        player_run2 = pygame.transform.scale_by(pygame.image.load(
            'graphics/player/player_run2.png').convert_alpha(), (0.8, 0.8))
        player_run3 = pygame.transform.scale_by(pygame.image.load(
            'graphics/player/player_run3.png').convert_alpha(), (0.8, 0.8))
        player_run4 = pygame.transform.scale_by(pygame.image.load(
            'graphics/player/player_run4.png').convert_alpha(), (0.8, 0.8))
        player_run5 = pygame.transform.scale_by(pygame.image.load(
            'graphics/player/player_run5.png').convert_alpha(), (0.8, 0.8))
        player_run6 = pygame.transform.scale_by(pygame.image.load(
            'graphics/player/player_run6.png').convert_alpha(), (0.8, 0.8))
        player_run7 = pygame.transform.scale_by(pygame.image.load(
            'graphics/player/player_run7.png').convert_alpha(), (0.8, 0.8))
        player_run8 = pygame.transform.scale_by(pygame.image.load(
            'graphics/player/player_run8.png').convert_alpha(), (0.8, 0.8))
        self.player_run = [player_run1, player_run2, player_run3,
                           player_run4, player_run5, player_run6, player_run7, player_run8]
        self.player_index = 0
        self.image = self.player_run[self.player_index]
        self.rect = self.image.get_rect(midbottom=(5, 600))

        # Round 1 sound
        self.round1_sound = pygame.mixer.Sound('sound/player/round1_1.wav')

        # Round 3 sound
        self.round3_help_lion = pygame.mixer.Sound(
            'sound/player/round3_help_lion.wav')
        self.round3_win = pygame.mixer.Sound('sound/player/round3_win.wav')

        # Round 4 sound
        self.round4_see_rabbit = pygame.mixer.Sound(
            'sound/player/round4_see_rabbit.wav')
        self.round4_thanks = pygame.mixer.Sound(
            'sound/player/round4_thanks.wav')
        self.round4_reply = pygame.mixer.Sound('sound/player/round4_reply.wav')

        # Round 5 sound
        self.round5_start = pygame.mixer.Sound('sound/player/round5_start.wav')
        self.round5_thanks = pygame.mixer.Sound(
            'sound/player/round5_thanks.wav')
        self.round5_bye = pygame.mixer.Sound('sound/player/round5_bye.wav')

        # Round 6 sound
        self.round6_1_start = pygame.mixer.Sound(
            'sound/player/round6_1_start.wav')
        self.round6_2_win = pygame.mixer.Sound('sound/player/round6_2_win.wav')
        self.round6_2_end = pygame.mixer.Sound('sound/player/round6_2_end.wav')

        # Round 7 sound
        self.round7_sound = pygame.mixer.Sound('sound/player/round7_win.wav')

    def player_input(self):
        """
        Check player inputs
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x <= 720:
            self.facing = 'right'
            self.animation_state()
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.facing = 'left'
            self.animation_state()
            self.rect.x -= PLAYER_SPEED

    def animation_state(self):
        """"
        Control player directions and x_pos
        """
        self.player_index += PLAYER_MOVEMENT
        if self.player_index >= len(self.player_run):
            self.player_index = 0
        self.image = self.player_run[int(self.player_index)]
        if self.facing == 'left':
            self.image = pygame.transform.rotate(
                pygame.transform.flip(self.image, False, True), 180)

    # Update player each new round
    def new_round(self):
        """
        Set player attribute for new round
        """
        if self.game.current_round == 'round1_2':
            self.rect.midbottom = (5, 545)
        elif self.game.current_round == 'round2':
            self.rect.midbottom = (5, 490)
        elif self.game.current_round == 'round3':
            self.rect.midbottom = (5, 530)
        elif self.game.current_round == 'round4':
            self.rect.midbottom = (5, 400)
        elif self.game.current_round == 'round5':
            self.rect.midbottom = (5, 450)
        elif self.game.current_round == 'round6_1':
            self.rect.midbottom = (5, 535)
        else:
            self.rect.midbottom = (5, 600)
        self.round_updated = True

    def play_sound(self):
        """
        Play player's sound
        """
        pygame.mixer.stop()
        # Round 1
        if self.game.current_round == 'round1_1' and pygame.mixer.get_busy() == False:
            self.round1_sound.play()

        # Round 3
        elif self.game.current_round == 'round3' and pygame.mixer.get_busy() == False:
            if self.game.round_event == 2:
                self.round3_help_lion.play()

            if self.game.round_event == 7:
                self.round3_win.play()

        # Round 4
        elif self.game.current_round == 'round4' and pygame.mixer.get_busy() == False:
            if self.game.round_event == 1:
                self.round4_see_rabbit.play()
            if self.game.round_event == 4:
                self.round4_thanks.play()
            if self.game.round_event == 7:
                self.round4_reply.play()

        # Round 5
        elif self.game.current_round == 'round5' and pygame.mixer.get_busy() == False:
            if self.game.round_event == 1:
                self.round5_start.play()
            elif self.game.round_event == 4:
                self.round5_thanks.play()
            elif self.game.round_event == 6:
                self.round5_bye.play()

        # Round 6
        elif self.game.current_round == 'round6_1' and pygame.mixer.get_busy() == False:
            self.round6_1_start.play()

        elif self.game.current_round == 'round6_2' and pygame.mixer.get_busy() == False:
            if self.game.round_event == 0:
                self.round6_2_win.play()
            elif self.game.round_event == 2:
                self.round6_2_end.play()

        elif self.game.current_round == 'round7' and pygame.mixer.get_busy() == False:
            self.round7_sound.play()

    def round1(self):
        """
        Control round 1 events
        """
        if self.game.current_round == 'round1_1':
            if self.game.round_event == 2:
                self.play_sound()
                self.game.round_event += 1
            # Collect 3 items
            if self.game.win_round == 3:
                if self.rect.x >= 720:
                    self.game.next_round = 1
                    self.round_updated = False

        elif self.game.current_round == 'round1_2':
            # Step up the wood
            if self.rect.x >= 225 and self.game.round_event == 0:
                self.rect.bottom = 497
                self.game.round_event += 1

            # Pass round
            if self.game.round_event == 1 and self.rect.x >= 720:
                self.game.next_round = 1
                self.round_updated = False

    def round2(self):
        """
        Control round 2 events
        """
        # Pass round
        if self.game.win_round == 2 and self.rect.x >= 720:
            self.game.next_round = 1
            self.round_updated = False

    def round3(self):
        """
        Control round 3 events
        """
        # Event 2: See the hurt lion
        if self.game.round_event == 2:
            if pygame.mixer.get_busy() == False:
                self.play_sound()
                self.game.round_event += 1

        # Event 7: player script
        if self.game.round_event == 7:
            if pygame.mixer.get_busy() == False:
                self.play_sound()
                self.game.round_event += 1

        # Event 8: Player done script
        if self.game.round_event == 8:
            if pygame.mixer.get_busy() == False:
                self.game.win_round = 1

        # Pass round
        if self.game.win_round and self.rect.x >= 720:
            self.game.next_round = 1
            self.kill()
            self.round_updated = False

    def round4(self):
        """
        Control round 4 events
        """
        # Event 1: Player see the rabbit, appear
        if self.game.round_event == 1:
            if pygame.mixer.get_busy() == False:
                self.play_sound()
                self.game.round_event += 1
                self.game.items_created = 0

        # Event 4: Player thanks
        if self.game.round_event == 4:
            if pygame.mixer.get_busy() == False:
                self.play_sound()
                self.game.round_event += 1

        # Event 7: Player reply
        if self.game.round_event == 7:
            if pygame.mixer.get_busy() == False:
                self.play_sound()
                self.game.round_event += 1

        # Event 8: Player end script and end
        if self.game.round_event == 8 and pygame.mixer.get_busy() == False:
            self.game.win_round = 1

        # Pass round
        if self.game.win_round and self.rect.x >= 720:
            self.game.next_round = 1
            self.round_updated = False

    def round5(self):
        """
        Control round 5 events
        """
        # Event 1: player see elephant is captured
        if self.game.round_event == 1 and pygame.mixer.get_busy() == False:
            self.play_sound()
            self.game.round_event += 1
        # Event 4: player reply the elephant thanks
        elif self.game.round_event == 4 and pygame.mixer.get_busy() == False:
            self.play_sound()
            self.game.round_event += 1
        # Event 6: Bye elephant
        elif self.game.round_event == 6 and pygame.mixer.get_busy() == False:
            self.play_sound()
            self.game.round_event += 1

        # Pass round
        elif self.game.win_round == 2 and self.rect.x >= 720:
            self.game.next_round = 1
            self.round_updated = False
        # Event 7: Done script
        elif self.game.win_round == 1:
            self.game.win_round += 1

    def round6_1(self):
        """
        Control round 6_1 events
        """
        # Event 0: Player surprise
        if self.game.round_event == 0:
            self.play_sound()
            self.game.round_event += 1
        # Event 1: Player done script and collect items
        elif self.game.round_event == 1 and pygame.mixer.get_busy() == False:
            self.game.round_event += 1
            self.game.items_created = 0
        # Win round: Put three items together
        elif self.game.win_round == 3:
            self.game.next_round = 1
            self.round_updated = 0

    def round6_2(self):
        """
        Control round 2 events
        """
        # Event 0: see the new world
        if self.game.round_event == 0:
            self.play_sound()
            self.game.round_event += 1
            self.game.items_created = 0
        # Event 2
        elif self.game.round_event == 2 and pygame.mixer.get_busy() == False:
            self.play_sound()
            self.game.round_event += 1
        # Event 3
        elif self.game.round_event == 3 and pygame.mixer.get_busy() == False:
            self.game.win_round += 1
            self.game.round_event += 3
        elif self.game.win_round and self.rect.x >= 720:
            self.game.next_round = 1
            self.round_updated = 0

    def round7(self):
        """
        Control round 7 events
        """
        # Event 2: player get speaker and speak
        if self.game.round_event == 2:
            self.play_sound()
            self.game.round_event += 1
        # Event 3: player done script
        elif self.game.round_event == 3 and pygame.mixer.get_busy() == False:
            self.game.win_round = 1
            self.game.round_event += 1
        # End game
        elif self.game.win_round:
            self.game.end_game = 1

    def round_update(self):
        """
        Run round function when current round is this round
        """
        if self.round_updated == False:
            self.new_round()

        if self.game.current_round == 'round1_1' or self.game.current_round == 'round1_2':
            self.round1()
        elif self.game.current_round == 'round2':
            self.round2()
        elif self.game.current_round == 'round3':
            self.round3()
        elif self.game.current_round == 'round4':
            self.round4()
        elif self.game.current_round == 'round5':
            self.round5()
        elif self.game.current_round == 'round6_1':
            self.round6_1()
        elif self.game.current_round == 'round6_2':
            self.round6_2()
        elif self.game.current_round == 'round7':
            self.round7()

    def update(self):
        """
        Run all functions
        """
        self.round_update()
        self.player_input()
        """"

"""
# ==============Fairy================


class Fairy(pygame.sprite.Sprite):
    """
    Fairy sprite class will create NPC of this game, will give introduction to player
    ...
    Attributes
    ----------
    game: access all game class attribute
        game class of main file
    _layer: order of draw sprites
        int
    groups: all sprites of the game
        game sprites
    round_updated: control player update in new round
        bool
    sound_is_playing: control the fairy sound
        bool
    image: current image
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    all sound file: store fairy sound
        wav

    Methods
    -------
    new_round:
        set all attribute to default
    play_sound:
        play player sound
    all round function: 
        control specific round
    round_update:
        run all round function if its condition is true
    update:
        run all functions
    """

    def __init__(self, game):
        """"
        Initialize fairy
        """
        super().__init__()
        pygame.mixer.init()
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self._layer = SUB_CHAR
        self.sound_is_playing = False
        self.round_updated = False  # Check if start position of each round is updated

        self.image = pygame.transform.scale_by(pygame.image.load(
            'graphics/fairy/fairy.png').convert_alpha(), (0.8, 0.8))
        self.rect = self.image.get_rect(center=(730, 250))

        # Import fairy's voice
        self.intro_sound = pygame.mixer.Sound('sound/fairy/intro.wav')
        self.round1_1_sound = pygame.mixer.Sound('sound/fairy/round1.wav')
        self.round2_sound = pygame.mixer.Sound('sound/fairy/round2.wav')
        self.round6_1_sound = pygame.mixer.Sound('sound/fairy/round6_1.wav')
        self.round6_2_sound = pygame.mixer.Sound('sound/fairy/round6_2.wav')

    def update(self):
        """
        Run all fairy functions
        """
        self.round_update()

    def play_sound(self):
        """"
        Play fairy sound
        """
        self.game.skip_btn = SkipButton(self.game)
        pygame.mixer.stop()
        # Intro
        if self.game.current_round == 'intro' and pygame.mixer.get_busy() == False:
            if self.game.round_event == 0:
                self.sound_is_playing = True
                self.intro_sound.play()

        # Round 1
        if self.game.current_round == 'round1_1' and pygame.mixer.get_busy() == False:
            self.sound_is_playing = True
            self.round1_1_sound.play()

        # Round 2
        if self.game.current_round == 'round2' and pygame.mixer.get_busy() == False:
            self.sound_is_playing = True
            self.round2_sound.play()

        # Round 6
        if self.game.current_round == 'round6_1' and pygame.mixer.get_busy() == False:
            self.sound_is_playing = True
            self.round6_1_sound.play()

        if self.game.current_round == 'round6_2' and pygame.mixer.get_busy() == False:
            self.sound_is_playing = True
            self.round6_2_sound.play()

    def new_round(self):
        if self.game.current_round == 'round1_1':
            self.rect.midbottom = (700, 600)
            self.round_updated = True
        elif self.game.current_round == 'round2':
            self.rect.midbottom = (600, 320)
            self.round_updated = True
        elif self.game.current_round == 'round6_1':
            self.rect.midbottom = (600, 320)
            self.round_updated = True
        elif self.game.current_round == 'round6_2':
            self.rect.midbottom = (600, 320)
            self.round_updated = True

    def intro(self):
        """
        control intro events
        """
        if self.game.round_event == 0:
            self.play_sound()
            self.game.round_event += 1

        # Check if the fairy done the intro script
        if self.game.round_event == 1 and pygame.mixer.get_busy() == False:
            self.sound_is_playing = False
            self.game.next_round = 1
            self.round_updated = False

        # Skip button is clicked
        if self.game.next_round == 1:
            pygame.mixer.stop()

    def round1(self):
        """
        control round1 events
        """
        if self.game.current_round == 'round1_1':
            # Check if player collide with fairy
            if self.game.round_event == 0 and self.rect.colliderect(self.game.player):
                self.play_sound()
                self.rect.x -= 100
                self.rect.y -= 280
                self.game.round_event += 1  # Fairy start the script

            # Check if the fairy done the round 1_1 script
            if self.game.round_event == 1 and pygame.mixer.get_busy() == False:
                self.game.round_event += 1
                self.game.items_created = 0
                self.sound_is_playing = False
                self.round_updated = False
                self.kill()

            # Skip button is clicked
            if self.game.round_event == 2:
                pygame.mixer.stop()
                self.game.items_created = 0
                self.sound_is_playing = False
                self.round_updated = False
                self.kill()

    def round2(self):
        """
        control round2 events
        """
        # Event 0
        if self.game.round_event == 0:
            self.play_sound()
            self.game.round_event += 1

        # Event 1: Check if the fairy done script
        if self.game.round_event == 1 and pygame.mixer.get_busy() == False:
            self.sound_is_playing = False
            self.round_updated = False
            self.game.items_created = 0
            self.kill()

    def round6_1(self):
        """
        control round6_1 events
        """
        # Event 2
        if self.game.round_event == 2 and pygame.mixer.get_busy() == False:
            self.play_sound()
            self.game.round_event += 1
        # Event 3: fairy done script
        if self.game.round_event == 3 and pygame.mixer.get_busy() == False:
            self.sound_is_playing = False
            self.round_updated = False
            self.kill()

    def round6_2(self):
        """
        control round6_2 events
        """
        # Event 1
        if self.game.round_event == 1:
            self.play_sound()
            self.game.round_event += 1
        # Event 2
        elif self.game.round_event == 2 and pygame.mixer.get_busy() == False:
            self.sound_is_playing = False
            self.round_updated = False
            self.kill()

    def round_update(self):
        """
        run round function if current round is this round
        """
        if self.round_updated == False:
            self.new_round()

        if self.game.current_round == 'intro':
            self.intro()
        elif self.game.current_round == 'round1_1':
            self.round1()
        elif self.game.current_round == 'round2':
            self.round2()
        elif self.game.current_round == 'round6_1':
            self.round6_1()
        elif self.game.current_round == 'round6_2':
            self.round6_2()

# ==============Rhino================


class Rhino(pygame.sprite.Sprite):
    """
    Rhino sprite class will create a rhino in round 2, give new item if player win this round  
    ...
    Attributes
    ----------
    game: access all game class attribute
        game class of main file
    _layer: order of draw sprites
        int
    groups: all sprites of the game
        game sprites
    rhino_before: list of rhino images in start of round
        pygame image
    rhino_after: list of rhino images when player make a right move
        pygame image
    rhino_index: control rhino move images
        int
    image: current image
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    all sound file: store rhino sound
        wav
    die: get to know when rhino is killed by player and game over
        bool

    Methods
    -------
    play_sound:
        play player sound
    round_update:
        run round function if its condition is true
    update:
        run all functions
    move: 
        make the rhino move 
    """

    def __init__(self, game):
        """
        Initialize Rhino
        """
        super().__init__()

        self.game = game
        self._layer = SUB_CHAR
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        rhino_before1 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/before/rhino_before1.png').convert_alpha(), (0.8, 0.8))
        rhino_before2 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/before/rhino_before2.png').convert_alpha(), (0.8, 0.8))
        rhino_before3 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/before/rhino_before3.png').convert_alpha(), (0.8, 0.8))
        rhino_before4 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/before/rhino_before4.png').convert_alpha(), (0.8, 0.8))
        rhino_before5 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/before/rhino_before5.png').convert_alpha(), (0.8, 0.8))
        rhino_before6 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/before/rhino_before6.png').convert_alpha(), (0.8, 0.8))

        rhino_after1 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/after/rhino_after1.png').convert_alpha(), (0.69, 0.69))
        rhino_after2 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/after/rhino_after2.png').convert_alpha(), (0.69, 0.69))
        rhino_after3 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/after/rhino_after3.png').convert_alpha(), (0.69, 0.69))
        rhino_after4 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/after/rhino_after4.png').convert_alpha(), (0.69, 0.69))
        rhino_after5 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/after/rhino_after5.png').convert_alpha(), (0.69, 0.69))
        rhino_after6 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/after/rhino_after6.png').convert_alpha(), (0.69, 0.69))

        self.rhino_die = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rhino/rhino_die.png').convert_alpha(), (0.8, 0.8))

        self.rhino_before = [rhino_before1, rhino_before2,
                             rhino_before3, rhino_before4, rhino_before5, rhino_before6]
        self.rhino_after = [rhino_after1, rhino_after2,
                            rhino_after3, rhino_after4, rhino_after5, rhino_after6]

        self.rhino_index = 0
        self.image = self.rhino_before[self.rhino_index]
        self.rect = self.image.get_rect(midbottom=(800, 490))

        self.die = False
        self.rhino_sound = pygame.mixer.Sound('sound/rhino/rhino.wav')
        self.rhino_die_sound = pygame.mixer.Sound('sound/rhino/rhino_die.wav')
        self.rhino_win_sound = pygame.mixer.Sound('sound/rhino/rhino_win.wav')

    def move(self):
        """"
        Make the rhino move
        """
        if self.game.round_event == 1:
            self.rhino_index += 0.14
            self.rect.x -= 3
            if self.rhino_index >= len(self.rhino_before):
                self.rhino_index = 0
            self.image = self.rhino_before[int(self.rhino_index)]

        if self.game.round_event == 5:
            self.rhino_index += 0.14
            self.rect.x += 3.5
            if self.rhino_index >= len(self.rhino_after):
                self.rhino_index = 0
            self.image = self.rhino_after[int(self.rhino_index)]

        if self.die:
            self.image = self.rhino_die

    def update(self):
        """
        Run all function
        """
        self.round_update()

    def play_sound(self):
        """"
        Play Rhino sounds
        """
        pygame.mixer.stop()
        if self.game.round_event == 1 and pygame.mixer.get_busy() == False:
            self.rhino_sound.play()

        if self.game.round_event == 3 and pygame.mixer.get_busy() == False:
            self.rhino_win_sound.play()

        if self.die and pygame.mixer.get_busy() == False:
            self.rhino_die_sound.play()

    def round_update(self):
        """"
        Update round event
        """
        # Event 1: Rhino move close to player, start script and wait for the horn
        if self.game.round_event == 1:
            if self.rect.x >= 400:
                self.move()
            else:
                self.play_sound()
                self.game.round_event += 1

        # Event 3: Get the horn
        if self.game.round_event == 3 and pygame.mixer.get_busy() == False:
            self.image = pygame.transform.rotate(
                pygame.transform.flip(self.rhino_after[0], False, True), 180)
            self.play_sound()
            self.game.round_event += 1

        # Event 4: Done script
        if self.game.round_event == 4:
            if pygame.mixer.get_busy() == False:
                self.game.items_created = 0
                self.game.round_event += 1

        # Event 5: Rhino run away
        if self.game.round_event == 5:
            self.move()
            if self.rect.x >= 720:
                self.game.win_round += 1
                self.kill()

        # Killed by the saw
        if self.game.round_event == 2 and self.rect.colliderect(self.game.saw) and self.die == False:
            self.die = True
            self.play_sound()
            self.game.items_created = 0

        # Game_over
        if self.die and pygame.mixer.get_busy() == False:
            self.game.game_over_flag = 1
            self.kill()

# ==============Lion=================


class Lion(pygame.sprite.Sprite):
    """
    Lion sprite class will create a lion in round 3
    ...
    Attributes
    ----------
    game: access all game class attribute
        game class of main file
    _layer: order of draw sprites
        int
    groups: all sprites of the game
        game sprites
    lion_run: list of lion run movement images
        pygame image
    lion_run_index: control lion run movement
        int
    image: current image
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    all sound file: store rabbit sound
        wav
    die: get to know when rabbit is killed by player and game over
        bool

    Methods
    -------
    play_sound:
        play player sound
    round_update:
        run round function if its condition is true
    update:
        run all functions
    move: 
        make the rhino move 
    """

    def __init__(self, game):
        """"
        Initialize lion in start of round 3
        """
        super().__init__()

        self.game = game
        self._layer = SUB_CHAR
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        lion_run1 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/lion/lion_run1.png').convert_alpha(), (0.8, 0.8))
        lion_run2 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/lion/lion_run2.png').convert_alpha(), (0.8, 0.8))
        lion_run3 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/lion/lion_run3.png').convert_alpha(), (0.8, 0.8))
        self.lion_win = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/lion/lion_win.png').convert_alpha(), (0.8, 0.8))
        self.lion_die = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/lion/lion_die.png').convert_alpha(), (0.8, 0.8))
        self.lion_hurt = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/lion/lion_hurt.png').convert_alpha(), (0.8, 0.8))

        self.lion_run = [lion_run1, lion_run2, lion_run3]
        self.lion_run_index = 0
        self.image = self.lion_run[self.lion_run_index]
        self.rect = self.image.get_rect(midbottom=(800, 530))

        self.die = False

        self.touch_nail_sound = pygame.mixer.Sound('sound/lion/touch_nail.wav')
        self.win_sound = pygame.mixer.Sound('sound/lion/win.wav')
        self.die_sound = pygame.mixer.Sound('sound/lion/die.wav')

    def move(self):
        """"
        Control the lion movement
        """
        if self.game.round_event == 6:
            self.lion_run_index += 0.14
            self.rect.x += 3.5
            if self.lion_run_index >= len(self.lion_run):
                self.lion_run_index = 0
        self.image = self.lion_run[int(self.lion_run_index)]
        if self.game.round_event == 0:
            self.lion_run_index += 0.14
            self.rect.x -= 3
            if self.lion_run_index >= len(self.lion_run):
                self.lion_run_index = 0
            self.image = pygame.transform.rotate(
                pygame.transform.flip(self.image, False, True), 180)

    def update(self):
        """
        Run all round update function
        """
        self.round_update()

    def play_sound(self):
        """
        Play the lion sound
        """
        pygame.mixer.stop()
        if self.game.round_event == 1 and pygame.mixer.get_busy() == False:
            self.touch_nail_sound.play()

        if self.game.round_event == 4 and pygame.mixer.get_busy() == False:
            self.win_sound.play()

        if self.die and pygame.mixer.get_busy() == False:
            self.die_sound.play()

    def round_update(self):
        """"
        Update lion events all over the round
        """
        # Event 0: Lion run and touch the nail then get hurt
        if self.game.round_event == 0:
            self.move()

        # Event 1: Wait for player help
        if self.game.round_event == 1:
            self.play_sound()
            self.image = pygame.transform.rotate(
                pygame.transform.flip(self.lion_hurt, False, True), 180)
            self.game.round_event += 1

        # Event 4: Get player help
        if self.game.round_event == 4:
            self.image = self.lion_win
            self.play_sound()
            self.game.round_event += 1

        # Event 5: Done script
        if self.game.round_event == 5:
            if pygame.mixer.get_busy() == False:
                self.game.round_event += 1

        # Event 6: Lion run away
        if self.game.round_event == 6:
            self.move()
            if self.rect.x >= 720:
                self.game.round_event += 1
                self.kill()

        # Killed by the saw
        if self.game.round_event == 3 and self.rect.colliderect(self.game.saw) and self.die == False:
            self.die = True
            self.play_sound()
            self.game.items_created = 1

        # Game_over
        if self.die and pygame.mixer.get_busy() == False:
            self.game.game_over_flag = 1
            self.kill()

# ==============Rabbit================


class Rabbit(pygame.sprite.Sprite):
    """
    Rabbit sprite class will create a rabbit in round 4
    ...
    Attributes
    ----------
    game: access all game class attribute
        game class of main file
    _layer: order of draw sprites
        int
    groups: all sprites of the game
        game sprites
    rabbit_run: list of rabbit run movement images
        pygame image
    rabbit_run_index: control rabbit run movement
        int
    image: current image
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    all sound file: store rabbit sound
        wav
    die: get to when the rabbit is killed by player and game over
        bool

    Methods
    -------
    play_sound:
        play player sound
    round_update:
        run round function if its condition is true
    update:
        run all functions
    move: 
        make the rhino move 
    """

    def __init__(self, game):
        super().__init__()

        self.game = game
        self._layer = SUB_CHAR
        self.direction = 'left'
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        rabbit_run1 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rabbit/rabbit_run1.png').convert_alpha(), (0.8, 0.8))
        rabbit_run2 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rabbit/rabbit_run2.png').convert_alpha(), (0.8, 0.8))
        rabbit_run3 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rabbit/rabbit_run3.png').convert_alpha(), (0.8, 0.8))
        self.rabbit_cry = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/rabbit/rabbit_cry.png').convert_alpha(), (0.8, 0.8))

        self.rabbit_run = [rabbit_run1, rabbit_run2, rabbit_run3]
        self.rabbit_run_index = 0
        self.image = self.rabbit_run[self.rabbit_run_index]
        self.rect = self.image.get_rect(midbottom=(800, 600))
        # Count round rabbit run in event 0
        self.round_count = 0

        self.die = False

        self.rabbit_hungry_sound = pygame.mixer.Sound(
            'sound/rabbit/rabbit_hungry.wav')
        self.rabbit_get_food = pygame.mixer.Sound(
            'sound/rabbit/rabbit_get_food.wav')
        self.rabbit_win = pygame.mixer.Sound('sound/rabbit/rabbit_win.wav')
        self.rabbit_die_sound = pygame.mixer.Sound(
            'sound/rabbit/rabbit_die.wav')

    def move(self):
        """
        Control rabbit movement
        """
        if self.direction == 'right':
            self.rabbit_run_index += 0.14
            self.rect.x += 5
            if self.rabbit_run_index >= len(self.rabbit_run):
                self.rabbit_run_index = 0
        self.image = self.rabbit_run[int(self.rabbit_run_index)]
        if self.direction == 'left':
            self.rabbit_run_index += 0.14
            self.rect.x -= 5
            if self.rabbit_run_index >= len(self.rabbit_run):
                self.rabbit_run_index = 0
            self.image = pygame.transform.rotate(
                pygame.transform.flip(self.image, False, True), 180)

    def update(self):
        """
        Run all round update functions
        """
        self.round_update()

    def play_sound(self):
        """"
        Play rabbit sounds
        """
        pygame.mixer.stop()
        if self.game.round_event == 0 and pygame.mixer.get_busy() == False:
            self.rabbit_hungry_sound.play()

        if self.game.round_event == 3 and pygame.mixer.get_busy() == False:
            self.rabbit_get_food.play()

        if self.game.round_event == 5 and pygame.mixer.get_busy() == False:
            self.rabbit_win.play()

        if self.die and pygame.mixer.get_busy() == False:
            self.rabbit_die_sound.play()

    def round_update(self):
        """"
        Update rabbit events all over the round
        """
        # Event 0: Rabbit find carrot
        if self.game.round_event == 0:
            self.move()
            if self.round_count == 2 and self.rect.x <= 580:
                self.image = pygame.transform.rotate(
                    pygame.transform.flip(self.rabbit_cry, False, True), 180)
                self.rect = self.image.get_rect(midbottom=(580, 600))
                self.play_sound()
                self.game.round_event += 1
                self.game.items_created = 0
            else:
                if self.rect.x <= -130:
                    self.direction = 'right'
                    self.round_count += 1
                elif self.rect.x >= 800:
                    self.direction = 'left'
                    self.round_count += 1

        # Event 3: Get food, start script
        if self.game.round_event == 3 and pygame.mixer.get_busy() == False:
            self.play_sound()
            self.game.round_event += 1

        # Event 5: Rabbit reply
        if self.game.round_event == 5 and pygame.mixer.get_busy() == False:
            self.play_sound()
            self.game.round_event += 1

        # Event 6: Rabbit run away
        if self.game.round_event == 6:
            if pygame.mixer.get_busy() == False:
                self.direction = 'right'
                self.move()
                if self.rect.x >= 720:
                    self.game.round_event += 1
                    self.kill()

        # Killed by the saw
        if self.game.round_event == 2 and self.rect.colliderect(self.game.saw) and self.die == False:
            self.die = True
            self.play_sound()
            self.game.items_created = 1

        # Game_over
        if self.die and pygame.mixer.get_busy() == False:
            self.game.game_over_flag = 1
            self.kill()

# ==============Elephant================


class Elephant(pygame.sprite.Sprite):
    """
    Elephant sprite class will create a elephant in round 5
    ...
    Attributes
    ----------
    game: access all game class attribute
        game class of main file
    _layer: order of draw sprites
        int
    groups: all sprites of the game
        game sprites
    elephant_run: list of elephant run movement images
        pygame image
    elephant_run_index: control elephant run movement
        int
    image: current image
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    all sound file: store elephant sound
        wav
    die: get to when the elephant is killed by player and game over
        bool

    Methods
    -------
    play_sound:
        play player sound
    round_update:
        run round function if its condition is true
    update:
        run all functions
    move: 
        make the rhino move 
    """

    def __init__(self, game):
        """
        Initialize elephant in start of round 5
        """
        super().__init__()

        self.game = game
        self._layer = SUB_CHAR
        self.direction = 'left'
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        elephant_run1 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/elephant/elephant_run1.png').convert_alpha(), (0.8, 0.8))
        elephant_run2 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/elephant/elephant_run2.png').convert_alpha(), (0.8, 0.8))
        elephant_run3 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/elephant/elephant_run3.png').convert_alpha(), (0.8, 0.8))
        elephant_run4 = pygame.transform.scale_by(pygame.image.load(
            'graphics/animals/elephant/elephant_run4.png').convert_alpha(), (0.8, 0.8))

        self.elephant_run = [elephant_run1,
                             elephant_run2, elephant_run3, elephant_run4]
        self.elephant_run_index = 0
        self.image = self.elephant_run[self.elephant_run_index]
        self.rect = self.image.get_rect(midbottom=(500, 450))\

        self.elephant_start_sound = pygame.mixer.Sound(
            'sound/elephant/elephant_start.wav')
        self.elephant_reply_sound = pygame.mixer.Sound(
            'sound/elephant/elephant_reply.wav')
        self.elephant_win_sound = pygame.mixer.Sound(
            'sound/elephant/elephant_win.wav')

    def move(self):
        """
        Control the elephant movement
        """
        self.elephant_run_index += 0.14
        self.rect.x += 5
        if self.elephant_run_index >= len(self.elephant_run):
            self.elephant_run_index = 0
        self.image = self.elephant_run[int(self.elephant_run_index)]

    def update(self):
        """"
        Run un round update functions
        """
        self.round_update()

    def play_sound(self):
        """"
        Play elephant sounds
        """
        pygame.mixer.stop()
        if self.game.round_event == 0:
            self.elephant_start_sound.play()
        elif self.game.round_event == 3:
            self.elephant_win_sound.play()
        elif self.game.round_event == 5:
            self.elephant_reply_sound.play()

    def round_update(self):
        """"
        Update elephant events all over the round
        """
        # Event 0: Elephant is being captured
        if self.game.round_event == 0 and pygame.mixer.get_busy() == False:
            self.image = pygame.transform.rotate(
                pygame.transform.flip(self.image, False, True), 180)
            self.play_sound()
            self.game.round_event += 1
        # Event 3
        elif self.game.round_event == 3 and pygame.mixer.get_busy() == False:
            self.play_sound()
            self.game.round_event += 1
        # Event 5
        elif self.game.round_event == 5 and pygame.mixer.get_busy() == False:
            self.play_sound()
            self.game.round_event += 1

        # Event 7: Elephant run away
        if self.game.round_event == 7 and pygame.mixer.get_busy() == False:
            if self.rect.x >= 720:
                self.game.win_round += 1
                self.kill()
            else:
                self.move()

# ==============Man1================


class Man1(pygame.sprite.Sprite):
    """
    Man1 sprite class will create a man1 in last round
    ...
    Attributes
    ----------
    game: access all game class attribute
        game class of main file
    _layer: order of draw sprites
        int
    groups: all sprites of the game
        game sprites
    direction: control man1 direction
        string
    man1_walk: list of man1 walk movement images
        pygame image
    man1_walk_index: control man1 walk movement
        int
    image: current image
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    Methods
    -------
    round_update:
        run round function if its condition is true
    update:
        run all functions
    move: 
        make man1 move 
    """

    def __init__(self, game):
        """
        Initialize man1 in start of last round
        """
        super().__init__()

        self.game = game
        self._layer = SUB_CHAR
        self.direction = 'right'
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        man_walk1 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man1/man_walk1.png').convert_alpha(), (0.8, 0.8))
        man_walk2 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man1/man_walk2.png').convert_alpha(), (0.8, 0.8))
        man_walk3 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man1/man_walk3.png').convert_alpha(), (0.8, 0.8))
        man_walk4 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man1/man_walk4.png').convert_alpha(), (0.8, 0.8))
        man_walk5 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man1/man_walk5.png').convert_alpha(), (0.8, 0.8))

        self.man_walk = [man_walk1, man_walk2, man_walk3, man_walk4, man_walk5]
        self.man_walk_index = 0
        self.image = self.man_walk[self.man_walk_index]
        self.rect = self.image.get_rect(midbottom=(0, 600))

    def move(self):
        """
        Control man1 movement
        """
        if self.direction == 'right':
            self.man_walk_index += 0.14
            self.rect.x += 2
            if self.man_walk_index >= len(self.man_walk):
                self.man_walk_index = 0
        self.image = self.man_walk[int(self.man_walk_index)]
        if self.direction == 'left':
            self.man_walk_index += 0.14
            self.rect.x -= 2
            if self.man_walk_index >= len(self.man_walk):
                self.man_walk_index = 0
            self.image = pygame.transform.rotate(
                pygame.transform.flip(self.image, False, True), 180)

    def update(self):
        """
        Run all round update functions
        """
        self.round_update()

    def round_update(self):
        """
        Update man1 events all over the round
        """
        # Event 0:
        if self.game.round_event in range(0, 2):
            self.move()
            if self.rect.x <= -100:
                self.direction = 'right'
            elif self.rect.x >= 800:
                self.direction = 'left'
        # Event 1:
        elif self.game.round_event == 2:
            if self.direction == 'left':
                self.rect.x = self.game.player.rect.x + 150
            else:
                self.rect.x = self.game.player.rect.x - 150

# ==============Man2================


class Man2(pygame.sprite.Sprite):
    """
    Man2 sprite class will create a man2 in last round
    ...
    Attributes
    ----------
    game: access all game class attribute
        game class of main file
    _layer: order of draw sprites
        int
    groups: all sprites of the game
        game sprites
    direction: control man2 direction
        string
    man2_walk: list of man2 walk movement images
        pygame image
    man2_walk_index: control man2 walk movement
        int
    image: current image
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    Methods
    -------
    round_update:
        run round function if its condition is true
    update:
        run all functions
    move: 
        make man2 move 
    """

    def __init__(self, game):
        """"
        Initialize man2 in start of last round
        """
        super().__init__()

        self.game = game
        self._layer = SUB_CHAR
        self.direction = 'left'
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        man_walk1 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man2/man_walk1.png').convert_alpha(), (0.8, 0.8))
        man_walk2 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man2/man_walk2.png').convert_alpha(), (0.8, 0.8))
        man_walk3 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man2/man_walk3.png').convert_alpha(), (0.8, 0.8))
        man_walk4 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man2/man_walk4.png').convert_alpha(), (0.8, 0.8))
        man_walk5 = pygame.transform.scale_by(pygame.image.load(
            'graphics/man2/man_walk5.png').convert_alpha(), (0.8, 0.8))

        self.man_walk = [man_walk1, man_walk2, man_walk3, man_walk4, man_walk5]
        self.man_walk_index = 0
        self.image = self.man_walk[self.man_walk_index]
        self.rect = self.image.get_rect(midbottom=(800, 600))

    def move(self):
        """
        Control man2 movement
        """
        if self.direction == 'right':
            self.man_walk_index += 0.14
            self.rect.x += 2
            if self.man_walk_index >= len(self.man_walk):
                self.man_walk_index = 0
        self.image = self.man_walk[int(self.man_walk_index)]
        if self.direction == 'left':
            self.man_walk_index += 0.14
            self.rect.x -= 2
            if self.man_walk_index >= len(self.man_walk):
                self.man_walk_index = 0
            self.image = pygame.transform.rotate(
                pygame.transform.flip(self.image, False, True), 180)

    def update(self):
        """
        Run all round update functions
        """
        self.round_update()

    def round_update(self):
        """
        Update man2 events all over the round
        """
        # Event 0:
        if self.game.round_event in range(0, 2):
            self.move()
            if self.rect.x <= -100:
                self.direction = 'right'
            elif self.rect.x >= 800:
                self.direction = 'left'
        # Event 1:
        elif self.game.round_event == 2:
            if self.direction == 'left':
                self.rect.x = self.game.player.rect.x + 150
            else:
                self.rect.x = self.game.player.rect.x - 150

# ================Items=================
# ================Player items bar=================


class ItemsBar(pygame.sprite.Sprite):
    """
    A class create items bar to place player items
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of items bar
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    """

    def __init__(self, game):
        """
        Initialize items bar in start of round 1
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load(
            'graphics/items/player_items/items_bar.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.8, 0.8))
        self.rect = self.image.get_rect(center=(400, 100))

# =============Start Screen=============
# Find better image


class StartButton(pygame.sprite.Sprite):
    """
    A class create start button in start screen, will start the game if this sprite is clicked
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of start button
        png
    rect: image with rectangle around to control position more easily
        pygame rect

    Methods:
    update: update start button events
    is_clicked: when start button is clicked, move on to the next round
    """

    def __init__(self, game):
        """
        Initialize start button in start screen
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.transform.scale_by(pygame.image.load(
            'graphics/items/start_game/start_button.png').convert_alpha(), (0.65, 0.65))
        self.rect = self.image.get_rect(midbottom=(495, 615))

    def update(self):
        """
        Update start button events
        """
        if self.game.current_round != 'start_screen':
            self.kill()

    def is_clicked(self):
        """
        Disappear and move on to next round if this sprite is clicked
        """
        if self.alive():
            self.game.next_round = 1
            self.kill()


class GameLabel(pygame.sprite.Sprite):
    """
    A game label class, show the name of this game
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of game label
        png
    rect: image with rectangle around to control position more easily
        pygame rect

    Methods:
    update: delete game label sprite in which round is different with start screen
    """

    def __init__(self, game):
        """
        Initial game label in start screen
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load(
            'graphics/items/start_game/game_label.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.92, 0.92))
        self.rect = self.image.get_rect(midbottom=(415, 300))

    def update(self):
        """
        Delete this sprite if current round is not start screen
        """
        if self.game.current_round != 'start_screen':
            self.kill()

# =============Intro=============
# Improve earth transition


class Earth(pygame.sprite.Sprite):
    """
    A class creates earth image in intro
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of earth
        png
    rect: image with rectangle around to control position more easily
        pygame rect

    Methods:
    --------
    update: update earth events
    change: change earth image follow the fairy's script
    """

    def __init__(self, game):
        """
        Initialize earth in start of intro
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.earth1 = pygame.image.load(
            'graphics/items/intro/earth1.png').convert_alpha()
        self.earth2 = pygame.image.load(
            'graphics/items/intro/earth2.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.earth1, (0.6, 0.6))
        self.rect = self.image.get_rect(center=(400, 300))

    def update(self):
        """
        Update events of earth
        """
        if self.game.round_event == 1:
            threading.Thread(target=self.change).start()
        if self.game.current_round != 'intro':
            self.kill()

    def change(self):
        """
        Change earth image follow up to the fairy script
        """
        if self.game.round_event == 1:
            time.sleep(9)
            self.image = pygame.transform.scale_by(self.earth2, (0.6, 0.6))
            self.rect = self.image.get_rect(center=(400, 300))

# =============Round 1=============


class Mouse(pygame.sprite.Sprite):
    """
    A class creates a mouse to give introduction for the player
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of mouse
        png
    rect: image with rectangle around to control position more easily
        pygame rect

    Methods:
    --------
    update: delete mouse sprite when move on to the next round
    """

    def __init__(self, game):
        """
        Initialize mouse sprite in start of round1_1
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load(
            'graphics/items/round1/mouse_click.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(center=(450, 220))

    def update(self):
        """
        Delete mouse when the current round is not round1_1 
        """
        if self.game.current_round != 'round1_1':
            self.kill()


class Arrow(pygame.sprite.Sprite):
    """
    A class creates a arrow to give introduction for the player
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of arrow
        png
    rect: image with rectangle around to control position more easily
        pygame rect

    Methods:
    --------
    update: delete arrow sprite when move on to the next round
    """

    def __init__(self, game):
        """
        Initialize mouse sprite in start of round1_1
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load(
            'graphics/items/round1/arrow.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(center=(300, 250))

    def update(self):
        """
        Delete mouse when the current round is not round1_1 
        """
        if self.game.current_round != 'round1_1':
            self.kill()

# =============Round 2=============


class Horn(pygame.sprite.Sprite):
    """
    A class creates a horn when fairy finish the script in round1_1
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of horn
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    draggable: get to know when the horn is draggable
        bool

    Methods:
    --------
    update: update all horn events
    win_round: when the horn is touched to the rhino, move on to next event of this round 
    put_in_bag: when the player touches, the horn will be placed in items bar
    """

    def __init__(self, game):
        """
        Initialize horn sprite in start of round 2
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.draggable = False
        self._layer = ITEMS_LAYER

        self.image = pygame.image.load(
            'graphics/items/player_items/horn.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(320, 600))

    def update(self):
        """
        Update all horn events
        """
        self.win_round()
        self.put_in_bag()

    def win_round(self):
        """
        Get to know when the horn touches the rhino
        """
        # Event 2: Wait for player's help
        if self.game.current_round == 'round2':
            if self.game.round_event == 2 and self.rect.colliderect(self.game.rhino) and self.game.rhino.die == False and pygame.mixer.get_busy() == False:
                self.game.round_event += 1
                self.kill()

    def put_in_bag(self):
        """
        When touches the player in round1_1, the horn will be placed in items bar
        """
        if self.game.current_round == 'round1_1' and self.rect.colliderect(self.game.player):
            self.rect = self.image.get_rect(center=(210, 110))
            self.game.win_round += 1
            self.draggable = True

# =============Round 3=============


class FirstAidKit(pygame.sprite.Sprite):
    """
    A class creates a first aid kit when fairy finish the script in round1_1
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of first aid kit
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    draggable: get to know when the first aid kit is draggable
        bool

    Methods:
    --------
    update: update all first aid kit events
    win_round: when the first aid kit is touched to the lion, move on to next event of this round 
    put_in_bag: when the player touches, the first aid kit will be placed in items bar
    """

    def __init__(self, game):
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.draggable = False
        self._layer = ITEMS_LAYER

        self.image = pygame.image.load(
            'graphics/items/player_items/first_aid_kit.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(500, 600))

    def update(self):
        self.win_round()
        self.put_in_bag()

    def win_round(self):
        # Event 3: Wait for player's help
        if self.game.current_round == 'round3':
            if self.game.round_event == 3 and self.rect.colliderect(self.game.lion) and self.game.lion.die == False and pygame.mixer.get_busy() == False:
                self.game.round_event = 4
                self.kill()

    def put_in_bag(self):
        if self.game.current_round == 'round1_1' and self.rect.colliderect(self.game.player):
            self.rect = self.image.get_rect(center=(360, 110))
            self.game.win_round += 1
            self.draggable = True


class Nail(pygame.sprite.Sprite):
    """
    A class creates a nail in start of round 3
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of nail
        png
    rect: image with rectangle around to control position more easily
        pygame rect

    Methods:
    --------
    update: update all horn events
    touch_lion: move on to the next event of round 3 when the nail touches the lion
    """

    def __init__(self, game):
        """
        Initialize nail in start of round 3
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load(
            'graphics/items/round3/nail.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(350, 530))

    def update(self):
        """
        Update lion events
        """
        self.touch_lion()

    def touch_lion(self):
        """
        Move on to the next event of round 3 when the nail touches the lion
        """
        # Event 0: Lion is running then touch the nail
        if self.rect.colliderect(self.game.lion):
            self.game.round_event += 1
            self.kill()

# =============Round 4=============


class Carrot(pygame.sprite.Sprite):
    """
    A class creates a carrot when the rabbit finish the script in round 4
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    _layer: sprite draw order
        int
    groups: all sprites group
        pygame sprite
    image: image of carrot
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    draggable: get to know when the carrot is draggable
        bool

    Methods:
    --------
    update: update all carrot events
    win_round: when the carrot is touched to the rabbit, move on to next event of this round 
    put_in_bag: when the player touches, the carrot will be placed in items bar
    """

    def __init__(self, game):
        """
        Initialize carrot when the rabbit finish its script
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.draggable = False
        self._layer = ITEMS_LAYER

        self.image = pygame.image.load(
            'graphics/items/player_items/carrot.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(500, 400))

    def update(self):
        """
        Update carrot events
        """
        self.win_round()
        self.put_in_bag()

    def win_round(self):
        """
        Move on to next event of round4 when carrot touches the rabbit
        """
        # Event 2: Wait for player's help
        if self.game.current_round == 'round4':
            if self.game.round_event == 2 and self.rect.colliderect(self.game.rabbit) and self.game.lion.die == False and pygame.mixer.get_busy() == False:
                self.game.round_event += 1
                self.kill()

    def put_in_bag(self):
        """
        Be placed in items bag when touches the player
        """
        if self.game.current_round == 'round4' and self.rect.colliderect(self.game.player) and self.game.round_event == 2:
            self.rect = self.image.get_rect(center=(360, 110))
            self.draggable = True

# =============Round 5=============


class Saw(pygame.sprite.Sprite):
    """
    A class creates a saw when fairy finish the script in round1_1
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    image: image of arrow
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    draggable: get to know when the saw is draggable
        bool

    Methods:
    --------
    update: update all saw events
    win_round: when the saw is touched to the cage, move on to next event of this round 
    put_in_bag: when the player touches, the saw will be placed in items bar
    kill_animal: kill the animal the saw touches them
    """

    def __init__(self, game):
        """
        Initialize the saw in start of round1_1
        """
        self.display = 1
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.draggable = False
        self._layer = ITEMS_LAYER

        self.image = pygame.image.load(
            'graphics/items/player_items/saw.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(700, 600))

    def update(self):
        """
        Update all saw events
        """
        self.win_round()
        self.put_in_bag()
        self.kill_animal()

    def win_round(self):
        """
        When the saw touches the cage in round5, move on to the next event of this round
        """
        if self.game.current_round == 'round5' and self.game.round_event == 2 and self.rect.colliderect(self.game.cage) and pygame.mixer.get_busy() == False:
            # Event 2: Saw touch the cage
            self.game.round_event += 1
            self.kill()
            self.game.cage.kill()

    def put_in_bag(self):
        """
        Place the saw in items bar when it touches the player
        """
        if self.game.current_round == 'round1_1' and self.rect.colliderect(self.game.player):
            self.rect = self.image.get_rect(center=(500, 110))
            self.game.win_round += 1
            self.draggable = True

    def kill_animal(self):
        """
        Kill the animal when drag the saw to them
        """
        if self.game.current_round == 'round2' and self.game.round_event == 2 and self.rect.colliderect(self.game.rhino):
            self.kill()
        elif self.game.current_round == 'round3' and self.rect.colliderect(self.game.lion) and self.game.round_event == 3:
            self.kill()
        elif self.game.current_round == 'round4' and self.rect.colliderect(self.game.lion) and self.game.round_event == 2:
            self.kill()


class Cage(pygame.sprite.Sprite):
    """
    A class creates a cage in start of round 5
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of cage
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    """

    def __init__(self, game):
        """
        Initialize cage in start of round 5
        """
        self.game = game
        self._layer = ITEMS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load(
            'graphics/items/round5/cage.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(500, 450))

# =============Round 6=============


class Seed(pygame.sprite.Sprite):
    """
    A class creates a seed when the rhino finishes the script in round 2
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    _layer: sprite draw order
        int
    groups: all sprites group
        pygame sprite
    image: image of seed
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    draggable: get to know when the seed is draggable
        bool

    Methods:
    --------
    update: update all seed events
    win_round: When touches to the flower pot with shovel and watering can, move on to the next event of round 6 
    put_in_bag: when the player touches, the seed will be placed in items bar
    """

    def __init__(self, game):
        """
        Initialize the seed when the rhino finishes the script
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.draggable = False
        self._layer = ITEMS_LAYER

        self.image = pygame.image.load(
            'graphics/items/player_items/seed.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(400, 490))

    def update(self):
        """
        Update seed events
        """
        self.win_round()
        self.put_in_bag()

    def win_round(self):
        """
        When touches to the flower pot with shovel and watering can, move on to the next event of round 6
        """
        if self.game.current_round == 'round6_1' and pygame.mixer.get_busy() == False:
            if self.game.round_event == 3 and self.rect.colliderect(self.game.flowerpot):
                self.game.win_round += 1
                self.kill()

    def put_in_bag(self):
        """
        when the player touches, the seed will be placed in items bar in round 2
        """
        if self.game.current_round == 'round2' and self.rect.colliderect(self.game.player) and (self.game.win_round == 0 or self.game.win_round == 1):
            self.rect.center = (210, 110)
            self.draggable = True
            self.game.win_round += 1


class Shovel(pygame.sprite.Sprite):
    """
    A class creates a shovel when the fairy finishes the script in round 6
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    _layer: sprite draw order
        int
    groups: all sprites group
        pygame sprite
    image: image of shovel
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    draggable: get to know when the seed is draggable
        bool

    Methods:
    --------
    update: update all seed events
    win_round: when touches to the flower pot with seed and watering can, move on to the next event of round 6 
    put_in_bag: when the player touches, the seed will be placed in items bar
    """

    def __init__(self, game):
        """
        Initialize shovel when fairy finishes the script in round 6
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.draggable = False
        self._layer = ITEMS_LAYER

        self.image = pygame.image.load(
            'graphics/items/player_items/shovel.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(450, 535))

    def update(self):
        """
        Update all shovel events
        """
        self.win_round()
        self.put_in_bag()

    def win_round(self):
        """
        When touches to the flower pot with seed and watering can, move on to the next event of round 6
        """
        if self.game.round_event == 3 and self.rect.colliderect(self.game.flowerpot) and pygame.mixer.get_busy() == False:
            self.game.win_round += 1
            self.kill()

    def put_in_bag(self):
        """
        When the player touches, the seed will be placed in items bar
        """
        if self.game.round_event in range(1, 4):
            if self.rect.colliderect(self.game.player):
                self.rect.center = (500, 110)
                self.draggable = True


class WateringCan(pygame.sprite.Sprite):
    """
    A class creates a watering can when the fairy finishes the script in round 6
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    _layer: sprite draw order
        int
    groups: all sprites group
        pygame sprite
    image: image of watering can
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    draggable: get to know when the seed is draggable
        bool

    Methods:
    --------
    update: update all seed events
    win_round: when touches to the flower pot with shovel and seed, move on to the next event of round 6 
    put_in_bag: when the player touches, the seed will be placed in items bar
    """

    def __init__(self, game):
        """
        Initialize watering can when the fairy finishes the script in round 6
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.draggable = False
        self._layer = ITEMS_LAYER

        self.image = pygame.image.load(
            'graphics/items/player_items/watering_can.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(250, 535))

    def update(self):
        """
        Update all watering can events
        """
        self.win_round()
        self.put_in_bag()

    def win_round(self):
        """
        When touches to the flower pot with shovel and seed, move on to the next event of round 6
        """
        if self.game.round_event == 3 and self.rect.colliderect(self.game.flowerpot) and pygame.mixer.get_busy() == False:
            self.game.win_round += 1
            self.kill()

    def put_in_bag(self):
        """
        When the player touches, the seed will be placed in items bar
        """
        if self.game.round_event in range(1, 4):
            if self.rect.colliderect(self.game.player):
                self.rect.center = (360, 110)
                self.draggable = True


class Flowerpot(pygame.sprite.Sprite):
    """
    A class creates a flower pot in start round 6
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    _layer: sprite draw order
        int
    groups: all sprites group
        pygame sprite
    image: image of flower pot
        png
    rect: image with rectangle around to control position more easily
        pygame rect

    Methods:
    --------
    update: delete this sprite when the current round is not round6_1
    """

    def __init__(self, game):
        """
        Initialize flower pot in start of round 6
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.draggable = False
        self._layer = ITEMS_LAYER

        self.image = pygame.image.load(
            'graphics/items/round6/flowerpot.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(400, 535))

    def update(self):
        """
        Delete this sprite when the current round is not round6_1
        """
        if self.game.current_round != 'round6_1':
            self.kill()

# =============Round 7=============


class Speaker(pygame.sprite.Sprite):
    """
    A class creates a speaker in start of last round
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    _layer: sprite draw order
        int
    groups: all sprites group
        pygame sprite
    image: image of speaker
        png
    rect: image with rectangle around to control position more easily
        pygame rect
    draggable: get to know when the seed is draggable
        bool

    Methods:
    --------
    update: update all seed events
    win_round: when touches the player, move on to the next event of final round 
    put_in_bag: when the player touches, the seed will be placed in items bar
    """

    def __init__(self, game):
        """
        Initialize speaker in start of last round 
        """
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.draggable = False
        self._layer = ITEMS_LAYER

        self.image = pygame.image.load(
            'graphics/items/player_items/speaker.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (0.6, 0.6))
        self.rect = self.image.get_rect(midbottom=(450, 535))

    def update(self):
        """
        Update all speaker events
        """
        self.win_round()
        self.put_in_bag()

    def win_round(self):
        """
        When touches player, move on to the next event of last round 
        """
        # Event 1: speaker touch player
        if self.game.round_event == 1 and self.rect.colliderect(self.game.player):
            self.game.round_event += 1
            self.kill()

    def put_in_bag(self):
        """
        When the player touches, the seed will be placed in items bar
        """
        # Event 0: player collect speaker
        if self.game.round_event == 0 and self.rect.colliderect(self.game.player):
            self.rect.center = (500, 110)
            self.game.round_event += 1
            self.draggable = True

# =============Game control=============


class SkipButton(pygame.sprite.Sprite):
    """
    A class creates skip button when the fairy starts her script, will skip the fairy's script if this sprite is clicked
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of skip button
        png
    rect: image with rectangle around to control position more easily
        pygame rect

    Methods:
    update: update skip button events
    is_clicked: when skip button is clicked, move on to the next event of the round
    """

    def __init__(self, game):
        """
        Initialize the skip button when the fairy starts her script
        """
        self.game = game
        self._layer = ITEMS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.transform.scale_by(pygame.image.load(
            'graphics/items/game_control/skip_button.png').convert_alpha(), (0.065, 0.065))
        self.rect = self.image.get_rect(center=(680, 130))

    def update(self):
        """
        Update all skip button events
        """
        if self.game.fairy.sound_is_playing != 1:
            self.kill()

    def is_clicked(self):
        """
        When skip button is clicked, move on to the next event of the round
        """
        # Intro
        if self.game.current_round == 'intro':
            pygame.mixer.stop()
            self.game.next_round = 1
            self.kill()
        # Round 1
        elif self.game.current_round == 'round1_1':
            pygame.mixer.stop()
            self.game.round_event += 1
            self.kill()
        # Round 2
        elif self.game.current_round == 'round2':
            pygame.mixer.stop()
            self.game.round_event = 1
            self.kill()
        # Round 6_1
        elif self.game.current_round == 'round6_1':
            pygame.mixer.stop()
            self.kill()
        # Round 6_2
        elif self.game.current_round == 'round6_2':
            pygame.mixer.stop()
            self.kill()


class PlayAgainButton(pygame.sprite.Sprite):
    """
    A class creates play again button when this is game over screen
    , come back to start screen if play again button is clicked
    ...
    Attributes:
    -----------
    game: Game class in main file
        class
    groups: all sprites group
        pygame sprite
    _layer: sprite draw order
        int
    image: image of play again button
        png
    rect: image with rectangle around to control position more easily
        pygame rect

    Methods:
    update: update play again button events
    is_clicked: when play again button is clicked, move on to the next event of the round
    """

    def __init__(self, game):
        """
        Initialize play again button in game over screen
        """
        self.game = game
        self._layer = ITEMS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.transform.scale_by(pygame.image.load(
            'graphics/items/game_control/play_again_btn.png').convert_alpha(), (0.3, 0.3))
        self.rect = self.image.get_rect(center=(400, 440))

    def is_clicked(self):
        """
        When play again button is clicked, come back to start screen 
        """
        self.game.new()
