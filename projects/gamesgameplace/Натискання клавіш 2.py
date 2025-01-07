from tkinter import Toplevel, Canvas
import sys
# Load and initialize Modules here
import pygame

# Main AnimalEat Class
class AnimalEat():
    WHITE = (255,255,255)
    c_zrv1 = (23,0,178)
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
           
           
        
        
    def __init__(self, displayw=800, displayh=600, name_game = "Поїдач"):
        # Window Information
        pygame.init()
        self.dw = displayw
        self.dh = displayh
        self.window = pygame.display
        # pygame.NOFRAME | https://youtu.be/RihDgtqRj58?list=PLA0M1Bcd0w8xg_hyqpPpHdbZnPubSyIQ_&t=941
        self.w = self.window.set_mode((self.dw,self.dh))
        self.window.set_caption(name_game)
        self.window.set_icon(pygame.image.load("gameimg/nam_nam.png").convert_alpha())
        
        self.one_x = self.dw // 2 - 75
        self.one_y = self.dh // 2 - 125
        self.x, self.y = 0, 0
        self.k = None
        
        # Clock
        self.windowclock = pygame.time.Clock()
        self.FPS = 10
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
            self.w.fill((255,255,255)) #Tuple for filling display... Current is white
            
            self.move_one(self.x, self.y) #zrv_function
            
            
            # Remember things on top get done first so they will update in the order yours is set at
            
            # Remember to update your clock and display at the end
            self.window.update()
            self.windowclock.tick(self.FPS)

        # If you need to reset variables here
        # This includes things like score resets

    # After your main loop throw in extra things such as a main menu or a pause menu
    # Make sure you throw them in your main loop somewhere where they can be activated by the user

# All player classes and object classes should be made outside of the main class and called inside the class
#The end of your code should look something like this
if __name__ == '__main__':
    AnimalEat()



