#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
from nis import match
from os import read
from tokenize import maybe
import pygame, sys
import json
import random
import time
funcionarios = []
ovrs = []
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
from  time import sleep 

ovrgeral = 0
pygame.init()
pygame.display.set_caption('Capitalism III')
gameDisplay = pygame.display.set_mode((800, 600))
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (224, 224, 224)
light_blue = (173, 216, 230)
grey = (128, 128, 128)
blue = (0, 100, 250)
red = (255, 0, 0)
green = (0,128,0)
game_running = True
data = {
    'coins':100000,
    'AutoMiner':0,
    'AutoPreco':20,
    'UpClick':1,
    'UpPreco':20,
    'CapacidadePreco':300,
    'Capacidade':5,
    'Funcionarios':0,
    'RAutoMiner':0,
    'PrecoRAutoMiner':300,
    'gastos':0,
    'menos':1,
    "loan_bank":0,
    "ovrgeral":0
}

Funcionarios = data['Funcionarios']
clock = pygame.time.Clock()
box1 = pygame.image.load("Images/box1.png")
autog = data['Funcionarios']
cost2 = data['AutoPreco']
Capacidade = data['Capacidade']
CapacidadePreco = data['CapacidadePreco']
Capacidade = data['Capacidade']
svrate = '1'
text = ''
pygame.mixer.init()

font = pygame.font.Font('Fonts/freesansbold.ttf', 35)
fontpixel = pygame.font.Font('Fonts/pixelart.ttf', 35)

print(data)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def criarmedia(gameDisplay):
    global click
    running = True
    input_box = pygame.Rect(200, 150, 310, 35)
    opcao1 = ['Baseado em moedas', 'Baseado em level']
    opcaostr = opcao1[0]
    H1 = 0
    H2 = 0
    H1p = pygame.Rect(335,220,30,30)
    H2p = pygame.Rect(415,220,30,30)
    vez = True
    while running:
        gameDisplay.fill(grey)
        pygame.draw.rect(gameDisplay, black, H1p)
        pygame.draw.rect(gameDisplay, black, H2p)
        draw_text("Habilidade Media:", font, (255, 255, 255), gameDisplay, 40, 220)
        draw_text(str(H1), font, (255, 255, 255), gameDisplay, 338, 220)
        draw_text(str(H2), font, (255, 255, 255), gameDisplay, 420, 220)
        draw_text("-", font, (255, 255, 255), gameDisplay, 380, 220)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if H1p.collidepoint((event.pos)):
                    if event.button == 1:
                        H1 += 1
                    if event.button == 3:
                        H1 -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if H2p.collidepoint((event.pos)):
                    if event.button == 1:
                        H2 += 1
                    if event.button == 3:
                        H2 -= 1
            if H1 > 32:
                H1 = 32
            elif H2 > 32:
                H2 = 32
            elif H1 >= 10:
                H1p.w = 35
            elif H2 >= 10:
                H2p.w = 35
            elif H1 <= 10:
                H1p.w = 30
            elif H2 <= 10:
                H2p.w = 30

