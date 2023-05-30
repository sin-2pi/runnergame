from sys import exit
import pygame

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time = round(current_time/1000, 1)
    score_surf = game_font.render(f'{current_time}',False,'Black')
    score_rect = score_surf.get_rect(center = (400,80))
    screen.blit(score_surf,score_rect)

# Initializing all pygame modules
pygame.init()

# Starting variables
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()
game_active = True
start_time = 0

# Loading Font(Path, Font Size)
# Sets font for all text rendered in game
game_font = pygame.font.Font('fonts/puffy.otf', 40)

#! Loading Surfaces
# Sky background
background_image = pygame.image.load('graphics/desert.png').convert()
background_image = pygame.transform.scale(background_image,(800,350))

# Ground background
ground_image = pygame.image.load('graphics/ground.png').convert()

# Text that displays while game is running
# game_font.render(Text, Anti Aliasing, Color)
gamerunning_text = game_font.render('SCORE', False ,'Black')
gamerunning_rect = gamerunning_text.get_rect(center = (400,40))

# Text that displays when game ends.
gameover_text = game_font.render('GAME OVER: SPACE TO PLAY AGAIN', False, 'Black')
gameover_rect = gameover_text.get_rect(center = (400,50))

# Rock enemy image
# Loadings, scaling, and creating a rectangle for it.
rock_image = pygame.image.load('graphics/rock_enemy.png').convert_alpha()
rock_image = pygame.transform.scale(rock_image, (50,50))
rock_x_pos = 0
max_x_pos = 800
rock_rect = rock_image.get_rect(midbottom = (700, 350))

# Image of character you play.
runner_image = pygame.image.load('graphics/char1.png').convert_alpha()
runner_image = pygame.transform.scale(runner_image, (45,45))
runner_rect = runner_image.get_rect(midbottom = (20,355))
runner_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if runner_rect.collidepoint(event.pos) and runner_rect.bottom >= 300:
                    runner_gravity = -20
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and runner_rect.bottom >= 300:
                runner_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                rock_rect.left = 800
                start_time = pygame.time.get_ticks() 
                
                
    if game_active:
        # Copying loaded surfaces to screen
        screen.blit(background_image, (0, 0))
        screen.blit(ground_image, (0,350))
        pygame.draw.rect(screen, '#c7b18f', gamerunning_rect)
        screen.blit(gamerunning_text, gamerunning_rect)
        display_score()
        screen.blit(rock_image, rock_rect)
    
        # Moving the rock 4 pixels for every frame, to the right
        # Repositioning it when it goes out of frame of the display
        rock_rect.x -= 4
        if rock_rect.right <= 0:
            rock_rect.left = 800
        
        # Making sure player does not fall below the ground from gravity implementation
        runner_gravity += 1
        runner_rect.y += runner_gravity 
        if runner_rect.bottom >= 355:
            runner_rect.bottom = 355
        screen.blit(runner_image, runner_rect)

        #! Endgame collison
        # Game freezes when game_active = False
        if rock_rect.colliderect(runner_rect):
            game_active = False
    
    #! Occurs when game_active = False
    else:
        screen.fill('Blue')
        pygame.draw.line(screen, 'Red', (0,0), (800,500)) and pygame.draw.line(screen, 'Red', (800,0), (0,500))
        screen.blit(gameover_text, gameover_rect)
      
    # Updating the screen, 60 times per second
    # (60fps)
    pygame.display.update()
    fps = clock.tick(60)
