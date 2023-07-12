import pygame, pglobals, math
from random import uniform

def setPokemonData(selection, playerType):
    selection = selection.lower()
    if playerType == "own":
        if selection == "pikachu":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/pikachu_back.png")
            pglobals.ownPokemonName = "pikachu"
            pglobals.ownPokemonStats = [35, 55, 40, 50, 50, 90]
            pglobals.ownPokemonMoves = ["electro ball", "discharge", "thunderbolt", "thunder"]
        elif selection == "bulbasaur":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/bulbasaur_back.png")
            pglobals.ownPokemonName = "bulbasaur"
            pglobals.ownPokemonStats = [45, 49, 49, 65, 65, 45]
            pglobals.ownPokemonMoves = ["vine whip", "razor leaf", "-", "-"]
        elif selection == "ivysaur":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/ivysaur_back.png")
            pglobals.ownPokemonName = "ivysaur"
            pglobals.ownPokemonStats = [60, 62, 63, 80, 80, 60]
            pglobals.ownPokemonMoves = ["vine whip", "razor leaf", "solar beam", "-"]
        elif selection == "venusaur":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/venusaur_back.png")
            pglobals.ownPokemonName = "venusaur"
            pglobals.ownPokemonStats = [80, 82, 83, 100, 100, 80]
            pglobals.ownPokemonMoves = ["vine whip", "razor leaf", "solar beam", "double edge"]
        elif selection == "charmander":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/charmander_back.png")
            pglobals.ownPokemonName = "charmander"
            pglobals.ownPokemonStats = [39, 52, 43, 60, 50, 65]
            pglobals.ownPokemonMoves = ["scratch", "ember", "flamethrower", "-"]
        elif selection == "charmeleon":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/charmeleon_back.png")
            pglobals.ownPokemonName = "charmeleon"
            pglobals.ownPokemonStats = [58, 64, 58, 80, 65, 80]
            pglobals.ownPokemonMoves = ["ember", "fire spin", "slash", "flamethrower"]
        elif selection == "charizard":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/charizard_back.png")
            pglobals.ownPokemonName = "charizard"
            pglobals.ownPokemonStats = [78, 84, 78, 109, 85, 100]
            pglobals.ownPokemonMoves = ["crunch", "heat wave", "flamethrower", "flare blitz"]
        elif selection == "squirtle":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/squirtle_back.png")
            pglobals.ownPokemonName = "squirtle"
            pglobals.ownPokemonStats = [44, 48, 65, 50, 64, 43]
            pglobals.ownPokemonMoves = ["bubble", "water gun", "bite", "-"]
        elif selection == "wartortle":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/wartortle_back.png")
            pglobals.ownPokemonName = "wartortle"
            pglobals.ownPokemonStats = [59, 63, 80, 65, 80, 58]
            pglobals.ownPokemonMoves = ["bubble", "water gun", "bubble beam", "hydro pump"]
        elif selection == "blastoise":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/blastoise_back.png")
            pglobals.ownPokemonName = "blastoise"
            pglobals.ownPokemonStats = [79, 83, 100, 85, 105, 78]
            pglobals.ownPokemonMoves = ["aqua jet", "flash cannon", "hydro pump", "skull bash"]
        elif selection == "caterpie":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/caterpie_back.png")
            pglobals.ownPokemonName = "caterpie"
            pglobals.ownPokemonStats = [45, 30, 35, 20, 20, 45]
            pglobals.ownPokemonMoves = ["tackle", "-", "-", "-"]
        elif selection == "metapod":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/metapod_back.png")
            pglobals.ownPokemonName = "metapod"
            pglobals.ownPokemonStats = [50, 20, 55, 25, 25, 30]
            pglobals.ownPokemonMoves = ["harden", "harden", "harden", "harden"]
        elif selection == "butterfree":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/butterfree_back.png")
            pglobals.ownPokemonName = "butterfree"
            pglobals.ownPokemonStats = [60, 45, 50, 90, 80, 70]
            pglobals.ownPokemonMoves = ["gust", "confusion", "air slash", "bug buzz"]
        elif selection == "weedle":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/weedle_back.png")
            pglobals.ownPokemonName = "weedle"
            pglobals.ownPokemonStats = [40, 35, 30, 20, 20, 50]
            pglobals.ownPokemonMoves = ["poison sting", "bug bite", "-", "-"]
        elif selection == "kakuna":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/kakuna_back.png")
            pglobals.ownPokemonName = "kakuna"
            pglobals.ownPokemonStats = [45, 25, 50, 25, 25, 35]
            pglobals.ownPokemonMoves = ["harden", "harden", "harden", "harden"]
        elif selection == "beedrill":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/beedrill_back.png")
            pglobals.ownPokemonName = "beedrill"
            pglobals.ownPokemonStats = [65, 90, 40, 45, 80, 75]
            pglobals.ownPokemonMoves = ["twineedle", "poison jab", "pin missile", "outrage"]
        elif selection == "pidgey":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/pidgey_back.png")
            pglobals.ownPokemonName = "pidgey"
            pglobals.ownPokemonStats = [40, 45, 40, 35, 35, 56]
            pglobals.ownPokemonMoves = ["tackle", "gust", "air slash", "-"]
        elif selection == "pidgeotto":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/pidgeotto_back.png")
            pglobals.ownPokemonName = "pidgeotto"
            pglobals.ownPokemonStats = [63, 60, 55, 50, 50, 71]
            pglobals.ownPokemonMoves = ["twister", "wing attack", "air slash", "hurricane"]
        elif selection == "pidgeot":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/pidgeot_back.png")
            pglobals.ownPokemonName = "pidgeot"
            pglobals.ownPokemonStats = [83, 80, 75, 70, 70, 101]
            pglobals.ownPokemonMoves = ["twister", "wing attack", "air slash", "hurricane"]
        elif selection == "rattata":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/rattata_back.png")
            pglobals.ownPokemonName = "rattata"
            pglobals.ownPokemonStats = [30, 56, 35, 25, 35, 72]
            pglobals.ownPokemonMoves = ["tackle", "pursuit", "bite", "-"]
        elif selection == "raticate":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/raticate_back.png")
            pglobals.ownPokemonName = "raticate"
            pglobals.ownPokemonStats = [55, 81, 60, 50, 70, 97]
            pglobals.ownPokemonMoves = ["bite", "sucker punch", "crunch", "double edge"]
        elif selection == "spearow":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/spearow_back.png")
            pglobals.ownPokemonName = "spearow"
            pglobals.ownPokemonStats = [40, 60, 30, 31, 31, 70]
            pglobals.ownPokemonMoves = ["peck", "pursuit", "aerial ace", "-"]
        elif selection == "fearow":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/fearow_back.png")
            pglobals.ownPokemonName = "fearow"
            pglobals.ownPokemonStats = [65, 90, 65, 61, 61, 100]
            pglobals.ownPokemonMoves = ["aerial ace", "assurance", "drill run", "drill peck"]
        elif selection == "ekans":
            pglobals.ownPokemonImg = pygame.image.load("pokemon/ekans_back.png")
            pglobals.ownPokemonName = "ekans"
            pglobals.ownPokemonStats = [35, 60, 44, 40, 54, 55]
            pglobals.ownPokemonMoves = ["wrap", "poison sting", "acid", "gunk shot"]
        else:
            pglobals.ownPokemonImg = pygame.image.load("missingTex.png")
            print("That's either not a Pokémon, or I haven't bothered to code it in yet.")



    elif playerType == "opponent":
        if selection == "pikachu":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/pikachu.png")
            pglobals.oppPokemonName = "pikachu"
            pglobals.ownPokemonStats = [35, 55, 40, 50, 50, 90]
            pglobals.oppPokemonMoves = ["electro ball", "discharge", "thunderbolt", "thunder"]
        elif selection == "bulbasaur":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/bulbasaur.png")
            pglobals.oppPokemonName = "bulbasaur"
            pglobals.oppPokemonStats = [45, 49, 49, 65, 65, 45]
            pglobals.oppPokemonMoves = ["vine whip", "razor leaf", "-", "-"]
        elif selection == "ivysaur":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/ivysaur.png")
            pglobals.oppPokemonName = "ivysaur"
            pglobals.oppPokemonStats = [60, 62, 63, 80, 80, 60]
            pglobals.oppPokemonMoves = ["vine whip", "razor leaf", "solar beam", "-"]
        elif selection == "venusaur":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/venusaur.png")
            pglobals.oppPokemonName = "venusaur"
            pglobals.oppPokemonStats = [80, 82, 83, 100, 100, 80]
            pglobals.oppPokemonMoves = ["vine whip", "razor leaf", "solar beam", "double edge"]
        elif selection == "charmander":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/charmander.png")
            pglobals.oppPokemonName = "charmander"
            pglobals.oppPokemonStats = [39, 52, 43, 60, 50, 65]
            pglobals.oppPokemonMoves = ["scratch", "ember", "flamethrower", "-"]
        elif selection == "charmeleon":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/charmeleon.png")
            pglobals.oppPokemonName = "charmeleon"
            pglobals.oppPokemonStats = [58, 64, 58, 80, 65, 80]
            pglobals.oppPokemonMoves = ["ember", "fire spin", "slash", "flamethrower"]
        elif selection == "charizard":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/charizard.png")
            pglobals.oppPokemonName = "charizard"
            pglobals.oppPokemonStats = [78, 84, 78, 109, 85, 100]
            pglobals.oppPokemonMoves = ["crunch", "heat wave", "flamethrower", "flare blitz"]
        elif selection == "squirtle":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/squirtle.png")
            pglobals.oppPokemonName = "squirtle"
            pglobals.oppPokemonStats = [44, 48, 65, 50, 64, 43]
            pglobals.oppPokemonMoves = ["bubble", "water gun", "bite", "-"]
        elif selection == "wartortle":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/wartortle.png")
            pglobals.oppPokemonName = "wartortle"
            pglobals.oppPokemonStats = [59, 63, 80, 65, 80, 58]
            pglobals.oppPokemonMoves = ["bubble", "water gun", "bubble beam", "hydro pump"]
        elif selection == "blastoise":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/blastoise.png")
            pglobals.oppPokemonName = "blastoise"
            pglobals.oppPokemonStats = [79, 83, 100, 85, 105, 78]
            pglobals.oppPokemonMoves = ["aqua jet", "flash cannon", "hydro pump", "skull bash"]
        elif selection == "caterpie":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/caterpie.png")
            pglobals.oppPokemonName = "caterpie"
            pglobals.oppPokemonStats = [45, 30, 35, 20, 20, 45]
            pglobals.oppPokemonMoves = ["tackle", "-", "-", "-"]
        elif selection == "metapod":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/metapod.png")
            pglobals.oppPokemonName = "metapod"
            pglobals.oppPokemonStats = [50, 20, 55, 25, 25, 30]
            pglobals.oppPokemonMoves = ["harden", "harden", "harden", "harden"]
        elif selection == "butterfree":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/butterfree.png")
            pglobals.oppPokemonName = "butterfree"
            pglobals.oppPokemonStats = [60, 45, 50, 90, 80, 70]
            pglobals.oppPokemonMoves = ["gust", "confusion", "air slash", "bug buzz"]
        elif selection == "weedle":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/weedle.png")
            pglobals.oppPokemonName = "weedle"
            pglobals.oppPokemonStats = [40, 35, 30, 20, 20, 50]
            pglobals.oppPokemonMoves = ["poison sting", "bug bite", "-", "-"]
        elif selection == "kakuna":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/kakuna.png")
            pglobals.oppPokemonName = "kakuna"
            pglobals.oppPokemonStats = [45, 25, 50, 25, 25, 35]
            pglobals.oppPokemonMoves = ["harden", "harden", "harden", "harden"]
        elif selection == "beedrill":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/beedrill.png")
            pglobals.oppPokemonName = "beedrill"
            pglobals.oppPokemonStats = [65, 90, 40, 45, 80, 75]
            pglobals.oppPokemonMoves = ["twineedle", "poison jab", "pin missile", "outrage"]
        elif selection == "pidgey":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/pidgey.png")
            pglobals.oppPokemonName = "pidgey"
            pglobals.oppPokemonStats = [40, 45, 40, 35, 35, 56]
            pglobals.oppPokemonMoves = ["tackle", "gust", "air slash", "-"]
        elif selection == "pidgeotto":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/pidgeotto.png")
            pglobals.oppPokemonName = "pidgeotto"
            pglobals.oppPokemonStats = [63, 60, 55, 50, 50, 71]
            pglobals.oppPokemonMoves = ["twister", "wing attack", "air slash", "hurricane"]
        elif selection == "pidgeot":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/pidgeot.png")
            pglobals.oppPokemonName = "pidgeot"
            pglobals.oppPokemonStats = [83, 80, 75, 70, 70, 101]
            pglobals.oppPokemonMoves = ["twister", "wing attack", "air slash", "hurricane"]
        elif selection == "rattata":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/rattata.png")
            pglobals.oppPokemonName = "rattata"
            pglobals.oppPokemonStats = [30, 56, 35, 25, 35, 72]
            pglobals.oppPokemonMoves = ["tackle", "pursuit", "bite", "-"]
        elif selection == "raticate":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/raticate.png")
            pglobals.oppPokemonName = "raticate"
            pglobals.oppPokemonStats = [55, 81, 60, 50, 70, 97]
            pglobals.oppPokemonMoves = ["bite", "sucker punch", "crunch", "double edge"]
        elif selection == "spearow":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/spearow.png")
            pglobals.oppPokemonName = "spearow"
            pglobals.oppPokemonStats = [40, 60, 30, 31, 31, 70]
            pglobals.oppPokemonMoves = ["peck", "pursuit", "aerial ace", "-"]
        elif selection == "fearow":
            pglobals.oppPokemonImg = pygame.image.load("pokemon/fearow.png")
            pglobals.oppPokemonName = "fearow"
            pglobals.oppPokemonStats = [65, 90, 65, 61, 61, 100]
            pglobals.oppPokemonMoves = ["aerial ace", "assurance", "drill run", "drill peck"]
        
        else:
            pglobals.oppPokemonImg = pygame.image.load("missingTex.png")
            print("That's either not a Pokémon, or I haven't bothered to code it in yet.")

