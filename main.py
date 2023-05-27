from sys import exit
import pygame

# Initializing all pygame modules
pygame.init()

# Starting variables
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()

# Loading font
test_font = pygame.font.Font('fonts/puffy.otf', 50)

# Loading surfaces, scaling size of some
background_image = pygame.image.load('graphics/background.jpeg').convert()
background_image = pygame.transform.scale(background_image,(800,350))

ground_image = pygame.image.load('graphics/ground.png').convert()

text_surface = test_font.render('Hello player', False ,'Purple')

bird_image = pygame.image.load('graphics/cardinal.gif').convert_alpha()
bird_image = pygame.transform.scale(bird_image, (50,50))
character_x_pos = 0
max_x_pos = 800

runner_image = pygame.image.load('graphics/char1.png').convert_alpha()
runner_image = pygame.transform.scale(runner_image, (40,40))

character_rect = runner_image.get_rect(midbottom = (0,355))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Copying loaded surfaces to screen
    screen.blit(background_image, (0, 0))
    screen.blit(ground_image, (0,350))
    screen.blit(text_surface, (250,0))
    character_x_pos += 4
    if character_x_pos > max_x_pos:
        character_x_pos = 0
    screen.blit(bird_image, (character_x_pos,250))
    screen.blit(runner_image, character_rect)

    # Updating the screen, 60 times per second
    # (60fps)
    pygame.display.update()
    clock.tick(60)
