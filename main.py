import sys, pygame
import spritesheet as spsh
import pokemonutil
import pglobals
import pygame.freetype
import math
import time
from moves import movePowers
import random

menuStage = 1
mouseClickX = 0
mouseClickY = 0

#stats are as follows:
#HP      0
#ATK     1
#DEF     2
#SP ATK  3
#SP DEF  4
#SPEED   5

pglobals.initialise()

selectCursor = pygame.image.load("selected.png")
chosenMoveIndex = 0

while pglobals.ownPokemonName == None:
    pokemonutil.setPokemonData(input("Choose your Pokémon: "), "own")
while pglobals.oppPokemonName == None:
    pokemonutil.setPokemonData(input("Choose your opponent's Pokémon: "), "opponent")
pglobals.ownPokemonImg = pygame.transform.scale(pglobals.ownPokemonImg, (pglobals.ownPokemonImg.get_size()[0] * 3, pglobals.ownPokemonImg.get_size()[1] * 3))
pglobals.oppPokemonImg = pygame.transform.scale(pglobals.oppPokemonImg, (pglobals.oppPokemonImg.get_size()[0] * 4, pglobals.oppPokemonImg.get_size()[1] * 4))
while pglobals.ownPokemonLvl == None:
    pokemonutil.setPokemonLevel(input("Set your Pokémon's level: "), "own")
while pglobals.oppPokemonLvl == None:
    pokemonutil.setPokemonLevel(input("Set your opponent's Pokémon's level: "), "opponent")

pokemonutil.calculatePokemonStats("own")
pokemonutil.calculatePokemonStats("opponent")

pygame.init()

font = pygame.freetype.Font("fonts/Pokemon GB.ttf", 12)
fontMid = pygame.freetype.Font("fonts/Pokemon GB.ttf", 24)
fontLarge = pygame.freetype.Font("fonts/Pokemon GB.ttf", 36)

size = width, height, = 1000, 600

logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Semi-functional Pokémon Battle")

screen = pygame.display.set_mode(size)

pygame.mixer.init()
pygame.mixer.music.load("rgbyBattleMusic.mp3")
pygame.mixer.music.play()

bg = pygame.image.load("grasslandBG.png")
textBox = pygame.image.load("textBox.png")
textBox = pygame.transform.scale(textBox, (1000, 150))

hpBarsSS = spsh.spritesheet("hpBars.png")
opponentHpBarImg = hpBarsSS.image_at((0, 0, 242, 72), (0, 0, 0))
ownHpBarImg = hpBarsSS.image_at((258, 0, 513, 97), (0, 0, 0))

battlePlate = pygame.image.load("grasslandBattlePlates.png")
oppBattlePlate = pygame.image.load("opponentBattlePlate.png")

ownPokemonMaxHPImg, rect = font.render(str(pglobals.ownPokemonMaxHP), (72, 72, 72))

