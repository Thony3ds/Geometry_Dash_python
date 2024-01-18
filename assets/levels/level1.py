# level1.py

import pygame

class Level1:
    def __init__(self):
        self.cubes = pygame.sprite.Group()
        self.bottom_cube_added = False

    def load_level(self):
        # Ajoutez les cubes à votre niveau
        cube1 = Cube(200, 500, "assets/images/levels_img/cube.png")
        cube2 = Cube(400, 400, "assets/images/levels_img/cube.png")
        cube3 = Cube(600, 300, "assets/images/levels_img/cube.png")

        self.cubes.add(cube1, cube2, cube3)

    def add_bottom_cube(self, x):
        if not self.bottom_cube_added:
            # Ajoutez un cube tout en bas de l'écran
            bottom_cube = Cube(x, 740 - 50, "assets/images/levels_img/cube.png")
            self.cubes.add(bottom_cube)
            self.bottom_cube_added = True  # Marquez que le cube a été ajouté

    def check_collisions(self, player):
        for cube in self.cubes:
            if player.rect.colliderect(cube.rect):
                # Vérifiez si le joueur touche la gauche du cube
                if player.rect.left < cube.rect.left:
                    # Le joueur touche la gauche du cube
                    return True
                # Vérifiez si le bas du joueur touche le haut du cube
                elif player.rect.bottom >= cube.rect.top:
                    # Ajustez le mouvement du joueur pour rester au-dessus du cube
                    player.rect.bottom = cube.rect.top
                    return False  # Le joueur ne meurt pas dans ce cas

        return False

    def draw(self, screen):
        # Dessinez les éléments du niveau, comme les cubes
        self.cubes.draw(screen)

class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