def Contratar_Trabalhadores():
    global click
    running = True
    input_box = pygame.Rect(200, 150, 310, 35)
    opcao1 = ['Baseado em moedas', 'Baseado em level']
    opcaostr = opcao1[0]
    H1 = 0
    H2 = 0
    H1p = pygame.Rect(335,220,30,30)
    H2p = pygame.Rect(415,220,30,30)
    V1 = 0
    V2 = 0
    V1p = pygame.Rect(335,220,30,30)
    H2p = pygame.Rect(415,220,30,30)
    vez = True
    nomes = ['Robert', 'José', 'Zari', 'John', 'Garry', 'Luís', 'Rory', 'Arnaldo', 'Amongus', 'Danilo', 'Fausto', 'Daniel', 'Sieg', 'Slade', 'Oliver', 'Nathaniel', 'StickMasterLuck']
    print(len(nomes))
    
    n = random.randrange(0,len(nomes))
    print(n)
    while running:
        gameDisplay.fill(grey)
        cost = H2*5000+data['coins']/4
        pygame.draw.rect(gameDisplay, black, input_box)
        pygame.draw.rect(gameDisplay, black, H1p)
        pygame.draw.rect(gameDisplay, black, H2p)
        draw_text(opcaostr, font, (255, 255, 255), gameDisplay, input_box.x, input_box.y)
        draw_text("Contratar Trabalhadores", font, (255, 255, 255), gameDisplay, 200, 50)
        draw_text("Habilidade Media:", font, (255, 255, 255), gameDisplay, 40, 220)
        draw_text("Nome:", font, (255, 255, 255), gameDisplay, 40, 260)
        draw_text(str(H1), font, (255, 255, 255), gameDisplay, 338, 220)
        draw_text(str(H2), font, (255, 255, 255), gameDisplay, 420, 220)
        draw_text("-", font, (255, 255, 255), gameDisplay, 380, 220)
        searchb = pygame.Rect(200,450,250,50)
        nome = pygame.Rect(145,262,150,30)
        draw_text(nomes[n], font,black, gameDisplay,155,260)
        pygame.draw.rect(gameDisplay, green, searchb)
        draw_text(f"{cost}",font,black,gameDisplay,220,455)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nome.collidepoint(event.pos):
                    n=random.randrange(0,len(nome))
                    print(n)
                if searchb.collidepoint(event.pos):
                    data['coins'] -= cost
                    ovr = random.randrange(H1,H2)
                    nome = nomes[n]
                    func = {
                        "Nome":f"{nome}",
                        "Ovr":int(ovr),
                        "Lvl":0
                    }
                    print(func)
                    arq = open(f'data/Funcionarios.txt', 'w')
                    arq.write(func['Nome'])
                    arq.close()
                    arq = open("data/ovrs.txt", "w")
                    arq.write(str(func['Ovr']))
                    arq.close()
                    with open("data/Funcionarios.txt") as file:
                        for line in file:
                            funcionarios.append(line)
                    with open("data/ovrs.txt") as file:
                        for line in file:
                            ovrs.append(line)
                    with open(f'Funcionarios/{nome}.json', 'w') as f:
                        json.dump(func,f)
                        H1 = 0
                        H2 = 0
                    data['ovrgeral'] += func['Ovr']
                        
                if input_box.collidepoint(event.pos):
                    if click:
                        if vez:
                           opcaostr = opcao1[1]
                           vez = False
                        elif vez == False:
                            opcaostr = opcao1[0]
                            vez = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if H1p.collidepoint((event.pos)):
                    if event.button == 1:
                        H1 += 1
                    if event.button == 3:
                        H1 -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if H2p.collidepoint((event.pos)):
                    if event.button == 1:
                        H2 += 1
                    if event.button == 3:
                        H2 -= 1
            if H1 > 32:
                H1 = 32
            elif H2 > 32:
                H2 = 32
            elif H1 >= 10:
                H1p.w = 35
            elif H2 >= 10:
                H2p.w = 35
            elif H1 <= 10:
                H1p.w = 30
            elif H2 <= 10:
                H2p.w = 30
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False             
        
        pygame.display.update()
        mainClock.tick(60)

def trabalhadores():
    data['coins'] += data['ovrgeral']

def bank():
    global text
    global click
    clock = pygame.time.Clock()
    input_box = pygame.Rect(280, 440, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color_error = pygame.Color('red')
    color = color_inactive
    active = False
    done = False
    button1 = pygame.Rect(40,505,95,39)
    button2 = pygame.Rect(640, 505, 29, 31)
    mx, my = pygame.mouse.get_pos()
    click = False
    pedir = 'Pedir'
    rect = pygame.Rect(button1.x, button1.y, 95,39)
    rect2 = pygame.Rect(button2.x, button2.y, 95,39)
    amount = 0
    error = False

    while not done:
        for event in pygame.event.get():
            text[:-1]
            #Pay button
            if event.type == pygame.MOUSEBUTTONDOWN:
              if rect2.collidepoint(event.pos):
                  if click:
                      if data['loan_bank'] > 0:
                          if data['coins'] > 0:
                            data['loan_bank'] = data['loan_bank'] - amount
                            data['coins'] = data['coins'] - amount
                            error = False
                            time.sleep(0.7)
                            text='Sucessfully'
                            active = not active
                            amount = 0

            #Give Button
            if error:
                pedir = 'Choose a number below 10000$'
            if active and text == 'Sucessfully' or active and text == 'Error':
                text = ''
                color = pygame.Color('dodgerblue2')
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
                pygame.quit()
            if active and pedir=='Choose a number below 10000$':
                pedir='Pedir'    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            print(text)
                            print(amount)
                            amount += int(text)
                            active = False
                        except:
                            print(error)
                    else:
                        text += event.unicode
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_KP_ENTER:
                        print(text)
                        amount += int(text)
                        active = False
            
            #Give Loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    if click:
                        if amount < 10001:
                            if data['loan_bank'] < 10001:
                                data['coins'] = amount + data['coins']
                                print(data['coins'])
                                error = False
                                data['loan_bank'] = data['loan_bank'] + amount
                                time.sleep(0.7)
                                print(f"{data['loan_bank']} é seu empréstimo")
                                text='Sucessfully'
                                amount = 0
                            else:
                                text = 'Error'
                                color = pygame.Color('red')
                                amount = 0
                        else:
                            text = 'Error'
                            color = pygame.Color('red')
                            amount = 0
            
            if data['loan_bank'] > 10000:
                data['loan_bank'] = 10000
                data['coins'] = data['coins'] - amount
                            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                  click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_game()
            
        gameDisplay.fill((30, 30, 30))
        draw_text(f"Your money: {data['coins']}", font, black, gameDisplay, 25, 85)
        draw_text(f"Loan to bank: {data['loan_bank']}", font, black, gameDisplay, 25, 85*2)
        draw_text('Back to game',font,black,gameDisplay,545,570)
        draw_text('Bank', font, (255, 255, 255), gameDisplay, 300, 40)
        draw_text(pedir,font,green,gameDisplay, button1.x, button1.y)
        draw_text("Pegar",font,red,gameDisplay,640,505)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        gameDisplay.blit(txt_surface, (input_box.x+10, input_box.y-2))
        pygame.draw.rect(gameDisplay, color, input_box, 2)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)
        