maxImg = pygame.image.load("max.png")
midImg = pygame.image.load("mid.png")
minImg = pygame.image.load("min.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClickX, mouseClickY = event.pos

    if pglobals.oppPokemonStats[0] <= 0:
        pygame.mixer.music.load("victory.mp3")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        screen.blit(textBox, (0, 450))
        exitMsgImg, rect = fontMid.render(pglobals.oppPokemonName.upper() + " FAINTED! " + pglobals.ownPokemonName.upper() + " WINS!", (72, 72, 72))
        screen.blit(exitMsgImg, (80, 480))
        screen.blit(opponentHpBarImg, (0, 50))
        screen.blit(oppPokemonNameImg, (5, 75))
        screen.blit(oppPokemonLvlImg, (170, 75))
        pygame.display.flip()
        time.sleep(5)
        sys.exit()

    screen.blit(bg, (0, 0))
    screen.blit(battlePlate, (0, 0))
    screen.blit(oppBattlePlate, (100, 0))
    
    screen.blit(pglobals.ownPokemonImg, (150 - (pglobals.ownPokemonImg.get_size()[0]/2), 500 - (pglobals.ownPokemonImg.get_size()[1])))
    screen.blit(pglobals.oppPokemonImg, (675 - (pglobals.oppPokemonImg.get_size()[0]/2), 400 - (pglobals.oppPokemonImg.get_size()[1])))
    
    screen.blit(opponentHpBarImg, (0, 50))
    screen.blit(ownHpBarImg, (745, 300))
    screen.blit(textBox, (0, 450))

    ownPokemonNameImg, rect = font.render(pglobals.ownPokemonName.upper(), (72, 72, 72))
    screen.blit(ownPokemonNameImg, (780, 330))

    oppPokemonNameImg, rect = font.render(pglobals.oppPokemonName.upper(), (72, 72, 72))
    screen.blit(oppPokemonNameImg, (5, 75))

    ownPokemonLvlImg, rect = font.render(str(pglobals.ownPokemonLvl), (72, 72, 72))
    screen.blit(ownPokemonLvlImg, (960, 330))

    oppPokemonLvlImg, rect = font.render(str(pglobals.oppPokemonLvl), (72, 72, 72))
    screen.blit(oppPokemonLvlImg, (170, 75))

    screen.blit(ownPokemonMaxHPImg, (940, 369))

    ownCurHPImg, rect = font.render(str(round(pglobals.ownPokemonStats[0])), (72, 72, 72))

    if pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP > 0.5:
        ownHPBar = pygame.transform.scale(maxImg, (math.floor((pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP)*96), 6))
    elif pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP > 0.3:
        ownHPBar = pygame.transform.scale(midImg, (math.floor((pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP)*96), 6))
    else:
        if pglobals.ownPokemonStats[0] > 0:
            ownHPBar = pygame.transform.scale(minImg, (math.ceil((pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP)*96), 6))
        else:
            ownHPBar = pygame.image.load("blank.png")

    if pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP > 0.5:
        oppHPBar = pygame.transform.scale(maxImg, (math.floor((pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP)*96), 6))
    elif pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP > 0.3:
        oppHPBar = pygame.transform.scale(midImg, (math.floor((pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP)*96), 6))
    else:
        if pglobals.oppPokemonStats[0] > 0:
            oppHPBar = pygame.transform.scale(minImg, (math.ceil((pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP)*96), 6))
        else:
            oppHPBar = pygame.image.load("blank.png")

    screen.blit(ownHPBar, (889, 354))
    screen.blit(oppHPBar, (100, 100))

    screen.blit(ownCurHPImg, (880, 369))

    if menuStage == 1:
        fightText, rect = fontLarge.render("FIGHT", (72, 72, 72))
        runText, rect = fontLarge.render("RUN", (215, 215, 215))
        bagText, rect = fontLarge.render("BAG", (215, 215, 215))
        pkmnText, rect = fontLarge.render("POKÉMON", (215, 215, 215))
        screen.blit(fightText, (160, 480))
        screen.blit(bagText, (160, 540))
        screen.blit(pkmnText, (600, 480))
        screen.blit(runText, (600, 540))
        
        screen.blit(pygame.transform.scale(selectCursor, (33, 34)), (120, 480))
        if mouseClickX > 156 and mouseClickX < 339 and mouseClickY > 476 and mouseClickY < 513:
            mouseClickX = 0
            mouseClickY = 0
            menuStage = 2
    elif menuStage == 2:
        move1Img, rect = fontLarge.render(pglobals.ownPokemonMoves[0].upper(), (72, 72, 72))
        move2Img, rect = fontLarge.render(pglobals.ownPokemonMoves[1].upper(), (72, 72, 72))
        move3Img, rect = fontLarge.render(pglobals.ownPokemonMoves[2].upper(), (72, 72, 72))
        move4Img, rect = fontLarge.render(pglobals.ownPokemonMoves[3].upper(), (72, 72, 72))

        screen.blit(move1Img, (80, 480))
        screen.blit(move2Img, (80, 540))
        screen.blit(move3Img, (520, 480))
        screen.blit(move4Img, (520, 540))
        if mouseClickX > 75 and mouseClickY > 473 and mouseClickX < 509 and mouseClickY < 514:
            chosenMoveIndex = 0
            mouseClickX = 0
            mouseClickY = 0
            menuStage = 3
        elif mouseClickX > 72 and mouseClickY > 534 and mouseClickX < 512 and mouseClickY < 573:
            chosenMoveIndex = 1
            mouseClickX = 0
            mouseClickY = 0
            menuStage = 3
        elif mouseClickX > 516 and mouseClickY > 473 and mouseClickX < 920 and mouseClickY < 514:
            chosenMoveIndex = 2
            mouseClickX = 0
            mouseClickY = 0
            menuStage = 3
        elif mouseClickX > 516 and mouseClickY > 535 and mouseClickX < 920 and mouseClickY < 579:
            chosenMoveIndex = 3
            mouseClickX = 0
            mouseClickY = 0
            menuStage = 3
        
            
    elif menuStage == 3:
        if pglobals.ownPokemonStats[5] > pglobals.oppPokemonStats[5]:
            responseImg, rect = fontMid.render(pglobals.ownPokemonName.upper() + " USES " + pglobals.ownPokemonMoves[chosenMoveIndex].upper() + "!", (72, 72, 72))
            screen.blit(responseImg, (80, 480))
            pglobals.oppPokemonStats[0] = pglobals.oppPokemonStats[0] - pokemonutil.calculateAttackDamage(movePowers[pglobals.ownPokemonMoves[chosenMoveIndex]], "own")

            if pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP > 0.5:
                oppHPBar = pygame.transform.scale(maxImg, (math.floor((pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP)*96), 6))
            elif pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP > 0.3:
                oppHPBar = pygame.transform.scale(midImg, (math.floor((pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP)*96), 6))
            else:
                if pglobals.oppPokemonStats[0] > 0:
                    oppHPBar = pygame.transform.scale(minImg, (math.ceil((pglobals.oppPokemonStats[0]/pglobals.oppPokemonMaxHP)*96), 6))
                else:
                    oppHPBar = pygame.image.load("blank.png")

            screen.blit(opponentHpBarImg, (0, 50))
            screen.blit(oppHPBar, (100, 100))
            screen.blit(oppPokemonNameImg, (5, 75))
            screen.blit(oppPokemonLvlImg, (170, 75))

            pygame.display.flip()
            time.sleep(1)

            if pglobals.oppPokemonStats[0] <= 0:
                pygame.mixer.music.load("victory.mp3")
                pygame.mixer.music.stop()
                pygame.mixer.music.play()
                screen.blit(textBox, (0, 450))
                screen.blit(oppPokemonLvlImg, (170, 75))
                exitMsgImg, rect = fontMid.render(pglobals.oppPokemonName.upper() + " FAINTED! " + pglobals.ownPokemonName.upper() + " WINS!", (72, 72, 72))
                screen.blit(exitMsgImg, (80, 480))
                pygame.display.flip()
                time.sleep(5)
                sys.exit()

            
            oppChosenMoveIndex = random.randint(0, 3)
            while pglobals.oppPokemonMoves[oppChosenMoveIndex] == "-":
                oppChosenMoveIndex = random.randint(0, 3)
            responseImg, rect = fontMid.render(pglobals.oppPokemonName.upper() + " USES " + pglobals.oppPokemonMoves[oppChosenMoveIndex].upper() + "!", (72, 72, 72))
            screen.blit(textBox, (0, 450))
            screen.blit(responseImg, (80, 480))
            pglobals.ownPokemonStats[0] = pglobals.ownPokemonStats[0] - pokemonutil.calculateAttackDamage(movePowers[pglobals.oppPokemonMoves[oppChosenMoveIndex]], "opponent")

            if pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP > 0.5:
                ownHPBar = pygame.transform.scale(maxImg, (math.floor((pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP)*96), 6))
            elif pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP > 0.3:
                ownHPBar = pygame.transform.scale(midImg, (math.floor((pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP)*96), 6))
            else:
                if pglobals.ownPokemonStats[0] > 0:
                    ownHPBar = pygame.transform.scale(minImg, (math.ceil((pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP)*96), 6))
                else:
                    ownHPBar = pygame.image.load("blank.png")
            
            
            if pglobals.ownPokemonStats[0] <= 0:
                ownCurHPImg, rect = font.render("0", (72, 72, 72))
            
            screen.blit(ownHpBarImg, (745, 300))
            screen.blit(ownHPBar, (889, 354))
            screen.blit(ownCurHPImg, (880, 369))
            screen.blit(ownPokemonMaxHPImg, (940, 369))
            screen.blit(ownPokemonNameImg, (780, 330))
            screen.blit(ownPokemonLvlImg, (960, 330))
            
            pygame.display.flip()
            time.sleep(1)
            if pglobals.ownPokemonStats[0] <= 0:
                pygame.mixer.music.stop()
                screen.blit(textBox, (0, 450))
                exitMsgImg, rect = fontMid.render(pglobals.ownPokemonName.upper() + " FAINTED! " + pglobals.oppPokemonName.upper() + " WINS!", (72, 72, 72))
                screen.blit(exitMsgImg, (80, 480))
                pygame.display.flip()
                time.sleep(5)
                sys.exit()
            
            menuStage = 1
            
        elif pglobals.oppPokemonStats[5] >= pglobals.ownPokemonStats[5]:
            oppChosenMoveIndex = random.randint(0, 3)
            while pglobals.oppPokemonMoves[oppChosenMoveIndex] == "-":
                oppChosenMoveIndex = random.randint(0, 3)
            responseImg, rect = fontMid.render(pglobals.oppPokemonName.upper() + " USES " + pglobals.oppPokemonMoves[oppChosenMoveIndex].upper() + "!", (72, 72, 72))
            screen.blit(responseImg, (80, 480))
            pglobals.ownPokemonStats[0] = pglobals.ownPokemonStats[0] - pokemonutil.calculateAttackDamage(movePowers[pglobals.oppPokemonMoves[oppChosenMoveIndex]], "opponent")

            if pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP > 0.5:
                ownHPBar = pygame.transform.scale(maxImg, (math.floor((pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP)*96), 6))
            elif pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP > 0.3:
                ownHPBar = pygame.transform.scale(midImg, (math.floor((pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP)*96), 6))
            else:
                if pglobals.ownPokemonStats[0] > 0:
                    ownHPBar = pygame.transform.scale(minImg, (math.ceil((pglobals.ownPokemonStats[0]/pglobals.ownPokemonMaxHP)*96), 6))
                else:
                    ownHPBar = pygame.image.load("blank.png")
            
            
            if pglobals.ownPokemonStats[0] <= 0:
                ownCurHPImg, rect = font.render("0", (72, 72, 72))
            
            screen.blit(ownHpBarImg, (745, 300))
            screen.blit(ownHPBar, (889, 354))
            screen.blit(ownCurHPImg, (880, 369))
            screen.blit(ownPokemonMaxHPImg, (940, 369))
            screen.blit(ownPokemonNameImg, (780, 330))
            screen.blit(ownPokemonLvlImg, (960, 330))
            
            pygame.display.flip()
            time.sleep(1)
            if pglobals.ownPokemonStats[0] <= 0:
                pygame.mixer.music.stop()
                screen.blit(textBox, (0, 450))
                exitMsgImg, rect = fontMid.render(pglobals.ownPokemonName.upper() + " FAINTED! " + pglobals.oppPokemonName.upper() + " WINS!", (72, 72, 72))
                screen.blit(exitMsgImg, (80, 480))
                pygame.display.flip()
                time.sleep(5)
                sys.exit()

            if pglobals.oppPokemonStats[0] <= 0:
                pygame.mixer.music.load("victory.mp3")
                pygame.mixer.music.stop()
                pygame.mixer.music.play()
                screen.blit(textBox, (0, 450))
                screen.blit(oppPokemonLvlImg, (170, 75))
                exitMsgImg, rect = fontMid.render(pglobals.oppPokemonName.upper() + " FAINTED! " + pglobals.ownPokemonName.upper() + " WINS!", (72, 72, 72))
                screen.blit(exitMsgImg, (80, 480))
                pygame.display.flip()
                time.sleep(5)
                sys.exit()
            
            responseImg, rect = fontMid.render(pglobals.ownPokemonName.upper() + " USES " + pglobals.ownPokemonMoves[chosenMoveIndex].upper() + "!", (72, 72, 72))
            screen.blit(textBox, (0, 450))
            screen.blit(responseImg, (80, 480))
            pygame.display.flip()
            time.sleep(1)
            pglobals.oppPokemonStats[0] = pglobals.oppPokemonStats[0] - pokemonutil.calculateAttackDamage(100, "own")
            time.sleep(1)

            menuStage = 1
    
    pygame.display.flip()
    time.sleep(1/1000)
