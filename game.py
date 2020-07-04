"""
Game.py contain the code in charge to execute the game
"""

# Import of libraries
import pygame
from script import MacGiver, Guardian, Delimiter, Item

# Game initialization
pygame.init()
pygame.time.Clock().tick(30) # Refresh every 30 milliseconds only
pygame.font.init()

# Create Framework object
velocity = 20
framework = pygame.image.load('ressource/structures.png')
delimiter = Delimiter(velocity)
limit = delimiter.limit
allowed = delimiter.allowed

# Create MacGiver object
startX = delimiter.start[0]
startY = delimiter.start[1]
macGyver = MacGiver(startX, startY, velocity)

# Create Guardian object
exitX = delimiter.exit[0]
exitY = delimiter.exit[1]
guardian = Guardian(exitX, exitY)

# Create Item object
items = Item(allowed, macGyver.width, macGyver.heigth)

# Window initialization
winWidth = 300
winHeigth = 160
win = pygame.display.set_mode((winWidth, winHeigth))
count = 0
pygame.display.set_caption("Aidez MacGyver ! {}/3".format(count))
win.blit(framework, (0, 0))
run = True

# Game execution
while run:
    pygame.time.delay(100)

    # Shifting management
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and macGyver.x > macGyver.velocity:
        macGyver.moveRight(limit)
    if keys[pygame.K_RIGHT] and macGyver.x < winWidth - macGyver.velocity - macGyver.width:
        macGyver.moveLeft(limit)
    if keys[pygame.K_UP] and macGyver.y > macGyver.velocity:
        macGyver.moveUp(limit)
    if keys[pygame.K_DOWN] and macGyver.y < winHeigth - macGyver.velocity - macGyver.heigth:
        macGyver.moveDown(limit)

    # Item management
    if (macGyver.x, macGyver.y) == items.needlePosition and items.pop['needle']==True:
        items.pop['needle'] = False
        count += 1
    if (macGyver.x, macGyver.y) == items.tubePosition and items.pop['tube']==True:
        items.pop['tube'] = False
        count += 1
    if (macGyver.x, macGyver.y) == items.etherPosition and items.pop['ether']==True:
        items.pop['ether'] = False
        count += 1

    # Displaying management
    pygame.display.set_caption("Aidez MacGyver ! {}/3".format(count))
    win.blit(framework, (0, 0))
    win.blit(macGyver.image, (macGyver.x, macGyver.y))
    win.blit(guardian.image, guardian.position)

    if items.pop['needle']:
        win.blit(items.needleImage, items.needlePosition)
    if items.pop['tube']:
        win.blit(items.tubeImage, items.tubePosition)
    if items.pop['ether']:
        win.blit(items.etherImage, items.etherPosition)

    # Game result management
    if (macGyver.x, macGyver.y) == guardian.position:
        font = pygame.font.SysFont('Comic Sans MS', 30)
        if True in items.pop.values():
            text = font.render(guardian.lose(), False, (255, 255, 255))
        else:
            text = font.render(guardian.win(), False, (255, 255, 255))
        win.blit(text, (0, 0))

    # Game execution management
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
