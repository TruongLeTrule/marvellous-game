import pygame
import sys
from sprites import *
from config import *
from backgrounds import *


class Game:
    """
    A class to control the game
    ...

    Attributes
    ----------
    screen: pygame display class
        user's monitor
    clock: pygame Clock class 
        game clock
    font: pygame Font class 
        game font
    running: bool
        True if game is running
    rounds: list
        Ordered game rounds 
    skip_btn: None
        Make sure that there is no problem when skip button haven't been created yet
    in_game_music: pygame Sound class
        Theme music
    playing: bool
        True if main function is playing
    all_sprites: pygame Sprite class
        Group of game items, characters
    next_round: int
        1 if player passed the round, other case is 0 
    win_round: int
        1 if player can pass the current round, other case is 0 
    game_over_flag: int
        1 if player lost the game, other case is 0
    items_created: int
        1 if items of current round was created, 0 if haven't been created
    round_index: int
        keep track of current round index in round list
    round_event: int
        control current round events
    end_game: int
        1 if game ended, 0 if didn't
    current_round: string
        name of current round
    active_item: pygame sprite class
        item is clicked
    bg: Background class
        game background
    player_items: list
        list of draggable game items

    Methods
    ------- 
    new: 
        create new game, start from start screen
    init_new_round:
        init items of each new round
    events:
        check player input from keyboard or mouse
    pass_round:
        if player passed current round, change background and reset round attribute
    draw:
        draw sprites, background
    update:
        update game events
    game_over:
        if player lost the game, kill all sprites and set background to game over screen
    game_end:
        if player won the game, kill all sprites and set background to end screen
    main:
        call all function 
    """

    def __init__(self):
        """"
        Initialize game resources
        """
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('font/Pixeltype.ttf')
        pygame.display.set_caption('Marvellous')
        self.running = True
        self.rounds = ['start_screen', 'intro', 'round1_1', 'round1_2', 'round2',
                       'round3', 'round4', 'round5', 'round6_1', 'round6_2', 'round7']
        self.skip_btn = None

        self.in_game_music = pygame.mixer.Sound(
            'sound/music/in_game_music.wav')
        self.in_game_music.play(loops=-1)

    def new(self):
        """"
        Start new game, reset all game controlling attributes
        """
        #  A new game start
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.next_round = 0  # Pass current round
        self.win_round = 0  # Player done all mission in current round
        self.game_over_flag = 0  # Player lost the game
        self.items_created = 0  # Check if new round items were created
        self.round_index = 0
        self.round_event = 0
        self.end_game = 0
        self.current_round = self.rounds[self.round_index]
        self.active_item = None

        self.bg = Background(self.current_round)

        self.player_items = []

    def init_new_round(self):
        """"
        Initialize each round items
        """
        if self.items_created == 0:
            # Start screen
            if self.current_round == 'start_screen':
                self.start_button = StartButton(self)
                self.game_label = GameLabel(self)
                self.items_created = 1

            # Intro
            if self.current_round == 'intro':
                self.earth = Earth(self)
                self.fairy = Fairy(self)
                self.items_created = 1

            # Round 1
            if self.current_round == 'round1_1':
                if self.round_event == 0:
                    self.mouse = Mouse(self)
                    self.arrow = Arrow(self)
                    self.items_bar = ItemsBar(self)
                    self.player = Player(self)
                    self.items_created = 1

                if self.round_event == 3:
                    self.horn = Horn(self)
                    self.first_aid_kit = FirstAidKit(self)
                    self.saw = Saw(self)
                    self.player_items.extend(
                        [self.horn, self.first_aid_kit, self.saw])
                    self.items_created = 1

            # Round 2
            if self.current_round == 'round2':
                if self.round_event == 0:
                    self.fairy = Fairy(self)
                    self.items_created = 1
                elif self.round_event == 1:
                    self.rhino = Rhino(self)
                    self.items_created = 1
                elif self.round_event == 5:
                    self.seed = Seed(self)
                    self.player_items.append(self.seed)
                    self.items_created = 1

            # Round 3
            if self.current_round == 'round3':
                self.lion = Lion(self)
                self.nail = Nail(self)
                self.items_created = 1

            # Round 4
            if self.current_round == 'round4':
                if self.round_event == 0:
                    self.rabbit = Rabbit(self)
                    self.items_created = 1
                elif self.round_event == 1 and pygame.mixer.get_busy() == False:
                    self.player = Player(self)
                    self.items_created = 1
                elif self.round_event == 2 and pygame.mixer.get_busy() == False:
                    self.carrot = Carrot(self)
                    self.player_items.append(self.carrot)
                    self.items_created = 1

            # Round 5
            if self.current_round == 'round5':
                if self.round_event == 0:
                    self.cage = Cage(self)
                    self.elephant = Elephant(self)
                    self.items_created = 1

            # Round 6
            if self.current_round == 'round6_1':
                if self.round_event == 0:
                    self.flowerpot = Flowerpot(self)
                    self.shovel = Shovel(self)
                    self.watering_can = WateringCan(self)
                    self.player_items.extend([self.shovel, self.watering_can])
                    self.items_created = 1
                elif self.round_event == 2:
                    self.fairy = Fairy(self)
                    self.items_created = 1
            if self.current_round == 'round6_2':
                if self.round_event == 0:
                    self.items_created = 1
                elif self.round_event == 1 and pygame.mixer.get_busy() == False:
                    self.fairy = Fairy(self)
                    self.items_created = 1

            # Round 7
            if self.current_round == 'round7':
                if self.round_event == 0:
                    self.man1 = Man1(self)
                    self.man2 = Man2(self)
                    self.speaker = Speaker(self)
                    self.player_items.append(self.speaker)
                    self.items_created = 1

            # Game over
            if self.current_round == 'game_over':
                self.play_again_btn = PlayAgainButton(self)
                self.items_created = 1

    def events(self):
        """"
        Check for the events when mouse is clicked
        """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Click start button
                if self.start_button.rect.collidepoint(event.pos):
                    self.start_button.is_clicked()

                # Click skip button
                if self.skip_btn != None:
                    if self.skip_btn.rect.collidepoint(event.pos):
                        self.skip_btn.is_clicked()

                # Click play again button
                if self.current_round == 'game_over' and self.play_again_btn.rect.collidepoint(event.pos):
                    self.play_again_btn.is_clicked()

                # Click player items
                for num, item in enumerate(self.player_items):
                    if item.rect.collidepoint(event.pos):
                        self.active_item = num

            if event.type == pygame.MOUSEBUTTONUP:
                self.active_item = None

            if event.type == pygame.MOUSEMOTION:
                # Drag player items
                if self.active_item != None and self.player_items[self.active_item].draggable:
                    self.player_items[self.active_item].rect.move_ip(event.rel)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def pass_round(self):
        """"
        If received next_round = 1 then reset all round controlling attribute
        and let the player pass this round
        """
        # Check if player pass through current round
        if self.next_round == 1:
            self.round_index += 1

            # Change background
            self.current_round = self.rounds[self.round_index]
            self.bg.update(self.current_round)

            # Set all flag to origin
            self.next_round = 0
            self.items_created = 0
            self.round_event = 0
            self.win_round = 0

    def draw(self):
        """"
        Draw all sprites and background on screen
        """
        self.bg.draw(self.screen, self.current_round)
        self.all_sprites.draw(self.screen)

    def update(self):
        """"
        Update all events of the game
        """
        self.all_sprites.update()
        self.pass_round()
        self.game_over()
        self.game_end()
        pygame.display.update()

    def game_over(self):
        """"
        When received game_over_flag = 1 then set current round to game_over screen and kill all the sprites
        """
        if self.game_over_flag:
            self.current_round = 'game_over'
            self.bg.update(self.current_round)
            for sprite in self.all_sprites:
                sprite.kill()
            self.game_over_flag = 0

    def game_end(self):
        """
        When received end_game = 1 then set current round to end_game screen and kill all the sprites
        """
        if self.end_game:
            self.current_round = 'end_screen'
            self.bg.update(self.current_round)
            for sprite in self.all_sprites:
                sprite.kill()

    def main(self):
        """
        Run all functions
        """
        while self.playing:
            self.init_new_round()

            self.events()
            self.draw()
            self.update()
            self.clock.tick(FPS)
        self.running = False


# ==============Main==============
g = Game()
g.new()
while g.running:
    g.main()
