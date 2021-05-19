import pygame, sys, random
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

font = pygame.font.SysFont('Arial', 40)

# Sounds

gemCatchSound = pygame.mixer.Sound('Sounds/mixkit-game-ball-tap-2073.wav')
bombCatchSound = pygame.mixer.Sound('Sounds/mixkit-player-jumping-in-a-video-game-2043.wav')
pygame.mixer.music.load('Sounds/Child\'s Nightmare.ogg')


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def options():
    global characterOption
    characterOption = 'Images/miner1.png'
    running = True
    while running:

        screen.fill((102, 113, 62))
        pygame.mouse.set_visible(True)
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)

        miner1 = pygame.image.load('Images/miner1.png')
        miner2 = pygame.image.load('Images/miner2.png')
        miner3 = pygame.image.load('Images/miner3.png')

        miner_height, miner_width = 150, 150
        miner1 = pygame.transform.scale(miner1, (miner_height, miner_width))
        miner2 = pygame.transform.scale(miner2, (miner_height, miner_width))
        miner3 = pygame.transform.scale(miner3, (miner_height, miner_width))

        miner1Button = pygame.Rect(((WIDTH - miner_width) / 2, (HEIGHT - miner_height) / 2), (150, 150))
        miner2Button = pygame.Rect(((WIDTH - miner_width) / 2 - 200, (HEIGHT - miner_height) / 2), (150, 150))
        miner3Button = pygame.Rect(((WIDTH - miner_width) / 2 + 200, (HEIGHT - miner_height) / 2), (150, 150))

        screen.blit(miner1, ((WIDTH - miner_width) / 2, (HEIGHT - miner_height) / 2))
        screen.blit(miner2, ((WIDTH - miner_width) / 2 - 200, (HEIGHT - miner_height) / 2))
        screen.blit(miner3, ((WIDTH - miner_width) / 2 + 200, (HEIGHT - miner_height) / 2))

        mx, my = pygame.mouse.get_pos()

        dark = pygame.Surface((150, 150), flags=pygame.SRCALPHA)
        dark.fill((50, 50, 50, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if miner1Button.collidepoint((mx, my)):
                    characterOption = 'Images/miner1.png'
                    print(characterOption)
                if miner2Button.collidepoint((mx, my)):
                    characterOption = 'Images/miner2.png'
                    print(characterOption)
                if miner3Button.collidepoint((mx, my)):
                    characterOption = 'Images/miner3.png'
                    print(characterOption)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()


def button(screen, position, text, fontSize):
    font = pygame.font.SysFont("Arial", fontSize)
    text_render = font.render(text, True, (255, 0, 0))
    x, y, w, h = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))

    return screen.blit(text_render, (x, y))


def main_menu():
    while True:

        screen.fill((0, 200, 0))

        background = pygame.image.load('Images/wall1.png')
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        screen.blit(background, (0, 0))

        draw_text('Main menu', font, (255, 255, 255), screen, (WIDTH + HEIGHT) / 4, 20)
        pygame.mouse.set_visible(True)

        mx, my = pygame.mouse.get_pos()

        buttonWidth = 200
        buttonHeight = 50

        playButton = button(screen,
                            ((WIDTH - buttonWidth) / 2, (HEIGHT - buttonHeight) / 2, buttonWidth, buttonHeight),
                            "Play", buttonHeight - 10)
        quitButton = button(screen, (
            (WIDTH - buttonWidth) / 2, (HEIGHT - buttonHeight) / 2 + 100, buttonWidth, buttonHeight), "Options",
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
                    Game()
                if quitButton.collidepoint((mx, my)):
                    options()

        pygame.display.update()


def Game():
    global gemsNumber
    global bombsNumber
    global adder

    background = pygame.image.load('Images/wall2.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT)).convert_alpha()

    pygame.mixer.music.play(-1)
    scoreFont = pygame.font.SysFont('Arial', 30)
    score = 0
    lives = 3
    clock = pygame.time.Clock()

    player = Miner(characterOption, WIDTH / 2, HEIGHT - minerHeight / 2, minerWidth, minerHeight)
    miner = pygame.sprite.Group()
    print(player.rect.x, player.rect.y)
    miner.add(player)

    bonusLife = pygame.sprite.Group()
    gems = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    adder = True

    # add 'gemsNumber' gems in gems

    for _ in range(bombsNumber):
        x = random.randrange(bombWidth, WIDTH - bombWidth)
        y = random.randrange(-120, -90)
        bombs.add(Bomb('Images/bomb.png', x, y, bombHeight, bombWidth))

    for _ in range(gemsNumber):
        x = random.randrange(0, WIDTH - gemWidth)
        y = random.randrange(-65, -45)

        print(x, y)
        gems.add(Gem('Images/gem.png', x, y, gemHeight, gemWidth))

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
                    pygame.mixer.music.stop()
                    running = False

        for gem in gems:
            if pygame.sprite.collide_rect(gem, player):
                gem.rect.y = random.randrange(-80, -35)
                gem.rect.x = random.randrange(gemWidth, WIDTH - gemWidth)
                gemCatchSound.play()
                score += 1
                adder = True

        for bomb in bombs:
            if pygame.sprite.collide_rect(bomb, player):
                bomb.rect.y = random.randrange(-120, -90)
                bomb.rect.x = random.randrange(bombWidth, WIDTH - bombWidth)
                bombCatchSound.play()
                lives -= 1

                if lives == 0:
                    pygame.mixer.music.stop()
                    gemsNumber = 2
                    bombsNumber = 1
                    running = False

                adder = True
        for life in bonusLife:
            if pygame.sprite.collide_rect(life, player):
                life.rect.y = random.randrange(-80, -35)
                life.rect.x = random.randrange(gemWidth, WIDTH - gemWidth)
                gemCatchSound.play()
                lives += 1
                bonusLife.empty()
                adder = True
            if life.rect.y > HEIGHT - 80 and pygame.sprite.collide_rect(life, player) == False:
                life.rect.y = random.randrange(-80, -35)
                life.rect.x = random.randrange(gemWidth, WIDTH - gemWidth)
                bonusLife.empty()
                adder = True

        if score > 1 and score % 10 == 0 and adder:
            x = random.randrange(0, WIDTH - gemWidth)
            y = random.randrange(-65, -45)

            gems.add(Gem('Images/gem.png', x, y, gemHeight, gemWidth))
            gemsNumber += 1

            if score % 20 == 0 and adder:
                bombs.add(Bomb('Images/bomb.png', x, y, bombHeight, bombWidth))
                bombsNumber += 1

            if score > 1 and score % 30 == 0 and adder:
                x = random.randrange(0, WIDTH - gemWidth)
                y = random.randrange(-65, -45)
                bonusLife.add(Heart('Images/like.png', x, y, gemHeight, gemWidth))
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


main_menu()
