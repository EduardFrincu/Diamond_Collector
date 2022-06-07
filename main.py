import pygame
import sys
import random
from player import Miner
from gem import Gem
from bomb import Bomb
from Heart import Heart

WIDTH = 1200
HEIGHT = 800

gemsNumber = 2
gemWidth = 50
gemHeight = 50

adder = True

bombsNumber = gemsNumber - 1
bombWidth = gemWidth
bombHeight = gemHeight

minerHeight, minerWidth = 120, 120

characterOption = 'Images/miner1.png'  # default option

# Initialization
pygame.init()

# window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Diamond Collector')
window_icon = pygame.image.load('Images/window_icon.png')
pygame.display.set_icon(window_icon)

font = pygame.font.SysFont('goudystout', 40)

# Sounds

gemCatchedSound = pygame.mixer.Sound('Sounds/mixkit-game-ball-tap-2073.wav')
bombCatchedSound = pygame.mixer.Sound('Sounds/mixkit-player-jumping-in-a-video-game-2043.wav')
pygame.mixer.music.load('Sounds/Child\'s Nightmare.ogg')
buttonPressedSound = pygame.mixer.Sound('Sounds/button_select.mp3')
pygame.mixer.music.set_volume(0.07)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def button(surface, position, text, fontSize):
    font = pygame.font.SysFont('goudystout', fontSize)
    text_render = font.render(text, True, (255, 255, 255))
    x, y, w, h = position
    pygame.draw.line(surface, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(surface, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(surface, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(surface, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(surface, (100, 100, 100), (x, y, w, h))

    return surface.blit(text_render, (x, y))


def options():
    global characterOption
    characterOption = 'Images/miner1.png'

    background = pygame.image.load('Images/wall1.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))

    check = pygame.image.load('Images/check.png')
    check = pygame.transform.scale(check, (50,50)).convert_alpha()

    miner1 = pygame.image.load('Images/miner1.png')
    miner2 = pygame.image.load('Images/miner2.png')
    miner3 = pygame.image.load('Images/miner3.png')

    miner_height, miner_width = 150, 150
    miner1 = pygame.transform.scale(miner1, (miner_height, miner_width)).convert_alpha()
    miner2 = pygame.transform.scale(miner2, (miner_height, miner_width)).convert_alpha()
    miner3 = pygame.transform.scale(miner3, (miner_height, miner_width)).convert_alpha()

    miner1Button = miner1.get_rect()
    miner2Button = miner1.get_rect()
    miner3Button = miner1.get_rect()

    miner1Button.topleft = ((WIDTH - miner_width) / 2, (HEIGHT - miner_height) / 2)
    miner2Button.topleft = ((WIDTH - miner_width) / 2 - 200, (HEIGHT - miner_height) / 2)
    miner3Button.topleft = ((WIDTH - miner_width) / 2 + 200, (HEIGHT - miner_height) / 2)

    screen.blit(miner1, ((WIDTH - miner_width) / 2, (HEIGHT - miner_height) / 2))
    screen.blit(miner2, ((WIDTH - miner_width) / 2 - 200, (HEIGHT - miner_height) / 2))
    screen.blit(miner3, ((WIDTH - miner_width) / 2 + 200, (HEIGHT - miner_height) / 2))

    draw_text('Options', font, (255, 255, 255), screen, 20, 20)

    running = True
    while running:

        pygame.mouse.set_visible(True)
        mx, my = pygame.mouse.get_pos()


        if characterOption == 'Images/miner1.png':
            screen.blit(background, (0, 0))
            draw_text('Options', font, (255, 255, 255), screen, 20, 20)
            screen.blit(miner1, ((WIDTH - miner_width) / 2, (HEIGHT - miner_height) / 2))
            screen.blit(miner2, ((WIDTH - miner_width) / 2 - 200, (HEIGHT - miner_height) / 2))
            screen.blit(miner3, ((WIDTH - miner_width) / 2 + 200, (HEIGHT - miner_height) / 2))
            screen.blit(check, ((WIDTH - miner_width/2) / 2, (HEIGHT - miner_height) / 2 + 150))

        if characterOption == 'Images/miner2.png':
            screen.blit(background, (0, 0))
            draw_text('Options', font, (255, 255, 255), screen, 20, 20)
            screen.blit(miner1, ((WIDTH - miner_width) / 2, (HEIGHT - miner_height) / 2))
            screen.blit(miner2, ((WIDTH - miner_width) / 2 - 200, (HEIGHT - miner_height) / 2))
            screen.blit(miner3, ((WIDTH - miner_width) / 2 + 200, (HEIGHT - miner_height) / 2))
            screen.blit(check, ((WIDTH - miner_width/2) / 2 - 200, (HEIGHT - miner_height) / 2 + 150))

        if characterOption == 'Images/miner3.png':
            screen.blit(background, (0, 0))
            draw_text('Options', font, (255, 255, 255), screen, 20, 20)
            screen.blit(miner1, ((WIDTH - miner_width) / 2, (HEIGHT - miner_height) / 2))
            screen.blit(miner2, ((WIDTH - miner_width) / 2 - 200, (HEIGHT - miner_height) / 2))
            screen.blit(miner3, ((WIDTH - miner_width) / 2 + 200, (HEIGHT - miner_height) / 2))
            screen.blit(check, ((WIDTH - miner_width / 2) / 2 + 200, (HEIGHT - miner_height) / 2 + 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if miner1Button.collidepoint((mx, my)):
                    characterOption = 'Images/miner1.png'
                    buttonPressedSound.play()
                if miner2Button.collidepoint((mx, my)):
                    characterOption = 'Images/miner2.png'
                    buttonPressedSound.play()
                if miner3Button.collidepoint((mx, my)):
                    characterOption = 'Images/miner3.png'
                    buttonPressedSound.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()



def main_menu():
    while True:

        screen.fill((0, 200, 0))

        background = pygame.image.load('Images/wall1.png')
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        screen.blit(background, (0, 0))

        draw_text('Diamond Collector', font, (255, 255, 255), screen, WIDTH / 2 - 40 * 9, 20)
        pygame.mouse.set_visible(True)

        mx, my = pygame.mouse.get_pos()

        buttonWidth = 200
        buttonHeight = 50

        playButton = button(screen,
                            ((WIDTH - buttonWidth) / 2, (HEIGHT - buttonHeight) / 2, buttonWidth, buttonHeight),
                            "Play", buttonHeight - 10)
        optionsButton = button(screen, (
            (WIDTH - buttonWidth) / 2 - 63, (HEIGHT - buttonHeight) / 2 + 100, buttonWidth + 126, buttonHeight),
                            "Options",
                            buttonHeight - 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.collidepoint((mx, my)):
                    buttonPressedSound.play()
                    Game()
                if optionsButton.collidepoint((mx, my)):
                    buttonPressedSound.play()
                    options()

        pygame.display.update()


def Game():
    global gemsNumber
    global bombsNumber
    global adder

    background = pygame.image.load('Images/cave2.webp')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT)).convert_alpha()

    pygame.mixer.music.play(-1)
    scoreFont = pygame.font.SysFont('Arial', 30)

    score = 0
    lives = 3
    clock = pygame.time.Clock()

    player = Miner(characterOption, WIDTH / 2, HEIGHT - minerHeight / 2, minerWidth, minerHeight)
    miner = pygame.sprite.Group()
    miner.add(player)

    bonusLife = pygame.sprite.Group()
    gems = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    adder = True

    # add 'gemsNumber' gems in gems

    for _ in range(bombsNumber):
        bombs.add(Bomb('Images/bomb.png', bombHeight, bombWidth))

    for _ in range(gemsNumber):
        gems.add(Gem('Images/gem.png', gemHeight, gemWidth))

    # game loop

    running = True
    while running:

        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gemsNumber = 2
                    bombsNumber = 1
                    pygame.mixer.music.stop()
                    running = False

        for gem in gems:
            if pygame.sprite.collide_rect(gem, player):
                gem.rect.y = random.randrange(-80, -35)
                gem.rect.x = random.randrange(gemWidth, WIDTH - gemWidth)
                gem.speed = random.randrange(1, 6)
                gemCatchedSound.play()
                score += 1
                adder = True

        for bomb in bombs:
            if pygame.sprite.collide_rect(bomb, player):
                bomb.rect.y = random.randrange(-120, -90)
                bomb.rect.x = random.randrange(bombWidth, WIDTH - bombWidth)
                bomb.speed = random.randrange(1, 6)
                bombCatchedSound.play()
                lives -= 1

                if lives == 0:
                    pygame.mixer.music.stop()
                    gemsNumber = 2
                    bombsNumber = 1
                    game_over()
                    running = False

                adder = True
        for life in bonusLife:
            if pygame.sprite.collide_rect(life, player):
                life.rect.y = random.randrange(-80, -35)
                life.rect.x = random.randrange(gemWidth, WIDTH - gemWidth)
                gemCatchedSound.play()
                lives += 1
                bonusLife.empty()
                adder = True
            if life.rect.y > HEIGHT - 80 and pygame.sprite.collide_rect(life, player) == False:
                life.rect.y = random.randrange(-80, -35)
                life.rect.x = random.randrange(gemWidth, WIDTH - gemWidth)
                bonusLife.empty()
                adder = True

        if score > 1 and score % 10 == 0 and adder:
            gems.add(Gem('Images/gem.png', gemHeight, gemWidth))
            gemsNumber += 1

            if score % 20 == 0 and adder:
                bombs.add(Bomb('Images/bomb.png', bombHeight, bombWidth))
                bombsNumber += 1

            if score > 1 and score % 30 == 0 and adder:
                bonusLife.add(Heart('Images/like.png', gemHeight, gemWidth))
            adder = False

        miner.update()
        gems.update()
        bombs.update()
        bonusLife.update()
        miner.draw(screen)
        gems.draw(screen)
        bombs.draw(screen)
        bonusLife.draw(screen)
        draw_text("Score: " + str(score), scoreFont, (255, 255, 255), screen, WIDTH - 120, 20)
        draw_text('Lives: ' + str(lives), scoreFont, (255, 255, 255), screen, WIDTH - 120, 50)
        pygame.display.update()
        clock.tick(120)


def game_over():
    background = pygame.image.load('Images/wall1.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))


    gameOverMiner = pygame.image.load('Images/game_over_miner.png')
    gameOverMiner = pygame.transform.scale(gameOverMiner, (120, 120))

    screen.blit(gameOverMiner, (800, 400))
    

    while True:
        buttonWidth = 300
        buttonHeight = 50
        playAgainButton = button(screen, ((WIDTH - buttonWidth) / 2 - 75, (HEIGHT - buttonHeight) / 2 , buttonWidth + 150, buttonHeight),
                            "Play Again", buttonHeight - 10)
        mainMenuButton = button(screen, (
        (WIDTH - buttonWidth) / 2 - 70, (HEIGHT - buttonHeight) / 2 + 100, buttonWidth + 140, buttonHeight), "Main Menu",
                            buttonHeight - 10)

        pygame.mouse.set_visible(True)
        mx, my = pygame.mouse.get_pos()

        draw_text('Game over', font, (255, 255, 255), screen, WIDTH / 2 - 40*5, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playAgainButton.collidepoint((mx, my)):
                    buttonPressedSound.play()
                    Game()
                if mainMenuButton.collidepoint((mx, my)):
                    buttonPressedSound.play() 
                    main_menu()

        pygame.display.update()

main_menu()

