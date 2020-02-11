import pygame


class Spritesheet:
    def __init__(self, image, width, height, padding):
        self.image = image
        self.width = width
        self.height = height
        self.padding = padding

    def get_image(self, x, y):
        surf = pygame.Surface((self.width, self.height))
        dest = [x * self.width, y * self.height]
        if x > 0:
            # add in padding
            dest[0] += (x - 1) * self.width
        if y > 1:
            dest[1] += (y - 1) * self.height
        surf.blit(self.image, (0, 0), dest)
        return surf
