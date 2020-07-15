"""
script.py contain the classes of MacGiver, Guardian, Delimiter and Item object
"""

import pygame
import random


class MacGiver:
    """Give birth to Mac Giver"""
    def __init__(self, x, y, speed):
        self.image = pygame.image.load('ressource/MacGyver.png')
        self.width = 16
        self.heigth = 16
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.x = x
        self.y = y
        self.speed = speed

    def moveRight(self, limit):
        # Make a move to the right
        if (self.x - self.speed, self.y) not in limit:
            self.x -= self.speed
            return self.x

    def moveLeft(self, limit):
        # Make a move to the left
        if (self.x + self.speed, self.y) not in limit:
            self.x += self.speed
            return self.x

    def moveUp(self, limit):
        # Make a move to the top
        if (self.x, self.y - self.speed) not in limit:
            self.y -= self.speed
            return self.y

    def moveDown(self, limit):
        # Make a move to the bottom
        if (self.x, self.y + self.speed) not in limit:
            self.y += self.speed
            return self.y


class Guardian:
    """Guardian Interaction"""

    def __init__(self, x, y):
        self.image = pygame.image.load('ressource/Gardien.png')
        self.width = 16
        self.heigth = 16
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.position = (x, y)

    def win(self):
        # Return the message when the player win the game
        return 'You win !'

    def lose(self):
        # Return the message when the player lose the game
        return 'You lose !'


class Delimiter:
    """Delimit the level. Return the allowed and forbidden emplacements."""
    def __init__(self, speed):

        self.limit = []
        self.allowed = []

        with open('framework.txt', 'r') as file:
            for y, line in enumerate(file):

                # Y emplacement computation
                if y == 0:
                    y += 1
                else:
                    y = y * speed + 1

                for x, value in enumerate(line[:-1]):

                    # X emplacement computation
                    if x == 0:
                        x += 1
                    else:
                        x = x * speed + 1

                    # Get the forbidden and allowed emplacements
                    if value == 's':
                        self.start = (x, y)
                    elif value == 'e':
                        self.exit = (x, y)
                    elif value == 'w' and (x, y):
                        self.limit.append((x, y))
                    elif value != 'w' and (x, y):
                        self.allowed.append((x, y))


class Item:
    """Manage the Items population"""
    def __init__(self, allowed, width, heigth):

        # Needle generation
        self.needleImage = pygame.image.load('ressource/aiguille.png')
        self.needleImage = pygame.transform.scale(self.needleImage, (16, 16))
        self.needlePosition = random.choice(allowed)
        allowed.remove(self.needlePosition)

        # Tube generation
        self.tubeImage = pygame.image.load('ressource/tube_plastique.png')
        self.tubeImage = pygame.transform.scale(self.tubeImage, (16, 16))
        self.tubePosition = random.choice(allowed)
        allowed.remove(self.tubePosition)

        # Ether generation
        self.etherImage = pygame.image.load('ressource/ether.png')
        self.etherImage = pygame.transform.scale(self.etherImage, (16, 16))
        self.etherPosition = random.choice(allowed)
        allowed.remove(self.etherPosition)

        # Population rights
        self.pop = {'needle': True, 'tube': True, 'ether': True}
