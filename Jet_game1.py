import pygame 
import random
sound_initiol = pygame.mixer.init()
pygame_initiol = pygame.display.init()
font_initiol = pygame.font.init()
screen = pygame.display.set_mode((800,600))
caption = pygame.display.set_caption("My game")
background = pygame.transform.scale(pygame.image.load("css/bg_02_h.png"),(800,600))
plain1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("css/plane-animated-top-down-game-art.png"),(100,100)),270)
plain2 =  pygame.transform.rotate(pygame.transform.scale(pygame.image.load("css/firing.png"),(140,130)),90)
sound  = pygame.mixer.Sound("css/boom_c_06-102838.mp3")
messile =  pygame.transform.rotate(pygame.transform.scale(pygame.image.load("css/messssile-removebg-preview.png"),(40,90)),270)
data = {"plain1_x_pos":20,"plain1_y_pos":250,"plain2_x_pos":680,"plain2_y_pos":250,"bullet_state": "ready","bullet_x":30,"score": 0,'run':True}
high_score_data = [] 
game_over = pygame.font.SysFont('comicsans',40)
high_score = pygame.font.SysFont('comicsans',40)
bullet_y = data['plain1_y_pos']
score_board = pygame.font.SysFont('comicsans',40)
Clock = pygame.time.Clock()
board = pygame.font.SysFont('comicsans',40)
bullet_fixed_pos = []
while data["run"]:
    rect1_x = data["plain2_x_pos"]+60
    rect1_y = data["plain2_y_pos"]+25
    for event in pygame.event.get():
     if event.type==pygame.QUIT:run=False,pygame.quit(),exit()
    screen.blit(background,(0,0))
    rectangle2 = pygame.draw.rect(screen,(255,0,0),(rect1_x,rect1_y,5,85))
    screen.blit(plain1,(data["plain1_x_pos"],data['plain1_y_pos']))
    screen.blit(plain2,(data["plain2_x_pos"],data["plain2_y_pos"]))
    data["plain2_x_pos"]-=2
    if data["plain2_x_pos"]<=0:
     render = board.render("GAME OVER!",True,(255,0,0))
     screen.blit(render,(250,220))
     game_over_display = game_over.render("PRESS SPACE TO RETRY",True,(255,0,0))
     screen.blit(game_over_display,(180,290))
    score_rander = board.render(f"SCORE:{data['score']}",1,(255,0,0))
    screen.blit(score_rander,(20,20))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:data["plain1_y_pos"]-=2.3
    if keys[pygame.K_DOWN]:data["plain1_y_pos"]+=2.3
    if data["plain1_y_pos"]<0:data["plain1_y_pos"]=0
    if data["plain1_y_pos"]>=500:data["plain1_y_pos"]=500
    if keys[pygame.K_RIGHT]:data["bullet_state"]="fire";bullet_fixed_pos.append(data["plain1_x_pos"]) 
    if keys[pygame.K_SPACE]:data['plain2_x_pos']=680;data['plain2_y_pos']=250;data["plain1_y_pos"] =250
    if 'fire' in data["bullet_state"]:
        bullet = pygame.draw.rect(screen,(255,0,0),(data['bullet_x']+50,data["plain1_y_pos"]+46,30,9))
        screen.blit(messile,(bullet_fixed_pos+5,data['plain1_y_pos']+30))
        data["bullet_x"]+=1
        if bullet.colliderect(rectangle2):
          sound.play()
          data["score"]+=1
          plain2_x_pos = 720
          data["bullet_x"] = 20
          data["bullet_state"] = "ready"
          data["plain2_x_pos"] = 680
          ran = random.randint(50,500)
          data['plain2_y_pos'] = ran
    if data["bullet_x"]>rect1_x:
       data["bullet_x"] = 20
       data["bullet_state"] = "ready" 
    pygame.display.update() 
    Clock.tick(1000)