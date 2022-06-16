import pygame 
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f"{current_time}",False,(64,64,64))
    score_rect = score_surf.get_rect(center = (350,50))
    screen.blit(score_surf,score_rect)

pygame.init() 
screen = pygame.display.set_mode((700, 400)) 
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True
start_time = 0

baground_surface = pygame.image.load("resources/image/baground.png").convert()

#score_surf = test_font.render("My game", False, "Black")
#score_rect = score_surf.get_rect(center = (350,50))

scorpion_surf = pygame.image.load("resources/image/scorpion.png").convert_alpha()
scorpion_rect = scorpion_surf.get_rect(bottomright = (600,350))

katak_surf = pygame.image.load("resources/image/katak.png").convert_alpha()
katak_rect = katak_surf.get_rect(topleft= (80,272))
katak_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if katak_rect.collidepoint(event.pos):
                    katak_gravity = -20
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and katak_rect.bottom >= 350:
                    katak_gravity = -20 
                
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                scorpion_rect.left = 700
                start_time = pygame.time.get_ticks()
        
    if game_active:
        screen.blit(baground_surface,(0,0))
        #pygame.draw.rect(screen, "#c0e8ec", score_rect)
        #pygame.draw.rect(screen, "#c0e8ec", score_rect,10)
        #screen.blit(score_surf,score_rect)
        display_score()
        
        scorpion_rect.x -= 4
        if scorpion_rect.right <= 0: scorpion_rect.left = 700
        screen.blit(scorpion_surf,(scorpion_rect))
        
        #katak
        katak_gravity += 1   
        katak_rect.y += katak_gravity
        if katak_rect.bottom >= 350: katak_rect.bottom = 350
        screen.blit(katak_surf,katak_rect)
            
        #collistion
        if scorpion_rect.colliderect(katak_rect):
            game_active = False
            
    else:
        screen.fill("yellow")
        
        
    pygame.display.update()
    clock.tick(60)
    