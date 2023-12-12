import pygame

pygame.init()
pygame.display.set_caption("Geometry_de")
screen = pygame.display.set_mode((1080, 720))
bg = pygame.image.load("assets/images/background/background.png")

clock = pygame.time.Clock()
running = True

while running:

    #couleur de l'arrière plan mettre la couleur avant car sinon le bg sera derière la couleur
    screen.fill((255, 0, 0))

    #ajout de l'arrière plan dans l'app
    screen.blit(bg, (0, 0))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
