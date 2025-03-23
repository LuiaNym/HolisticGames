import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 16)
sprite1 = pygame.image.load('../../images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (50, 50))
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()
pygame.display.set_caption("Hello Resize")
screen.fill((0, 0, 0))
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, (screen.get_width()/2 - spriteWidth/2, screen.get_height()/2 - spriteHeight/2))
    pygame.display.update()
pygame.quit()