#thomais
#road game innit!!!!

#things to implement
    #score system - done in like 2 seconds easy af
    #cloning parcels - done
    #fixing colision on parcels - done
    #moving parcels -DONEEEE
    #obstacles -DONEZO
    #game over screen - DONE
    #title screen - done
    

import pygame, math, random, sys, time
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()

wi = 1280
hi = 720

clock = pygame.time.Clock()
screen = pygame.display.set_mode((wi, hi))
logo = pygame.image.load('images/logo.png').convert_alpha()
bg = pygame.image.load('images/road.png').convert_alpha()
bg = pygame.transform.scale(bg, (1280, 720))
bg_rect = bg.get_rect()
score = 0
pygame.display.set_icon(logo)
pygame.display.set_caption('road game innit')


class Player(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.hi = hi
        self.wi = wi
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)
        pygame.sprite.Sprite.__init__(self)
            
    def handle_keys(self):
        keys = pygame.key.get_pressed()
        dist = 5
                
        if keys[pygame.K_UP] and not self.rect.y < 100:
            self.rect.y -= dist
                
        if keys[pygame.K_DOWN] and self.rect.y < 380:
            self.rect.y += dist
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
         
class collect(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.wi = wi
        self.hi = hi
        self.vel = 5
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.rect.center = (x,y)
        self.mask = pygame.mask.from_surface(self.image)
        pygame.sprite.Sprite.__init__(self)
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
 
 
class obstacle(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        super().__init__()
        self.wi = wi
        self.hi = hi
        self.vel = 5
        self.image = image
        self.rect = self.image.get_rect(topleft = (x,y))
        self.rect.center = (x,y)
        self.mask = pygame.mask.from_surface(self.image)
        pygame.sprite.Sprite.__init__(self)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))       

   
def text_obs(text, font):
    font = pygame.font.Font('fontinnit/retrogaming.ttf', 55)
    text_surface = font.render(text, True, (200,0,0))
    return text_surface, text_surface.get_rect()


def display_text(text):        
    title = pygame.font.Font('fontinnit/retrogaming.ttf', 40)
    textsurf, textrect = text_obs(text, title)
    textrect.center = (1280/2, 720/2)
    screen.blit(textsurf, textrect)
    
    pygame.display.update()
    time.sleep(2)
    game()

def button(msg,x,y,w,h,ic,ac,action=None):
    global score
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    normal_size = pygame.font.Font('fontinnit/retrogaming.ttf',20)
    textsurf, textrect = text_obs(msg, normal_size)
    textrect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textsurf, textrect)
    
 
def game_over():
    over = True
    pygame.mixer.music.load('moo/defeat.ogg')
    pygame.mixer.music.play(0)
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        background = pygame.image.load('images/mainscreenbad.png').convert_alpha()
        background = pygame.transform.scale(background, (1280, 720))
        screen.blit(background, (0,0))
        title = pygame.font.Font(None, 55)
        textsurf, textrect = text_obs('game over', title)
        textrect.center = (1280/2, 200)
        screen.blit(textsurf, textrect)
        
        normal_size = pygame.font.Font(None, 24)
        textsurf, textrect = text_obs('retry', normal_size)
        textrect.center = ((465+(350/2), (300+(75/2))))
        screen.blit(textsurf, textrect)
        
        font = pygame.font.Font('fontinnit/retrogaming.ttf', 28)
        score_text = font.render(f'Score: {score}', True, (0,0,0))
        screen.blit(score_text, (560,240))
        
        message = font.render("now my van's all damaged >:(", True, (0,0,0))
        screen.blit(message, (400,100))
        
        broken_van = pygame.image.load('images/brokenvan.png').convert_alpha()
        broken_van = pygame.transform.scale(broken_van, (340, 320))
        screen.blit(broken_van, (50,300))
        
        
        
        
        button('retry',465,300,350,75,(255,255,0), (128,255,0),game)
        button('quit',465,435,350,75,(255,255,0),(128,255,9),quit)
        pygame.display.update()
        clock.tick(15)
        
    
       
