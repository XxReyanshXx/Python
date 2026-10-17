import random 
import pygame
class button():
     
        def __init__(self,x,y,pos,width,hieght): 
            self.x=x
            self.y=y
            self.width=width
            self.hieght=hieght
            self.pos=pos
        
        def clicked(self,pos):
            self.pos = pygame.mouse.get_pos()
            if self.pos[0] >self.x  and self.pos[0]< self.x+self.width :
                if self.pos[1] >self.y  and self.pos[1] < self.y+self.hieght :
                    return True
            return False
class RpsGame ():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960,640))
        pygame.display.set_caption("RPS Smasher")
        
        
        
        self.bg = pygame.image.load("background.jpg")
        self.r_btn = pygame.image.load("r_button.png").convert_alpha()
        self.p_btn = pygame.image.load("p_button.png").convert_alpha() 
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()
        
        
        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissors = pygame.image.load("scissors.png").convert_alpha()
        
        self.screen.blit(self.bg,(0,0))
        self.screen.blit(self.r_btn,(20,500))
        self.screen.blit(self.p_btn,(330,500))
        self.screen.blit(self.p_btn,(640,500))
        
        self.rock_btn=button(30,520,(30,520),300,140)
        self.paper_btn=button(340,520,(340,520),300,140)
        self.scissors_btn=button(640,520,(640,520),300,140)
        
        self.front = pygame.font.Font(('splach.ttf'),10)
        self.text = self.font.render(f"",True,(255,255,255))
        
        
        self.pl_score = 0
        self.pc_score = 0
    def player(self):
        if self.rock_btn.clicked(30):
            self.p_option = "rock"
            self.screen.blit(self.choose_rock,(120,200))
        
        elif self.paper_btn.clicked(340):
            self.p_option = "paper"
            self.screen.blit(self.choose_paper,(120,200))
            
        else:
            self.scissors_btn.clicked(640)
            self.p_option = "scissors"
            self.screen.blit(self.choose_scissors,(120,200))
            return self.p_option
    
        
        
    
    
            
                
                    
                
                

   
         
        
        
    
