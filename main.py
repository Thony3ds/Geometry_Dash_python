import pygame
from pygame.locals import *
from assets.levels.level1 import Level1

# Constantes
BG_COLOR = (204, 102, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x_speed = 0
        self.y_speed = 0
        self.jump = False

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not self.jump:
            self.y_speed = -15
            self.jump = True
        self.y_speed += 1  # Gravité
        self.rect.y += self.y_speed

        # Ajout du déplacement horizontal
        self.x_speed = 0
        if keys[pygame.K_LEFT]:
            self.x_speed = -5
        if keys[pygame.K_RIGHT]:
            self.x_speed = 5

        self.rect.x += self.x_speed

        if self.rect.bottom > 740:  # Limite inférieure de l'écran
            self.rect.bottom = 740
            self.jump = False

def main():
    pygame.init()

    screen = pygame.display.set_mode((1080, 740))
    pygame.display.set_caption('Geometry Trash')

    bg = pygame.image.load("assets/images/bg/background.png")

    # Initialisation du joueur
    player = Player(300, 300, "assets/images/player_skins/cube.png")
    # load the level
    level1 = Level1()
    level1.load_level()
    level1.add_bottom_cube(1000)  # Ajoute un cube tout en bas de l'écran

    clock = pygame.time.Clock()

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Seul le niveau se déplace vers la gauche
        for cube in level1.cubes:
            cube.rect.x -= 5  # Ajustez la vitesse du déplacement

        # Mise à jour du joueur
        player.update()

        # Vérifiez la collision avec les cubes du niveau
        for cube in level1.cubes:
            if player.rect.colliderect(cube.rect) and player.rect.x < cube.rect.x:
                print("Collision avec le cube ! Game Over")


        # Dessiner l'écran
        screen.fill(BG_COLOR)
        screen.blit(bg, (0, 0))  # Fond d'écran fixe
        level1.draw(screen)  # Dessinez le niveau après le fond
        screen.blit(player.image, player.rect)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()