def intro():
    global score
    intros = True
    pygame.mixer.music.load('moo/introsong.ogg')
    pygame.mixer.music.play(-1)
    background = pygame.image.load('images/mainscreen.png').convert_alpha()
    background = pygame.transform.scale(background, (1280, 720))
    while intros:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
              
        screen.blit(background, (0,0))
        title = pygame.font.Font('fontinnit/retrogaming.ttf', 72)
        textsurf, textrect = text_obs('road game innit', title)
        textrect.center = (1280/2, 200)
        screen.blit(textsurf, textrect)
        
        normal_size = pygame.font.Font('fontinnit/retrogaming.ttf', 24)
        textsurf, textrect = text_obs('play', normal_size)
        textrect.center = ((465+(350/2), (300+(75/2))))
        screen.blit(textsurf, textrect)
        
        button('play',465,300,350,75,(255,255,0), (128,255,0),game)
        button('quit',465,435,350,75,(255,255,0),(128,255,9),quit)
        
        nice_van = pygame.image.load('images/nicevan.png').convert_alpha()
        nice_van = pygame.transform.scale(nice_van, (340, 320))
        screen.blit(nice_van, (50,300))
        
        pygame.display.update()
        clock.tick(15)     
 
def quit():
    sys.exit()
                       
def game():
    global score
    font = pygame.font.Font('fontinnit/retrogaming.ttf', 24)
    player_image = pygame.image.load('images/royalvan.png').convert_alpha()
    player_image = pygame.transform.scale(player_image, (290, 160))
    players = Player(player_image, 450,255)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(players)

    parcel_image = pygame.image.load('images/parcel.png').convert_alpha()
    parcel_image = pygame.transform.scale(parcel_image, (80,80))
    all_parcels = pygame.sprite.Group()
    for i in range(2):
        x = random.randrange(1300,2000)
        y = random.randrange(200,475)
        new_parcels = collect(parcel_image, x, y)
        all_parcels.add(new_parcels)    
        
    cone_image = pygame.image.load('images/cone.png').convert_alpha()
    cone_image = pygame.transform.scale(cone_image, (65,65))
    all_conesl = pygame.sprite.Group()
    for i in range(1):
        x = random.randrange(1300, 4000) #1300 4000
        y = random.randrange(200,225)
        new_cones = obstacle(cone_image, x, y)
        all_conesl.add(new_cones)

    all_conesr = pygame.sprite.Group()
    for i in range(1):
        x = random.randrange(1300,4000)
        y = random.randrange(450,475)
        new_cones = obstacle(cone_image, x, y)
        all_conesr.add(new_cones)
        
    all_cones = pygame.sprite.Group()
    all_cones.add(all_conesl)
    all_cones.add(all_conesr)
         
    pygame.init()
    scroll = 0
    tiles = math.ceil(wi /bg.get_width()) + 1
        
    run = True
    pygame.mixer.music.load('moo/moosic.ogg')
    pygame.mixer.music.play(-1)

    
    if score != 0:
            score = 0   
    while run:
        
        clock.tick(50)
        i=0
        while(i<tiles):
            screen.blit(bg, (bg.get_width()* i + scroll, 0))
            i+=1
                    
        scroll -=6
                
        if abs(scroll) > bg.get_width():
            scroll = 0
         
        for i in all_parcels:
            i.rect.x -= 6
            if i.rect.right < 0:
                i.rect.x = random.randrange(1300,2000)
                i.rect.y = random.randrange(200,475)
          
        for i in all_parcels:
            if pygame.sprite.collide_mask(players, i):
                i.rect.x = random.randrange(1300,2000)
                i.rect.y = random.randrange(200,475)
                score += 1
        
        hit_list = pygame.sprite.groupcollide(all_sprites, all_cones, False, True, collided = pygame.sprite.collide_mask)
            
        for i in hit_list:
            if pygame.sprite.collide_rect(players, i):
                all_conesl.empty()
                all_conesr.empty()
                all_parcels.empty()
                all_sprites.empty()
                run = False
                game_over()
                
        for i in hit_list:
            if pygame.sprite.collide_rect(players, i):
                all_conesr.empty()
                all_conesl.empty()
                all_parcels.empty()
                all_sprites.empty()
                run = False
                game_over()
                
        for i in all_conesl:
            i.rect.x -= 6
            if i.rect.right < 0:
                i.rect.x = random.randrange(1300,4000)
                i.rect.y = random.randrange(200,225)
                
        for i in all_conesr:
            i.rect.x -= 6
            if i.rect.right < 0:
                i.rect.x = random.randrange(1300,4000)
                i.rect.y = random.randrange(450,475)
                
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                
        score_text = font.render(f'Score: {score}', True, (255,255,255))
        screen.blit(score_text, (1100,25))              
        players.handle_keys()  
        all_sprites.draw(screen)
        all_parcels.draw(screen)
        all_cones.draw(screen)
        pygame.display.update()
        
             
intro()
game()
game_over()     
pygame.quit()