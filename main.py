from sys import exit
import pygame

# Initializing all pygame modules
pygame.init()

# Starting variables
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()

# Loading font(Path, Font Size)
test_font = pygame.font.Font('fonts/puffy.otf', 40)

# Loading surfaces --------------------------------------------------------------
background_image = pygame.image.load('graphics/desert.png').convert()
background_image = pygame.transform.scale(background_image,(800,350))

ground_image = pygame.image.load('graphics/ground.png').convert()

# test_font.render(Text, Anti Aliasing, Color)
text_surface = test_font.render('SCORE', False ,'Black')
text_rect = text_surface.get_rect(center = (400,40))

rock_image = pygame.image.load('graphics/rock_enemy.png').convert_alpha()
rock_image = pygame.transform.scale(rock_image, (50,50))
rock_x_pos = 0
max_x_pos = 800
rock_rect = rock_image.get_rect(midbottom = (700, 350))

runner_image = pygame.image.load('graphics/char1.png').convert_alpha()
runner_image = pygame.transform.scale(runner_image, (45,45))
runner_rect = runner_image.get_rect(midbottom = (20,355))
runner_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #! Commented lines below are demonstrating ways to
        #! obtain player input
        # if event.type == pygame.MOUSEMOTION:
        #     if runner_rect.collidepoint(event.pos):
        #         print('collides')
        # -----------------------------------------------------------------
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
             runner_gravity = -30

    # Copying loaded surfaces to screen -------------------------
    screen.blit(background_image, (0, 0))
    screen.blit(ground_image, (0,350))
    pygame.draw.rect(screen, '#c7b18f', text_rect)
    screen.blit(text_surface, text_rect)
    screen.blit(rock_image, rock_rect)
   
    if rock_rect.colliderect(runner_rect):
        pygame.draw.line(screen, 'Red', (0,0), (800,500)) and pygame.draw.line(screen, 'Red', (800,0), (0,500))

    # Moving the rock 4 pixels for every frame, to the right
    # Repositioning it when it goes out of frame of the display
    rock_rect.x -= 4
    if rock_rect.right <= 0:
        rock_rect.left = 800
    
    #? Player
    runner_gravity += 1
    runner_rect.y += runner_gravity
    if runner_rect.y > 400:
        runner_rect.y = 340
    screen.blit(runner_image, runner_rect)

    #! More ways to obtain player input
    #! Better for working seperate from event loop
    # keystrokes = pygame.key.get_pressed()
    # if keystrokes[pygame.K_UP]:
    #     runner_rect.top -= 5
    # elif keystrokes[pygame.K_DOWN]:
    #     runner_rect.top += 5

    # Updating the screen, 60 times per second ---------------------------
    # (60fps)
    pygame.display.update()
    fps = clock.tick(60)
