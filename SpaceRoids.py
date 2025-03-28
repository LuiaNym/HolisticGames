import pygame
import random
from pygame import Vector2
from pygame.transform import rotozoom
from pygame.mixer import Sound

asteroid_images = ['images/asteroid1.png', 'images/asteroid2.png', 'images/asteroid3.png']


def blit_rotated(position, image, forward, screen):
    angle = forward.angle_to(Vector2(0, -1))
    rotated_surface = rotozoom(image, angle, 1.0)
    rotated_surface_size = Vector2(rotated_surface.get_size())
    blit_position = position - rotated_surface_size // 2
    screen.blit(rotated_surface, blit_position)


def wrap_position(position, screen):
    x, y = position
    w, h = screen.get_size()
    return Vector2(x % w, y % h)


class Ship:
    def __init__(self, position):
        self.position = Vector2(position)
        self.image = pygame.image.load('images/ship.png')
        self.forward = Vector2(0, -1)
        self.bullets = []
        self.can_shoot = 0
        self.speed = 2  # Speed for forward/backward motion
        self.shoot = Sound('sounds/shoot.wav')

    def update(self):
        is_key_pressed = pygame.key.get_pressed()

        # Forward motion (up arrow)
        if is_key_pressed[pygame.K_UP]:
            self.position += self.forward * self.speed
        # Backward motion (down arrow)
        if is_key_pressed[pygame.K_DOWN]:
            self.position -= self.forward * self.speed
        # Rotate left (left arrow)
        if is_key_pressed[pygame.K_LEFT]:
            self.forward = self.forward.rotate(-2)
        # Rotate right (right arrow)
        if is_key_pressed[pygame.K_RIGHT]:
            self.forward = self.forward.rotate(2)
        # Shooting (space bar)
        if is_key_pressed[pygame.K_SPACE] and self.can_shoot == 0:
            self.bullets.append(Bullet(Vector2(self.position), self.forward * 10))
            self.shoot.play()
            self.can_shoot = 500
        # Cooldown for shooting
        if self.can_shoot > 0:
            self.can_shoot -= clock.get_time()
        else:
            self.can_shoot = 0

    def draw(self, screen):
        self.position = wrap_position(self.position, screen)
        blit_rotated(self.position, self.image, self.forward, screen)


class Bullet:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self):
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), [self.position.x, self.position.y, 5, 5])


class Asteroid:
    def __init__(self, position, size):
        self.position = Vector2(position)
        self.velocity = Vector2(random.randint(-3, 3), random.randint(-3, 3))
        self.image = pygame.image.load(asteroid_images[size])
        self.radius = self.image.get_width() // 2
        self.explode = Sound('sounds/explode.mp3')
        self.size = size

    def update(self):
        self.position += self.velocity

    def draw(self, screen):
        self.position = wrap_position(self.position, screen)
        blit_rotated(self.position, self.image, self.velocity, screen)

    def hit(self, position):
        if self.position.distance_to(position) <= self.radius:
            self.explode.play()
            return True
        return False


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Asteroids")
background = pygame.image.load('images/space.png')
game_over = False
ship = Ship((100, 700))
asteroids = []
out_of_bounds = [-150, -150, 950, 950]
for i in range(3):
    asteroids.append(Asteroid((random.randint(0, screen.get_width()),
                               random.randint(0, screen.get_height())), 0))

font = pygame.font.Font('fonts/Alien.ttf', 80)
text_loser = font.render("You Lost!", True, (255, 255, 255))
text_loser_position = ((screen.get_width() - text_loser.get_width()) // 2,
                       (screen.get_height() - text_loser.get_height()) // 2)

font2 = pygame.font.Font('fonts/Alien.ttf', 80)
text_winner = font2.render("You Won!", True, (255, 255, 255))
text_winner_position = ((screen.get_width() - text_winner.get_width()) // 2,
                        (screen.get_height() - text_winner.get_height()) // 2)

clock = pygame.time.Clock()
while not game_over:
    clock.tick(55)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(background, (0, 0))

    if ship is None:
        screen.blit(text_loser, text_loser_position)
        pygame.display.update()
        continue

    if len(asteroids) == 0:
        screen.blit(text_winner, text_winner_position)
        pygame.display.update()
        continue

    ship.update()
    ship.draw(screen)

    for a in asteroids:
        a.update()
        a.draw(screen)
        if a.hit(ship.position):
            ship = None
            break

    if ship is None:
        continue

    deadbullets = []
    deadasteroids = []

    for b in ship.bullets:
        b.update()
        b.draw(screen)

        if b.position.x < out_of_bounds[0] or \
                b.position.x > out_of_bounds[2] or \
                b.position.y < out_of_bounds[1] or \
                b.position.y > out_of_bounds[3]:
            if not deadbullets.__contains__(b):
                deadbullets.append(b)

        for a in asteroids:
            if a.hit(b.position):
                if not deadbullets.__contains__(b):
                    deadbullets.append(b)
                if not deadasteroids.__contains__(a):
                    deadasteroids.append(a)

    for b in deadbullets:
        ship.bullets.remove(b)

    for a in deadasteroids:
        if a.size < 2:
            asteroids.append(Asteroid(a.position, a.size + 1))
            asteroids.append(Asteroid(a.position, a.size + 1))
        asteroids.remove(a)

    pygame.display.update()
pygame.quit()
