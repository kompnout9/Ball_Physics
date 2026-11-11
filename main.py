import pygame
import itertools
from random import randint
import math
g = 900
floor_y = 600
wall_x = 1200
class Ball:
    _ids = itertools.count(1)

    def __init__(self, pos, radius = 36, color="Red"):
        self.id = next(Ball._ids)
        self.x, self.y = pos
        self.radius = radius
        self.color = color
        self.start_ball_time = pygame.time.get_ticks()
        self.vy,self.vx = 0,0
        self.ax,self.ay = 0,g
        
    def gravity(self,dt):
        self.vy += self.ay * dt # acceleration that is always directed downwards
        self.vx += self.ax * dt
        self.y += self.vy * dt
        self.x += self.vx * dt  # Guides the ball using this acceleration
        if self.y + self.radius >= floor_y: # Checks if the ball has crossed the border (taking its radius into account)
            self.y = floor_y - self.radius # He puts it on the border because it can go right through it
            
            
            self.vx *= 0.8
            self.vy = -self.vy * 0.8 # Changes the ball's direction upwards, taking energy loss into account
        if self.x + self.radius >= wall_x:
            self.x = wall_x - self.radius
        if self.x - self.radius <= 0:
            self.x = self.radius
    def check_ball_collision(ball1,ball2):
        dist = math.sqrt((ball1.x-ball2.x)**2+(ball1.y-ball2.y)**2)
        return dist <= ball1.radius + ball2.radius
              
            
               
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
        pass
        
def create_ball(screen,mouse_pos):
    pygame.draw.circle(screen, (randint(0,255),randint(0,255),randint(0,255)), mouse_pos, 40)

balls = []


pygame.init()
# pygame setup
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0   
while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
    pygame.draw.line(screen, "black", (0, floor_y), (1280, floor_y), 2)
    # RENDER YOUR GAME HERE
    if pygame.mouse.get_just_pressed()[0]:
        print("pressed")
        balls.append(Ball(pygame.mouse.get_pos(),color= (randint(0,255),randint(0,255),randint(0,255))))              
    for i in range(len(balls)):
        balls[i].draw(screen)
        balls[i].gravity(dt)
    for _ in range(10):
        for i in range(len(balls)):
            for f in range(i + 1, len(balls)):
                a, b = balls[i], balls[f]
                dx = b.x - a.x
                dy = b.y - a.y
                dist = math.hypot(dx, dy)
                min_dist = a.radius + b.radius

                if dist < min_dist:
                    if dist == 0:
                        dx, dy, dist = 1, 0, 1
                    nx, ny = dx / dist, dy / dist

                    # 1. раздвигаем
                    overlap = (min_dist - dist) / 2
                    a.x -= nx * overlap
                    a.y -= ny * overlap
                    b.x += nx * overlap
                    b.y += ny * overlap

                    # 2. меняем скорости
                    rvx = b.vx - a.vx # относительная скорость
                    rvy = b.vy - a.vy
                    vn = rvx * nx + rvy * ny   # скорость сближения вдоль нормали

                    if vn < 0:                 # шарики летят друг на друга
                        e = 0.3            # упругость (0 - слипаются, 1 - идеальный отскок)
                        impuls = -(1 + e) * vn / 2  # импульс (массы одинаковые)
                        a.vx -= impuls * nx
                        a.vy -= impuls * ny
                        b.vx += impuls * nx
                        b.vy += impuls * ny
                        print(f"nx:{nx} ny:{ny}")
    # flip() the display to put your work on screen
    pygame.display.flip()
     # limits FPS to 60
    dt = clock.tick(120) / 1000.0
pygame.quit()
