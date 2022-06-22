import pygame
from sys import exit

def display_score():
    current_time = (pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"Score:{current_time}",False,(64,64,64))
    score_rect = score_surf.get_rect(center = (350,50))
    screen.blit(score_surf,score_rect)
    return current_time

pygame.init() 
screen = pygame.display.set_mode((700, 400)) 
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True
start_time = 0
score = 0

baground_surface = pygame.image.load("resources/baground.png").convert()

#score_surf = test_font.render("My game", False, "Black")
#score_rect = score_surf.get_rect(center = (350,50))

scorpion_surf = pygame.image.load("resources/scorpion/scorpion1.png").convert_alpha()
scorpion_rect = scorpion_surf.get_rect(bottomright = (600,350))

katak_surf = pygame.image.load("resources/katak/katak_walk_1.png").convert_alpha()
katak_rect = katak_surf.get_rect(midbottom= (80,272))
katak_gravity = 0

#intro screen
katak_stand = pygame.image.load("resources/katak/katak_stand.png").convert_alpha()
katak_stand = pygame.transform.rotozoom(katak_stand,0,2)
katak_stand_rect = katak_stand.get_rect(center = (350,200))

game_name = test_font.render("Pixel Runner",False,(111,196,169))
game_name_rect = game_name.get_rect(center = (350,80))

game_message = test_font.render("Press space to run",False,(100,196,169))
game_message_rect = game_message.get_rect(center = (350,300)) 

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

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
                start_time = int(pygame.time.get_ticks() / 1000)
        
        if event.type == obstacle_timer: 
            print("test")
        
    if game_active:
        screen.blit(baground_surface,(0,0))
        #pygame.draw.rect(screen, "#c0e8ec", score_rect)
        #pygame.draw.rect(screen, "#c0e8ec", score_rect,10)
        #screen.blit(score_surf,score_rect)
        score = display_score()
        
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
        screen.fill((94,129,162))
        screen.blit(katak_stand,katak_stand_rect)
        
        score_message = test_font.render(f"your score: {score}",False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (350,350))
        screen.blit(game_name,game_name_rect)
        screen.blit(game_message,game_message_rect)
        
        if score == 0:screen.blit(game_message,game_message_rect)
        else:screen.blit(score_message,score_message_rect)
        
    pygame.display.update()
    clock.tick(60)
    