from tkinter import Toplevel, Canvas
import sys
# Load and initialize Modules here
import pygame
from random import randint as ri

# Main AnimalEat Class
class AnimalEat():
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    c_zrv1 = (23,0,178)    
    EAT = ['морква.png','капуста.png','мяч.png']
    EATS = pygame.sprite.Group()
        
    def __init__(self, displayw=800, displayh=566, name_game = "Поїдач"):
        # Window Information
        pygame.init()
        self.dw = displayw
        self.dh = displayh
        self.window = pygame.display
        # pygame.NOFRAME | https://youtu.be/RihDgtqRj58?list=PLA0M1Bcd0w8xg_hyqpPpHdbZnPubSyIQ_&t=941
        
        self.w = self.window.set_mode((self.dw,self.dh))
        self.window.set_caption(name_game)
        self.window.set_icon(pygame.image.load("gameimg/nam_nam.png").convert_alpha())
                
        #фон
        self.bg = pygame.image.load("gameimg/bg1plus.jpeg").convert()
        self.w.blit(self.bg,(0,0)) #Tuple for filling display... Current is white
        
        self.eat_surf = [pygame.image.load("gameimg/"+path).convert_alpha() for path in self.EAT]
        
        
        
        #Додаємо зображення
        self.rabbit_surf = pygame.image.load("gameimg/rabbit_lead.png")
        self.rabbit_rect = self.rabbit_surf.get_rect(center=(self.dw // 2, self.dh // 2))
        
        self.w.blit(self.rabbit_surf, self.rabbit_rect)
        
        self.one_x = self.dw // 2 - 75
        self.one_y = self.dh // 2 - 125
        self.x, self.y = 0, 0
        
        
        # Clock
        self.windowclock = pygame.time.Clock()
        self.FPS = 10
        self.creatEat(self.EATS)
        self.Main()
        print('Букашка')
    def Main(self):
         #Put all variables up here
        stopped = False

        while stopped == False:
            

            #Event Tasking
            #Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    stopped == True
                elif event.type == pygame.KEYDOWN:
                    self.key(event.key, True)
                elif event.type == pygame.KEYUP:
                    self.key(event.key, False)
            

            #Add things like player updates here
            #Also things like score updates or drawing additional items
            
            #self.move_one(self.x, self.y) #zrv_function
            '''
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_LEFT]: self.one_x -= 20
            elif keys[pygame.K_RIGHT]: self.one_x += 20
            elif keys[pygame.K_UP]: self.one_y -= 20
            elif keys[pygame.K_DOWN]: self.one_y += 20
            
            self.one = pygame.draw.rect(self.w, self.c_zrv1, (self.one_x, self.one_y, 150, 250),5)
            # Remember things on top get done first so they will update in the order yours is set at
            '''
            # Remember to update your clock and display at the end
            self.window.update()
            self.windowclock.tick(self.FPS)
    
    def creatEat(self,group):
        indy = ri(0, len(self.eat_surf)-1)
        y = ri(20, self.dh-20)
        speed = ri(1,4)
        return Eat(y, speed, self.eat_surf[indy], group)
    
    def move_one(self,x,y):
        #print(x,y)
        self.one_x += x
        self.one_y += y
        self.one = pygame.draw.rect(self.w, self.c_zrv1, (self.one_x, self.one_y, 150, 250),5)
        
    def key(self, event, w):
        match [event, w]:
            case [pygame.K_LEFT, True]: self.x = -20
            case [pygame.K_LEFT,False]: self.x = 0
            case [pygame.K_RIGHT, True]: self.x = +20
            case [pygame.K_RIGHT,False]: self.x = 0
            case [pygame.K_UP, True]: self.y = -20
            case [pygame.K_UP,False]: self.y = 0
            case [pygame.K_DOWN, True]: self.y = +20
            case [pygame.K_DOWN,False]: self.y = 0


class Eat(pygame.sprite.Sprite):
    def __init__(self, y, speed, surf, group):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(center=(0,y))



if __name__ == '__main__':
    AnimalEat()