def setPokemonLevel(level, playerType):
    if level != "amazingPassword":
        try:
            level = int(level)
        except:
            print("That's not a number!")
            return
        if level > 100:
            print("That's more than 100!")
            return
        elif level < 1:
            print("That's less than 1!")
            return
        if playerType == "own":
            pglobals.ownPokemonLvl = level
        elif playerType == "opponent":
            pglobals.oppPokemonLvl = level
        else:
            print("Invalid player type")
    else:
        try:
            level = int(input())
        except:
            print("That's not a number!")
            return
        if playerType == "own":
            pglobals.ownPokemonLvl = level
        elif playerType == "opponent":
            pglobals.oppPokemonLvl = level
        else:
            print("Invalid player type")
        
def calculatePokemonStats(player):
    if player == "own":
        hp_ = (math.floor((2*pglobals.ownPokemonStats[0]+pglobals.ownPokemonIVs[0]+(pglobals.ownPokemonEVs[0]/4)*pglobals.ownPokemonLvl)/100)+pglobals.ownPokemonLvl+10)
        atk_ = math.floor(math.floor((2*pglobals.ownPokemonStats[1]+pglobals.ownPokemonIVs[1]+(pglobals.ownPokemonEVs[1]/4)*pglobals.ownPokemonLvl)/100)+5)
        def_ = math.floor(math.floor((2*pglobals.ownPokemonStats[2]+pglobals.ownPokemonIVs[2]+(pglobals.ownPokemonEVs[2]/4)*pglobals.ownPokemonLvl)/100)+5)
        spatk_ = math.floor(math.floor((2*pglobals.ownPokemonStats[3]+pglobals.ownPokemonIVs[3]+(pglobals.ownPokemonEVs[3]/4)*pglobals.ownPokemonLvl)/100)+5)
        spdef_ = math.floor(math.floor((2*pglobals.ownPokemonStats[4]+pglobals.ownPokemonIVs[4]+(pglobals.ownPokemonEVs[4]/4)*pglobals.ownPokemonLvl)/100)+5)
        speed_ = math.floor(math.floor((2*pglobals.ownPokemonStats[5]+pglobals.ownPokemonIVs[5]+(pglobals.ownPokemonEVs[5]/4)*pglobals.ownPokemonLvl)/100)+5)
        pglobals.ownPokemonStats[0] = hp_
        pglobals.ownPokemonStats[1] = atk_
        pglobals.ownPokemonStats[2] = def_
        pglobals.ownPokemonStats[3] = spatk_
        pglobals.ownPokemonStats[4] = spdef_
        pglobals.ownPokemonStats[5] = speed_
        pglobals.ownPokemonMaxHP = hp_
    elif player == "opponent":
        hp_ = (math.floor((2*pglobals.oppPokemonStats[0]+pglobals.oppPokemonIVs[0]+(pglobals.oppPokemonEVs[0]/4)*pglobals.oppPokemonLvl)/100)+pglobals.oppPokemonLvl+10)
        atk_ = math.floor(math.floor((2*pglobals.oppPokemonStats[1]+pglobals.oppPokemonIVs[1]+(pglobals.ownPokemonEVs[1]/4)*pglobals.ownPokemonLvl)/100)+5)
        def_ = math.floor(math.floor((2*pglobals.oppPokemonStats[2]+pglobals.oppPokemonIVs[2]+(pglobals.ownPokemonEVs[2]/4)*pglobals.ownPokemonLvl)/100)+5)
        spatk_ = math.floor(math.floor((2*pglobals.oppPokemonStats[3]+pglobals.oppPokemonIVs[3]+(pglobals.ownPokemonEVs[3]/4)*pglobals.ownPokemonLvl)/100)+5)
        spdef_ = math.floor(math.floor((2*pglobals.oppPokemonStats[4]+pglobals.oppPokemonIVs[4]+(pglobals.ownPokemonEVs[4]/4)*pglobals.ownPokemonLvl)/100)+5)
        speed_ = math.floor(math.floor((2*pglobals.oppPokemonStats[5]+pglobals.oppPokemonIVs[5]+(pglobals.ownPokemonEVs[5]/4)*pglobals.ownPokemonLvl)/100)+5)
        pglobals.oppPokemonStats[0] = hp_
        pglobals.oppPokemonStats[1] = atk_
        pglobals.oppPokemonStats[2] = def_
        pglobals.oppPokemonStats[3] = spatk_
        pglobals.oppPokemonStats[4] = spdef_
        pglobals.oppPokemonStats[5] = speed_
        pglobals.oppPokemonMaxHP = hp_

def calculateAttackDamage(power, playerType):
    if playerType == "own":
        x = (math.floor((((((2*pglobals.ownPokemonLvl)/5)+2)*power*pglobals.ownPokemonStats[1]/pglobals.oppPokemonStats[2])/50)+2))
    elif playerType == "opponent":
        x = (math.floor((((((2*pglobals.oppPokemonLvl)/5)+2)*power*pglobals.oppPokemonStats[1]/pglobals.ownPokemonStats[2])/50)+2))
    return x
