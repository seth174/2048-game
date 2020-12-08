import numpy as np
import board as b
import pygame
import gui
import random


def initialize(board, game_screen_1):
    random_number_placer(board)
    random_number_placer(board)
    board_to_gui(board, game_screen_1)


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
    number = random.randint(0, 2)
    if number == 0:
        return 2
    else:
        return 4


def random_number_placer(board):
    new_number = random_number_generator()
    number_free = board.iterate() - 1
    if number_free == 0:
        pass
    print(f'number of free slots: {number_free}')
    random_number = random.randint(0, number_free)
    print(f'random number where it will be place: {random_number}')
    full_counter = 0
    counter = 0
    for cell in np.nditer(board.board):
        if cell != 0:
            print('pass')
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


new_board = b.Board()

pygame.init()
screen = pygame.display.set_mode((400, 400))
gui.game_board(screen)
run = True
initialize(new_board, screen)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if new_board.check_down():
                    new_board.push_entire_board_down()
                    random_number_placer(new_board)
                    board_to_gui(new_board, screen)
                    pygame.time.wait(100)
            elif event.key == pygame.K_UP:
                if new_board.check_up():
                    new_board.push_entire_board_up()
                    random_number_placer(new_board)
                    board_to_gui(new_board, screen)
                    pygame.time.wait(100)
            elif event.key == pygame.K_RIGHT:
                if new_board.check_right():
                    new_board.push_entire_board_right()
                    random_number_placer(new_board)
                    board_to_gui(new_board, screen)
                    pygame.time.wait(100)
            elif event.key == pygame.K_LEFT:
                if new_board.check_left():
                    new_board.push_entire_board_left()
                    random_number_placer(new_board)
                    board_to_gui(new_board, screen)
                    pygame.time.wait(100)
        pygame.display.update()