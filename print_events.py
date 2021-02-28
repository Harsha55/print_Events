import sys
import pygame
pygame.init()


green = (0, 255, 0)


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Print Events")
font = pygame.font.Font("freesansbold.ttf",30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            
            ev = "Key name: " + str(event.unicode) + " | code: "+ str(event.key)
            text = font.render(ev,True,green)
            textrect = text.get_rect()
            textrect.center = 500//2,500//2
            screen.fill("Black")
            screen.blit(text,textrect)
            
 
    pygame.display.flip()