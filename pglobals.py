import pygame
import random

def initialise():
    global ownPokemonName
    ownPokemonName = None
    global oppPokemonName
    oppPokemonName = None

    global ownPokemonStats
    ownPokemonStats = [1, 0, 0, 0, 0, 0]
    global oppPokemonStats
    oppPokemonStats = [1, 0, 0, 0, 0, 0]

    global ownPokemonMaxHP
    ownPokemonMaxHP = 1
    global oppPokemonMaxHP
    oppPokemonMaxHP = 1

    global ownPokemonImg
    ownPokemonImg = pygame.image.load("missingTex.png")
    global oppPokemonImg
    oppPokemonImg = pygame.image.load("missingTex.png")

    global ownPokemonLvl
    ownPokemonLvl = None
    global oppPokemonLvl
    oppPokemonLvl = None

    global ownPokemonIVs
    ownPokemonIVs = [random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30)]
    global oppPokemonIVs
    oppPokemonIVs = [random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30)]

    global ownPokemonEVs
    ownPokemonEVs = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    global oppPokemonEVs
    oppPokemonEVs = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

    global ownPokemonMoves
    ownPokemonMoves = ["PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER"]
    global oppPokemonMoves
    oppPokemonMoves = ["PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER"]
