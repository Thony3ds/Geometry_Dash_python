import pygame
from assets.libs import button

pygame.init()
pygame.display.set_caption("Geometry_de")
screen = pygame.display.set_mode((1080, 720))
bg = pygame.image.load("assets/images/background/background.png")

clock = pygame.time.Clock()
running = True

#define font
font = pygame.font.SysFont("arialblack", 40)

#define colors
text_col = (255, 255, 255)

#load button images
resume_img = pygame.image.load("assets/images/logo/settings.png")

#create button instance
resume_button = button.Button(304, 125, resume_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

while running:

    #couleur de l'arrière plan mettre la couleur avant car sinon le bg sera derière la couleur
    screen.fill((255, 0, 0))

    resume_button.draw(screen)
    
    #ajout de l'arrière plan dans l'app
    screen.blit(bg, (0, 0))

    draw_text("Welcome", font, text_col, 540, 460)

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(90)  # limits FPS to 90

pygame.quit()
