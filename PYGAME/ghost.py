import pygame

class Ghost(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/ghost-x4.gif")
        self.image = pygame.transform.scale(self.image, [30,30])
        self.rect = pygame.Rect(50, 50, 30, 30)

        self.speed = 0
        self.accelleration = 0.1
        
    def update(self, *args):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed -= self.accelleration
        elif keys[pygame.K_a]:
            self.speed +=self.accelleration
        else:
            self.speed *= 0.95
        self.rect.y += self.speed

        if self. rect.top < 0:
           self.rect.top = 0
           self.speed = 0

        elif self.rect.bottom > 480:
             self.rect.bottom = 480
             self.speed = 0