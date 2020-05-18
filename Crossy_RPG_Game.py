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
        direction = 0

        player_character = PlayerCharacter('images/player.png', 375, 700, 50, 50)
        enemy_0 = EnemyCharacter('images/enemy.png', 20, 400, 50, 50)
        treasure = GameObject('images/treasure.png', 375, 50, 50, 50)

        # Main game loop, used to update all gameplay such as movement, check and graphics.
        while not is_game_over:

            # Looks for quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

            self.game_screen.fill(WHITE_COLOR)
            treasure.draw(self.game_screen)

            player_character.move(direction, self.height)
            player_character.draw(self.game_screen)

            # Move and draw enemy
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            # Detect collision
            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True

            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update
            clock.tick(self.TICK_RATE)


# Generic game object class to be subclassed by other objects in the game
class GameObject:
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    # Draw the object by blitting it onto the background (game screen)
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


# Class to represent the character controlled by the player
class PlayerCharacter(GameObject):
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 20 - self.height:
            self.y_pos = max_height - 20 - self.height

    def detect_collision(self, other_entity: GameObject):
        if self.y_pos > other_entity.y_pos + other_entity.height:
            return False
        elif self.y_pos + self.height < other_entity.y_pos:
            return False

        if self.x_pos > other_entity.x_pos + other_entity.width:
            return False
        if self.x_pos + self.width < other_entity.x_pos:
            return False
        return True


# Class to represent the character controlled by the player
class EnemyCharacter(GameObject):
    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 20 - self.width:
            self.SPEED = -abs(self.SPEED)

        self.x_pos += self.SPEED


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()
