import pygame
pygame.init()

#set dimension of screen
screen = pygame.display.set_mode((600,600))
screen.fill('blue')
pygame.display.update()

class Rectangle():
    def __init__(self,color,dimensions):
        self.color = color
        self.dimensions = dimensions
        self.surf = screen
    def draw(self):
        pygame.draw.rect(self.surf, self.color, self.dimensions)
rectangle = Rectangle('green',(200, 300, 60, 100))


#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rectangle.draw()
    pygame.display.update()
pygame.quit()