def main_menu():
    while True:
        global click
        gameDisplay.fill(grey)
        draw_text('Bank', font, (255, 255, 255), gameDisplay, 285, 40)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(280, 150, 200, 81)
        gameDisplay.blit(jogarpng, button_1)
        draw_text("Play", fontpixel, black, gameDisplay, 331, 174)
        if button_1.collidepoint((mx, my)):
            if click:
              main_game()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                  click = True

        pygame.display.update()
        mainClock.tick(60)


xxx = pygame.image.load("Images/stat.png")
fundostat = pygame.transform.scale(xxx, (800,600))

def Stats():
    while True:
        button_1 = pygame.Rect(478, 522, 398, 46)
        gameDisplay.blit(fundostat, (0,0))
        draw_text('Back to game', font, black, gameDisplay, 475, 520)
        coins = data['coins']
        UpClick = data['UpClick']
        rautominer = data['RAutoMiner']
        draw_text(f'              Stats:       ', font, black, gameDisplay, 10, 100)
        draw_text(f'Coins = {coins} |', font, black, gameDisplay, 10+48,200)
        draw_text(f'Workers Level = {rautominer}', font, black, gameDisplay, 10+48, 300)
        draw_text(f'Workers = {Funcionarios}/{Capacidade} |', font, black, gameDisplay, 10+48, 400)
        draw_text(f"Salary Expenses = {gastosrand}", font, grey, gameDisplay, 10+48, 470)
        draw_text(f" Server rate = {svrate}", font, black, gameDisplay, 300+48, 200)
        draw_text(f" Click level = {UpClick}", font, black, gameDisplay, 400, 400)

        mx, my = pygame.mouse.get_pos()

        
        if button_1.collidepoint((mx, my)):
            if click:
                main_game()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                  click = True

        pygame.display.update()
        mainClock.tick(60)

def autominer():
    global data
    data['coins'] = data['coins'] + data['AutoMiner']
    ccc = Funcionarios * data['RAutoMiner']
    data['coins'] += ccc

computador = pygame.image.load("Images/pc.png")
computador2 = pygame.transform.scale(computador, (100,115))
site = False

