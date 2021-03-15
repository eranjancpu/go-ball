import math
from pygame import mixer
import pygame

pygame.init()

screen = pygame.display.set_mode((900, 900))

pygame.display.set_caption("go ball 2.0")

ball = pygame.image.load('d.png')
saw = pygame.image.load('saw.png')
saw1 = pygame.image.load('saw1.png')
saw2 = pygame.image.load('saw2.png')
hole = pygame.image.load('hole.png')
bg = pygame.image.load('cave.png')
mixer.music.load('pop.wav')


pygame.display.set_icon(ball)

ball = pygame.transform.scale(ball, (100, 100))
saw = pygame.transform.scale(saw, (100, 100))
saw1 = pygame.transform.scale(saw1, (100, 100))
saw2 = pygame.transform.scale(saw2, (100, 100))
hole = pygame.transform.scale(hole, (100, 100))
font = pygame.font.Font('freesansbold.ttf', 50)


# noinspection PyUnreachableCode
def isPop(sawx, sawy, saw1x, saw1y, saw2x, saw2y, ballx, bally, ):
    distance = math.sqrt(math.pow(sawx - ballx, 2) + (math.pow(sawy - bally, 2)))
    distance1 = math.sqrt(math.pow(saw1x - ballx, 2) + (math.pow(saw1y - bally, 2)))
    distance2 = math.sqrt(math.pow(saw2x - ballx, 2) + (math.pow(saw2y - bally, 2)))
    if distance < 50 or distance1 < 50 or distance2 < 50:
        return True
    else:
        return False


def isPopT(sawx, sawy, saw1x, saw1y, saw2x, saw2y, ballx, bally, ):
    distance = math.sqrt(math.pow(sawx - ballx, 2) + (math.pow(sawy - bally, 2)))
    distance1 = math.sqrt(math.pow(saw1x - ballx, 2) + (math.pow(saw1y - bally, 2)))
    distance2 = math.sqrt(math.pow(saw2x - ballx, 2) + (math.pow(saw2y - bally, 2)))
    if distance < 50 or distance1 < 50 or distance2 < 50:
        return True
    else:
        return False


def isWin(ballx, bally, holex, holey):
    distance = math.sqrt(math.pow(holex - ballx, 2) + (math.pow(holey - bally, 2)))
    if distance < 50:
        return True
    else:
        return False


level = 1

levelTextX = 0
levelTextY = 0


def show_win(x, y):
    you_win = font.render("YOU WIN!!!", True, (20, 255, 0))
    screen.blit(you_win, (x, y))


def show_level(x, y):
    levelText = font.render("level = " + str(level), True, (0, 20, 255))
    screen.blit(levelText, (x, y))


def holeDisplay(x, y):
    screen.blit(hole, (x, y))


def ballDisplay(x, y):
    screen.blit(ball, (x, y))


def sawDisplay(x, y):
    screen.blit(saw, (x, y))


def saw1Display(x, y):
    screen.blit(saw1, (x, y))


def saw2Display(x, y):
    screen.blit(saw2, (x, y))


textX = 600
textY = 600

holeX = 800
holeY = 0

sawX = 0
sawY = 600
sawChange = 6

saw1X = 800
saw1Y = 400
saw1Change = -6

saw2X = 0
saw2Y = 200
saw2Change = 6

ballX = 0
ballY = 800

ballXChange = 0
ballYChange = 0

running1 = True
while running1:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running1 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ballXChange = 1
            if event.key == pygame.K_LEFT:
                ballXChange = -1
            if event.key == pygame.K_UP:
                ballYChange = -1
            if event.key == pygame.K_DOWN:
                ballYChange = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ballXChange = 0
            if event.key == pygame.K_LEFT:
                ballXChange = 0
            if event.key == pygame.K_UP:
                ballYChange = 0
            if event.key == pygame.K_DOWN:
                ballYChange = 0
    if level == 1:
        sawX += sawChange
        saw1X += saw1Change
        saw2X += saw2Change
        ballX += ballXChange
        ballY += ballYChange
        ballDisplay(ballX, ballY)
        sawDisplay(sawX, sawY)
        show_level(levelTextX, levelTextY)
        saw1Display(saw1X, saw1Y)
        saw2Display(saw2X, saw2Y)
        holeDisplay(holeX, holeY)
        if sawX <= 0:
            sawChange = sawChange + 2
        elif sawX >= 800:
            sawChange = sawChange - 2
        if saw1X <= int(0):
            saw1Change = 6
        elif saw1X >= int(800):
            saw1Change = -6
        if saw2X <= int(0):
            saw2Change = 6
        elif saw2X >= int(800):
            saw2Change = -6

        if ballX <= 0:
            ballX = 0
        if ballX >= 800:
            ballX = 800
        if ballY <= 0:
            ballY = 0
        if ballY >= 800:
            ballY = 800
        pop = isPop(sawX, sawY, saw1X, saw1Y, saw2X, saw2Y, ballX, ballY)
        win = isWin(ballX, ballY, holeX, holeY)
        if pop:
            ballX = 0
            ballY = 800
            mixer.music.play(1)

        if win:
            show_win(textX, textY)
            vic = mixer.Sound('vic.wav')
            vic.play(1)
            level = level + 1
    if level == 2:
        sawX += sawChange
        saw1X += saw1Change
        saw2X += saw2Change
        ballX += ballXChange
        ballY += ballYChange
        ballDisplay(ballX, ballY)
        sawDisplay(sawX, sawY)
        show_level(levelTextX, levelTextY)
        saw1Display(saw1X, saw1Y)
        saw2Display(saw2X, saw2Y)
        holeDisplay(0, 800)
        if sawX <= 0:
            sawChange = sawChange + 2
        elif sawX >= 800:
            sawChange = sawChange - 2
        if saw1X <= int(0):
            saw1Change = 6
        elif saw1X >= int(800):
            saw1Change = -6
        if saw2X <= int(0):
            saw2Change = 6
        elif saw2X >= int(800):
            saw2Change = -6

        if ballX <= 0:
            ballX = 0
        if ballX >= 800:
            ballX = 800
        if ballY <= 0:
            ballY = 0
        if ballY >= 800:
            ballY = 800
        popT = isPopT(sawX, sawY, saw1X, saw1Y, saw2X, saw2Y, ballX, ballY)
        win = isWin(ballX, ballY, 0, 800)
        if popT:
            ballX = 800
            ballY = 0
        if win:
            show_win(textX, textY)
            vic = mixer.Sound('vic.wav')
            vic.play(1)

    pygame.display.update()
