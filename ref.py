import pygame
import random

WIDTH = 500
HEIGHT = 500
size = (WIDTH, HEIGHT)

desease_par = 10
contagious_par = 60

humans = pygame.sprite.Group()
borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()

file_green = open('green.txt', "w")
file_red = open('red.txt', "w")


class Human(pygame.sprite.Sprite):
    def __init__(self, radius):
        super().__init__(humans)
        self.radius = radius
        if random.randint(1, 100) <= desease_par:
            self.color = pygame.Color("red")
        else:
            self.color = pygame.Color("green")
        
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        
        position_x = random.randint(0, WIDTH - 2 * radius)
        position_y = random.randint(0, HEIGHT - 2 * radius)
        self.rect = pygame.Rect(position_x, position_y, 2 * radius, 2 * radius)
        
        self.v_x = random.randint(-5, 5)
        self.v_y = random.randint(-5, 5)

def update(self):
    self.rect = self.rect.move(self.v_x, self.v_y)

    if pygame.sprite.spritecollideany(self, vertical_borders):
        self.v_x *= -1
    if pygame.sprite.spritecollideany(self, horizontal_borders):
        self.v_y *= -1

    if pygame.sprite.spritecollideany(self, humans):
        if pygame.sprite.spritecollideany(self, humans) != self:
            other = pygame.sprite.spritecollideany(self, humans)
    
    if self.color == pygame.Color('green') and other.color == pygame.Color('red'):
        if random.randint(1, 100) <= contagious_par:
            self.color = pygame.Color('red')
            self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA, 32)
            pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)



class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(borders)

        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

for _ in range(50):
    Human(10)
Border(5, 5, WIDTH - 5, 5)
Border(5, HEIGHT - 5, WIDTH - 5, HEIGHT - 5)
Border(WIDTH - 5, 5, WIDTH - 5, HEIGHT - 5)
Border(5, 5, 5, HEIGHT - 5)

running = True
steps = 0
while running:
    count_red = 0
    count_green = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if steps > 500:
            running = False
    screen.fill(pygame.Color("white"))
    humans.draw(screen)
    humans.update()
    borders.draw(screen)
    
    for human in humans:
        if human.color == pygame.Color('green'):
            count_green += 1
        else:
            count_red += 1
    
    print(count_green, file=file_green)
    print(count_red, file=file_red)
    
    pygame.display.flip()
    clock.tick(30)
    steps += 1

file_green.close()
file_red.close()
pygame.quit()