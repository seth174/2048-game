import pygame

BOARD_COLOR = (150, 150, 200)
def game_board(screen):

    pygame.draw.line(screen, (35, 9, 56), (0, 0), (0, 400), 5)
    pygame.draw.line(screen, (35, 9, 56), (100, 0), (100, 400), 5)
    pygame.draw.line(screen, (35, 9, 56), (200, 0), (200, 400), 5)
    pygame.draw.line(screen, (35, 9, 56), (300, 0), (300, 400), 5)
    pygame.draw.line(screen, (35, 9, 56), (400, 0), (400, 400), 5)

    pygame.draw.line(screen, (35, 9, 56), (0, 0), (400, 0), 5)
    pygame.draw.line(screen, (35, 9, 56), (0, 100), (400, 100), 5)
    pygame.draw.line(screen, (35, 9, 56), (0, 200), (400, 200), 5)
    pygame.draw.line(screen, (35, 9, 56), (0, 300), (400, 300), 5)
    pygame.draw.line(screen, (35, 9, 56), (0, 400), (400, 400), 5)

    pygame.display.update()


def draw_number(value, row, column, screen):
    x_position = column * 100
    y_position = row * 100
    size = 0
    x_position_number = 0
    y_position_number = 0
    if value < 10:
        x_position_number = (column * 100) + 35
        y_position_number = (row * 100) + 25
        size = 90
    elif value < 100:
        x_position_number = (column * 100) + 17
        y_position_number = (row * 100) + 25
        size = 85
    elif value < 1000:
        x_position_number = (column * 100) + 7
        y_position_number = (row * 100) + 27
        size = 75
    elif value < 10000:
        x_position_number = (column * 100) + 5
        y_position_number = (row * 100) + 35
        size = 55
    color = get_color(value)
    square = pygame.draw.rect(screen, color, (x_position + 3, y_position + 3, 95, 95))
    font = pygame.font.Font(None, size)
    text = font.render(str(value), 1, (0, 0, 0))
    screen.blit(text, (x_position_number, y_position_number))
    pygame.display.update()


def erase_number(row, column, screen):
    x_position = column * 100
    y_position = row * 100
    screen.fill((150, 150, 200), (x_position + 3, y_position + 3, 95, 95))
    pygame.display.update()


def get_color(value):
    if value == 2:
        return 240, 248, 255
    elif value == 4:
        return 250, 235, 215
    elif value == 8:
        return 255, 127, 80
    elif value == 16:
        return 0, 191, 255
    elif value == 32:
        return 32, 178, 170
    elif value == 64:
        return 0, 250, 154
    elif value == 128:
        return 64, 224, 208
    elif value == 256:
        return 255, 255, 0
    elif value == 512:
        return 255, 215, 0
    elif value == 1024:
        return 205, 92, 92
    elif value == 2048:
        return 255, 69, 0
    elif value == 4096:
        return 255, 99, 71
    else:
        return 0, 0, 0


def move_number(screen, direction, numbers_placed):
    pass

def fill_board(screen):
    screen.fill(BOARD_COLOR)
    pygame.display.update()

def clear_instructions(screen):
    screen.fill(BOARD_COLOR, (0, 400, 400, 600))
    pygame.display.update()

def instructions(screen, starting_position, *string, ):
    x, y = starting_position
    y_position = y
    for sentence in string:
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (100, 0, 0))
        screen.blit(text, (x, y_position))
        y_position += 50
    pygame.display.update()

def erase_score(screen):
    screen.fill(BOARD_COLOR, (0, 500, 400, 100))
    pygame.display.update()

def score(screen, new_score):
    font = pygame.font.Font(None, 35)
    text = font.render(str(new_score), 1, (100, 0, 0))
    screen.blit(text, (20, 500))




