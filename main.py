import pygame, sys

# Initialization
pygame.init()

WIDTH = 1200
HEIGHT = 800

characterOption = 'Images/miner1.png'

# window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Diamond Collector')

window_icon = pygame.image.load('Images/window_icon.png')
pygame.display.set_icon(window_icon)

font = pygame.font.SysFont('Arial', 40)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
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
    text_render = font.render(text, 1, (255, 0, 0))
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

        button_width = 200
        button_height = 50

        playButton = button(screen,
                            ((WIDTH - button_width) / 2, (HEIGHT - button_height) / 2, button_width, button_height),
                            "Play", button_height - 10)
        quitButton = button(screen, (
        (WIDTH - button_width) / 2, (HEIGHT - button_height) / 2 + 100, button_width, button_height), "Options",
                            button_height - 10)

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
    score = 0
    screen.fill((0, 0, 0))
    # miner

    miner = pygame.image.load(characterOption)
    miner_height, miner_width = 120, 120

    miner = pygame.transform.scale(miner, (miner_height, miner_width))

    # game loop
    running = True
    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)

        screen.fill((102, 113, 62))
        screen.blit(miner, (mouse_x - 60, HEIGHT - 120))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


main_menu()