def loja():
    while True:
        global Capacidade
        gameDisplay.blit(lojafundo1, (0, 0))
        draw_text('Store', font, (255, 255, 255), gameDisplay, 260, 16)
        global data

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(130, 145, 100, 100)
        button_2 = pygame.Rect(450,520,350,50)
        button_3 = pygame.Rect(122,270,100,100)
        button_4 = pygame.Rect(260, 142, 100, 100)
        #Expansion event
        if button_1.collidepoint((mx, my)) and data['coins'] > CapacidadePreco:
          if click:
                data['Capacidade'] = data['Capacidade'] + 5
                data['CapacidadePreco'] = data['CapacidadePreco'] * 3
                data['coins'] = data['coins'] - CapacidadePreco
        #Back-to-game event
        if button_2.collidepoint((mx,my)):
            if click:
                main_game()
                with open('data/data.txt') as score:
                    data = json.load(score)
        #AutoMiner Upgrade
        if button_3.collidepoint((mx,my)) and data['coins'] > data['PrecoRAutoMiner'] and data['coins'] > -1:
            if click:
                data['coins'] = data['coins'] - data['PrecoRAutoMiner']
                data['RAutoMiner'] += 0.5
                data['PrecoRAutoMiner'] = data['PrecoRAutoMiner'] * 2
        
        gameDisplay.blit(martelo, button_3)
        gameDisplay.blit(computador2, button_4)
        box1m = pygame.transform.scale(box1,(100,100))
        gameDisplay.blit(box1m, (130,137))
        draw_text("Back to Game", font, black, gameDisplay, 457, 520)
        chocolate = data['CapacidadePreco']
        peppapig = data['PrecoRAutoMiner']
        coins = data['coins']
        draw_text(f"{chocolate}", font, black, gameDisplay, 129,125)
        draw_text(f"{peppapig}", font, black, gameDisplay, 135, 256)
        draw_text(f"{coins}", font, black, gameDisplay, 600,16)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("wowowowow")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                  click = True

        pygame.display.update()
        mainClock.tick(60)

def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))

ver = "2.4"

imagempic = pygame.image.load("Images/Picareta.png")
redimensao = pygame.transform.scale(
imagempic, (140, 140))
martelo1 = pygame.image.load("Images/martelo.png")
martelo = pygame.transform.scale(martelo1, (100,100))
imagemmoeda = pygame.image.load("Images/Moeda2.png")
redimensaomoeda = pygame.transform.scale(imagemmoeda, (40, 40))
lojaimagem = pygame.image.load("Images/loja.png")
imagemloja = pygame.transform.scale(lojaimagem, (31, 29))
imagemUP = pygame.image.load("Images/UpArrow.png")
redimensaoUP = pygame.transform.scale(
imagemUP, (140, 140))
fundomain = pygame.image.load("Images/mainfundo.png")
mainfundo = pygame.transform.scale(fundomain, (800,600))
worker = pygame.image.load("Images/WorkersList.png")
nsei = pygame.transform.scale(worker, (60, 60))
lojanseiq = pygame.image.load("Images/lojafundo.png")
lojafundo1 = pygame.transform.scale(lojanseiq,(800,600))
jogarpngq = pygame.image.load("Images/PlayButton.png")
jogarpng = pygame.transform.scale(jogarpngq, (200,87))
bancopng1 = pygame.image.load("Images/bancopng.png")
bancopng = pygame.transform.scale(bancopng1,(31,29))
Configimg = pygame.image.load("Images/Config.png")
Config = pygame.transform.scale(Configimg, (40,40))
mutedimg = pygame.image.load("Images/muted.png")
muted = pygame.transform.scale(mutedimg, (40,40))
unmutedimg = pygame.image.load("Images/unmuted.png")
unmuted = pygame.transform.scale(unmutedimg, (40,40))
int_volume = 0.5

pygame.mixer.music.load("Musics/openttdtheme.mp3")
pygame.mixer.music.set_volume(int_volume)
pygame.mixer.music.play()

