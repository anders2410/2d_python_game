import pygame

# MY CONSTANTS
# Screen variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Crossy RPG"
# RGB Colors
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and frames
clock = pygame.time.Clock()


# player_image = pygame.image.load('images/player.png')
# player_image = pygame.transform.scale(player_image, (50, 50))

class Game:
    # Typical rate of 60, equivalent to FPS
    TICK_RATE = 60
    is_game_over = False

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the windows of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        # Main game loop, used to update all gameplay such as movement, check and graphics.
        while not is_game_over:

            # Looks for quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True

            # self.game_screen.blit(player_image, (375, 375))

            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update
            clock.tick(self.TICK_RATE)


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()
