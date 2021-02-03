import numpy as np
import board as b
import pygame
import gui
import random
import sys
import matplotlib.pyplot as plt


def initialize(board, game_screen_1):
    random_number_placer(board)
    random_number_placer(board)
    board_to_gui(board, game_screen_1)
    global score
    score = 0


def board_to_gui(board, game_screen):
    for value in range(0, 16):
        if value < 4:
            number = int(board.get_value(value, 0))
            gui.erase_number(value, 0, game_screen)
            if number != 0:
                gui.draw_number(number, value, 0, game_screen)
        elif value < 8:
            number = int(board.get_value(value - 4, 1))
            gui.erase_number(value - 4, 1, game_screen)
            if number != 0:
                gui.draw_number(number, value - 4, 1, game_screen)
        elif value < 12:
            number = int(board.get_value(value - 8, 2))
            gui.erase_number(value - 8, 2, game_screen)
            if number != 0:
                gui.draw_number(number, value - 8, 2, game_screen)
        else:
            number = int(board.get_value(value - 12, 3))
            gui.erase_number(value - 12, 3, game_screen)
            if number != 0:
                gui.draw_number(number, value - 12, 3, game_screen)


def random_number_generator():
    global score
    number = random.randint(0, 2)
    if number == 0:
        score += 2
        return 2
    else:
        score += 4
        return 4


def random_number_placer(board):
    new_number = random_number_generator()
    number_free = board.iterate() - 1
    if number_free == 0:
        pass
    random_number = random.randint(0, number_free)
    full_counter = 0
    counter = 0
    for cell in np.nditer(board.board):
        if cell != 0:
            pass
        elif random_number == counter:
            if full_counter < 4:
                board.edit_board(full_counter, 0, new_number)
                return
            elif full_counter < 8:
                board.edit_board(full_counter - 4, 1, new_number)
                return
            elif full_counter < 12:
                board.edit_board(full_counter - 8, 2, new_number)
                return
            else:
                board.edit_board(full_counter - 12, 3, new_number)
                return
        else:
            counter = counter + 1
        full_counter = full_counter + 1


def name_check(string):
    return len(string.split()) == 2 or len(string.split()) == 1


FILENAME = 'scores.txt'
new_board = b.Board()

score = 0

pygame.init()

screen = pygame.display.set_mode((400, 600))
gui.fill_board(screen)
pygame.display.set_caption('2048')

gui.instructions(screen, (5, 425), 'Please enter your name', 'Press enter to start game',
                 'Press s to view statistics', )

run = True
name = ''
name_true = True
while run:
    for event in pygame.event.get():
        if name_true:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if name_check(name):
                        name_true = False
                    else:
                        gui.instructions(screen, (5, 300), 'Please enter a name ', 'with one or two words')

                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
            font = pygame.font.Font(None, 35)
            screen.fill((150, 150, 200), (0, 0, 400, 150))
            text = font.render(name, 1, (100, 0, 0))
            screen.blit(text, (5, 50))
            pygame.display.update()
            if not name_true:
                gui.fill_board(screen)
                gui.instructions(screen, (5, 425), 'Use arrow keys to move', 'Score:')
                gui.game_board(screen)
                initialize(new_board, screen)
        elif event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if new_board.check_down():
                    new_board.push_entire_board_down()
                    random_number_placer(new_board)
                    board_to_gui(new_board, screen)
                    gui.erase_score(screen)
                    gui.score(screen, score)
                    pygame.time.wait(100)
            elif event.key == pygame.K_UP:
                if new_board.check_up():
                    new_board.push_entire_board_up()
                    random_number_placer(new_board)
                    board_to_gui(new_board, screen)
                    gui.erase_score(screen)
                    gui.score(screen, score)
                    pygame.time.wait(100)
            elif event.key == pygame.K_RIGHT:
                if new_board.check_right():
                    new_board.push_entire_board_right()
                    random_number_placer(new_board)
                    board_to_gui(new_board, screen)
                    gui.erase_score(screen)
                    gui.score(screen, score)
                    pygame.time.wait(100)
            elif event.key == pygame.K_LEFT:
                if new_board.check_left():
                    new_board.push_entire_board_left()
                    random_number_placer(new_board)
                    board_to_gui(new_board, screen)
                    gui.erase_score(screen)
                    gui.score(screen, score)
                    pygame.time.wait(100)
        pygame.display.update()


try:
    file = open(FILENAME, 'a')
    file.write(f'{name} {score}\n')
    file.close()
except FileNotFoundError:
    print('File not found')
    sys.exit()
scores = {}
with open(FILENAME) as file:
    for line in file:
        info = line.split()
        if len(info) == 2:
            scores[info[0]] = int(info[1])
        else:
            scores[f'{info[0]} {info[1][0]}'] = int(info[2])
        scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
        if len(scores) > 10:
            temp = list(scores.keys())
            name = temp[10]
            scores.pop(name)

plt.bar(list(scores.keys()), list(scores.values()), align='center')

plt.xticks(rotation='vertical')

plt.title('Top 10 Scores')
plt.xlabel('Names')
plt.ylabel('Points')
plt.xticks(fontsize=7)


plt.show()