def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('Fonts/freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)

def main_game():
    global gastosrand
    global Capacidade
    global game_running
    global Funcionarios
    global clock
    global autog
    global ver
    global color1
    global color2
    global color3
    global Funcionarios
    global CapacidadePreco
    mong = 0
    cost = 20
    cost2 = 20
    qinvestir = 0
    global data
    while game_running:
        trabalhadores()
        gastosrand = random.randrange(0, data['menos'])
        if Funcionarios > 4:
            data['coins'] = data['coins'] - gastosrand
        autominer()
        gameDisplay.fill(light_blue)
        rectangle(gameDisplay, red, 600, 500, 200, 200)
        rectangle(gameDisplay, light_grey, 655, 130, 100, 40)
        rectangle(gameDisplay, black, 600, 500, 20, 20)
        DrawText("Upygamerade click! Cost: " + str(data['UpPreco']), black, light_blue, 670,
                 386, 20)
        DrawText("" + str(qinvestir) + "   inv", black, blue, 30, 554, 20)
        DrawText("Buy auto miner! Cost:" + str(data['AutoPreco']), black, light_blue, 130,
                 390, 20)
        DrawText("Workers: " + str(f"{data['Funcionarios']}/{data['Capacidade']}"), black, light_blue, 77, 360, 20)
        gameDisplay.blit(mainfundo,(0,0))
        DrawText("Version: " + ver, black, light_blue, 650, 50, 20)
        DrawText("Load", black, light_blue, 704, 116, 20)
        DrawText("Invest", black, light_blue, 38, 120, 20)
        gameDisplay.blit(imagemloja, (770, 285))
        gameDisplay.blit(redimensaoUP, (632, 432))
        rectangle(gameDisplay, blue, 0, 140, 90, 30)
        rectangle(gameDisplay, red, 70, 140, 30, 30)
        gameDisplay.blit(nsei, (0, 200))
        gameDisplay.blit(redimensao, (34, 430))
        rectangle(gameDisplay, grey, 355, 590, 120, 150)
        banco123 = pygame.Rect(770, 257, 31,29)
        loja123 = pygame.Rect(770,285,31,29)
        gameDisplay.blit(bancopng,(banco123))
        config = pygame.Rect(760,15,40,40)
        gameDisplay.blit(Config,config)
        DrawText("     " + str(data['coins']) + " coins", black, light_blue, 120,
                 50, 30)
        gameDisplay.blit(redimensaomoeda, (10, 30))

        pygame.display.update()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.QUIT:
                with open('data/data.txt', 'w') as score:
                    json.dump(data, score)
                    a
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if mx > 315 and mx < 488:
                   if my < 300 and my > 130:
                       workers_list()

                if mx > 656 and mx < 756:
                    if my < 170 and my > 127:
                        try:
                            with open('data/data.txt') as score:
                                data = json.load(score)
                            autog = data['AutoMiner']
                            cost2 = data['AutoPreco']
                        except:
                            print("Nenhum arquivo encontrado!")

                if mx > 600 and my > 400:
                    workers_list()

                if mx < 200 and my > 400 and data["Capacidade"] > data['Funcionarios']:
                    print("vai")
                    Contratar_Trabalhadores()
                if mx < 70:
                    if my > 137 and my < 170:
                        qinvestir += 100

                if mx < 100 and mx > 70:
                    print("sa")                
                if mx > 0 and mx < 60:
                    if my > 200 and my < 260:
                        Stats()
                if loja123.collidepoint((mx,my)):
                  loja()
                if banco123.collidepoint((mx,my)):
                  bank()
                if config.collidepoint((mx,my)):
                    config_screen()

        pygame.display.update()
        clock.tick(30)

def config_screen():
    global int_volume
    mx, my = pygame.mouse.get_pos()
    running = True
    while running:
        gameDisplay.fill((grey))
        mute = 1
        draw_text('Config', font, (255, 255, 255), gameDisplay, 130, 30)
        draw_text('Volume:', font, (255, 255, 255), gameDisplay, 120, 150)
        volume = pygame.Rect(260,150,120,40)
        pygame.draw.rect(gameDisplay,black,volume)
        draw_text(str(int_volume),font,(255,255,255), gameDisplay, 300,150+5)
        un_muted = pygame.Rect(400,150,40,40)
        if mute == 1:
            gameDisplay.blit(unmuted, (400,150))
        if mute==2:
            gameDisplay.blit(muted,(400,150))
            int_volume=0
        if int_volume == 0:
            gameDisplay.blit(muted,(400,150))            
        if int_volume != 0:
                mute=1

        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if un_muted.collidepoint(event.pos):
                    print("amanha tem ciencie?")
                    mute = 2
                    int_volume=0.0
                    pygame.mixer.music.set_volume(int_volume)


                if volume.collidepoint(event.pos):
                    if event.button == 1:
                        int_volume += 0.1
                    if event.button == 3:
                        int_volume-=0.1
                    if int_volume > 1:
                        int_volume = 0
                    if int_volume < 0:
                        int_volume = 1
                    int_volume = round(int_volume,1)
                    pygame.mixer.music.set_volume(int_volume)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def workers_list():
    running = True
    print(funcionarios)
    while running:
        gameDisplay.fill((0,0,0))
        i=50
        x=50
        for n in range(0,len(funcionarios)):
            DrawText(funcionarios[n]+":", white,black,130,30+i,40)
            i+=50
        for n in range(0,len(ovrs)):
            DrawText(ovrs[n]+" OverAll", white,black,270,30+x,40)
            x+=50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        gameDisplay.fill((0,0,0))
        draw_text('www.com', font, (255, 255, 255), gameDisplay, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()
#--------------//----------#