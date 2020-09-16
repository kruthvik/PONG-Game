import pygame
import time
import random
from pygame.locals import*  

pygame.init()

#Paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Paddle, self). __init__()
        self.position = position
        self.color = (255, 255, 255)
        self.surface = pygame.Surface([PaddleWidth, PaddleHeight])
        self.surface.fill(tuple(self.color))
        self.rect = self.surface.get_rect()
        self.rect.centerx, self.rect.centery = self.position
        self.speed = 0
        self.score = 0
        self.streak = 0
        self.AI_Speed = 0
        self.skill = 0
        self.change = lambda y: self.rect.move_ip(0, y) 
    def abs(self, num):
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0
            
            
    def keyUpdate(self):

        self.get_pressed = pygame.key.get_pressed()

        if self.get_pressed[K_UP] or self.get_pressed[K_w]: self.speed += -0.5
        if self.get_pressed[K_DOWN] or self.get_pressed[K_s]: self.speed +=0.5 
        


    def update(self):
        screen.blit(self.surface, self.rect)
        
        
        if self.rect.top <= 0:
            self.rect.y = 0
            


        if self.rect.bottom >= height:
            self.rect.bottom = height
            
    def AIupdate(self):

        if __name__ == "__main__":
            self.streak = Player.streak
            
            if ball.dx == -2:
                if self.rect.centerx - ball.rect.centerx >  200:
                    try:
                        self.change(2 * self.abs(((300) - self.rect.y) / 12))
                    except:
                        self.change(0)
            elif self.rect.centerx - ball.rect.centerx < 190 and ball.dx == 2:
                try:
                    self.skill = (1.4 + (self.score / Player.score) / 5 * 4)
                except:
                    if self.score == 0 and Player.score == 0:
                        self.skill = 2
                    elif self.score == 0:
                        self.skill = 3.1
                    else:
                        self.skill = 3
                        
                self.AI_Speed = self.skill * self.score

                self.distance = ball.rect.centery - self.rect.centery
                self.change(1.1 * self.abs(self.distance / 12))
                
            


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.position = (250, 250)
        self.color = (255, 255, 255)
        self.surface = pygame.Surface((20, 20))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect()
        self.rect.centerx, self.rect.centery = self.position
        self.dx, self.dy = 2, -2

    def update(self):
        screen.blit(self.surface, self.rect)
        pygame.draw.rect(screen, pygame.Color("WHITE"), (self.rect.x, self.rect.y, self.surface.get_width(), self.surface.get_height()))

        if self.rect.left < 20:

            AI.score += 1
            AI.streak -= 0.4
            self.dx*= -1
            self.rect.center = (300, 300)
            AI.rect.centery = Player.rect.centery = 300
        if self.rect.right > width - 20:

            Player.score += 1
            AI.streak += 0.7
            self.dx *= -1
            self.rect.center = (300, 300)
            
            self.rect.center = (300, 300)
            AI.rect.centery = Player.rect.centery = 300
        if self.rect.top <= 0:
            
            self.dy *= -1
            
        if self.rect.bottom >= height:
            
            self.dy *= -1

        self.collision = pygame.sprite.collide_rect(self, Player)

        if (self.collision):

            self.rect.x += 8
            self.dx *= -1
            

        else:
            
            self.collision = pygame.sprite.collide_rect(self, AI)
            if (self.collision):
        
                self.rect.x -= 8
                self.dx *= -1
    
        self.rect.move_ip(self.dx, self.dy)

START = False
width, height = 765, 600
screen = pygame.display.set_mode([width, height])
running = True
USEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(USEREVENT, 20)


PaddleDistance = 40
PaddleHeight = 120
PaddleWidth = 20

Player = Paddle((PaddleDistance, 300))
AI = Paddle((width - PaddleDistance, 300))
ball = Ball()


def render():
    global running
    while running:


        
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

                
        Player.keyUpdate()
        screen.fill((0, 0, 0))

        #updates
        pygame.draw.rect(screen, pygame.Color("WHITE"), (344, 0, 10, height))
        pygame.draw.rect(screen , pygame.Color("WHITE"), (0, 88, width + 5, 5))
        
        Player.update()
        ball.update()
        AI.update()
        AI.AIupdate()
        Player.rect.move_ip(0, Player.speed)
        


        Player.speed *= 0.9

        display = f"{Player.score}          {AI.score}"
        font = pygame.font.SysFont(None, 76)
        text = font.render(display, True, pygame.Color('WHITE'))
        screen.blit(text, (250, 30))
        
        pygame.time.Clock().tick(120)
        

        pygame.display.flip()
        


    pygame.quit()
    raise SystemExit()


if __name__ == "__main__":
    render()

