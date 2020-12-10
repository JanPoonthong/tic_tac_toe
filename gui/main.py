import os.path
import random
import sys
import pygame

pygame.init()

pygame.display.set_caption("Tic Tac Toe")
project_directory = os.path.dirname(__file__)
"""Author https://www.flaticon.com/free-icon/tic-tac-toe_566294 for icon.png"""
ICON = pygame.image.load(os.path.join(project_directory, "img/icon.png"))
pygame.display.set_icon(ICON)

WHITE = (255, 255, 255)
GREY = (72, 72, 72)
BRIGHT_GREY = (60, 60, 90)
BLACK = (0, 0, 0)
DARK_BLUE = (9, 109, 209)
PINK = (255, 0, 255)
LIGHT_BLUE = (108, 176, 243)

ARCADECLASSIC = os.path.join(project_directory, "font/font.regular.ttf")
FONT = pygame.font.Font(ARCADECLASSIC, 32)
OVER_FONT = pygame.font.Font(ARCADECLASSIC, 50)

CLOCK = pygame.time.Clock()
FPS = 15


class GameVariables:
    def __init__(self):
        self.width, self.height = 550, 650
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.won = False
        self.won_x = False
        self.won_o = False
        self.is_game_end = False

    def num(self, check_win, draw_text_won, board):
        """Check if player = 1 win or computer = 2"""
        if check_win(1, board):
            self.won_x = True
        elif check_win(2, board):
            self.won_o = True
        draw_text_won(self.won_x, self.screen, self.won_o)


class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


class IsGameEnd:
    @staticmethod
    def check_win(number, board):
        """Check all the win on the board"""
        for row in board:
            for tile in row:
                if tile == number:
                    continue
                break
            else:
                return True
        for column in range(3):
            for row in board:
                if row[column] == number:
                    continue
                break
            else:
                return True
        for tile in range(3):
            if board[tile][tile] == number:
                continue
            break
        else:
            return True
        for tile in range(3):
            if board[tile][2 - tile] == number:
                continue
            break
        else:
            return True

    @staticmethod
    def is_board_fill(board):
        """Check board is fill so that program know game is tie"""
        return board[0][0] != 0 and board[0][1] != 0 and \
            board[0][2] != 0 and board[1][0] != 0 and \
            board[1][1] != 0 and board[1][2] != 0 and \
            board[2][0] != 0 and board[2][1] != 0 and \
            board[2][2] != 0


class DrawScore:
    @staticmethod
    def draw_text_won(won_x, screen, won_o):
        """When someone won, this function will run"""
        if won_x:
            over_text = OVER_FONT.render("X won", True, LIGHT_BLUE)
            space_text = OVER_FONT.render("Space bar for clear", True, LIGHT_BLUE)
            screen.blit(over_text, (220, 200))
            screen.blit(space_text, (50, 300))
        elif won_o:
            over_text = OVER_FONT.render("Computer won", True, PINK)
            space_text = OVER_FONT.render("Space bar for clear", True, PINK)
            screen.blit(over_text, (140, 200))
            screen.blit(space_text, (50, 300))

    @staticmethod
    def tie(screen):
        """When game tie, this function will run"""
        tie_text = OVER_FONT.render("Tie", True, DARK_BLUE)
        space_text = OVER_FONT.render("Space bar for clear", True, DARK_BLUE)
        screen.blit(tie_text, (220, 200))
        screen.blit(space_text, (50, 300))


class Score:
    def __init__(self):
        self.x_score = 0
        self.o_score = 0

    def score_x(self, screen):
        """Draw the score for X"""
        score_value = FONT.render("X  " + str(self.x_score), True, WHITE)
        screen.blit(score_value, (50, 550))

    def score_o(self, screen):
        """Draw the score for O"""
        score_value = FONT.render("O  " + str(self.o_score), True, WHITE)
        screen.blit(score_value, (50, 600))


class AI:
    def __init__(self):
        self.current_player_turn = "X"
        self.w_resize, self.h_resize = 110, 110
        self.x_img = pygame.image.load(os.path.join(project_directory, "img/x.png"))
        self.o_img = pygame.image.load(os.path.join(project_directory, "img/o.png"))
        self.x_img = pygame.transform.scale(self.x_img, (self.w_resize, self.h_resize))
        self.o_img = pygame.transform.scale(self.o_img, (self.w_resize, self.h_resize))
        self.current_player = "X"

    def pick_random_ai(self, board, screen):
        """AI pick on the random board after best_ai()"""
        while self.current_player_turn == "Computer":
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            x_pos = [50, 225, 400][column]
            y_pos = [50, 225, 400][row]
            if board[row][column] == 0:
                screen.blit(self.o_img, (x_pos, y_pos))
                board[row][column] = 2
                self.current_player_turn = "X"

    def best_ai(self, board, screen):
        """Hardcode path for ai"""
        if board[1][1] == 0:
            screen.blit(self.o_img, (225, 225))
            board[1][1] = 2
            self.current_player_turn = "X"
        elif board[0][2] == 0:
            screen.blit(self.o_img, (400, 50))
            board[0][2] = 2
            self.current_player_turn = "X"
        elif board[0][1] == 1 and board[0][2] == 1 and board[0][0] == 0:
            x_pos = [50, 225, 400][0]
            y_pos = [50, 225, 400][0]
            board[0][0] = 2
            screen.blit(self.o_img, (x_pos, y_pos))
            self.current_player_turn = "X"
        elif board[1][1] == 1 and board[1][2] == 1 and board[0][1] == 0:
            x_pos = [50, 225, 400][0]
            y_pos = [50, 225, 400][1]
            board[1][0] = 2
            screen.blit(self.o_img, (x_pos, y_pos))
            self.current_player_turn = "X"
        elif board[2][1] == 1 and board[2][2] == 1 and board[2][0] == 0:
            x_pos = [50, 225, 400][0]
            y_pos = [50, 225, 400][2]
            board[2][0] = 2
            screen.blit(self.o_img, (x_pos, y_pos))
            self.current_player_turn = "X"
        elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 0:
            x_pos = [50, 225, 400][0]
            y_pos = [50, 225, 400][2]
            board[2][0] = 2
            screen.blit(self.o_img, (x_pos, y_pos))
            self.current_player_turn = "X"
        else:
            self.pick_random_ai(board, screen)

    def flip_ai_player(self):
        """Change turns for player and computer"""
        if self.current_player_turn == "X":
            self.current_player_turn = "Computer"
        elif self.current_player_turn == "Computer":
            self.current_player_turn = "X"

    def is_player_click(self, position, index_board, index_board_two, x_pos,
                        o_pos, board, screen, is_board_fill):
        """Check all the logic here, including mouse click, placing images,
        updating the board"""
        pos = pygame.mouse.get_pos()
        if position.collidepoint(pos) and board[index_board][index_board_two] == 0:
            if self.current_player == "X":
                screen.blit(self.x_img, (x_pos, o_pos))
                board[index_board][index_board_two] = 1
                if not is_board_fill(board):
                    self.best_ai(board, screen)
                    self.flip_ai_player()


class Rectangle:
    def __init__(self):
        self.first = None
        self.second = None
        self.third = None
        self.fourth = None
        self.fifth = None
        self.sixth = None
        self.seventh = None
        self.eighth = None
        self.ninth = None

    def rects(self, screen):
        """Draw all the nine box for place x and o images"""
        width, height = 150, 150
        position = [25, 200, 375]
        self.first = pygame.draw.rect(screen, WHITE,
                                      (position[0], position[0], width, height))
        self.second = pygame.draw.rect(screen, WHITE,
                                       (position[1], position[0], width, height))
        self.third = pygame.draw.rect(screen, WHITE,
                                      (position[2], position[0], width, height))
        self.fourth = pygame.draw.rect(screen, WHITE,
                                       (position[0], position[1], width, height))
        self.fifth = pygame.draw.rect(screen, WHITE,
                                      (position[1], position[1], width, height))
        self.sixth = pygame.draw.rect(screen, WHITE,
                                      (position[2], position[1], width, height))
        self.seventh = pygame.draw.rect(screen, WHITE,
                                        (position[0], position[2], width, height))
        self.eighth = pygame.draw.rect(screen, WHITE,
                                       (position[1], position[2], width, height))
        self.ninth = pygame.draw.rect(screen, WHITE,
                                      (position[2], position[2], width, height))

    def logic_handling(self, is_click, won, board, screen, is_board_fill):
        """All the logic handling happens here"""
        position = [50, 225, 400]
        box_pos = [0, 1, 2]
        if won:
            return
        is_click(self.first, box_pos[0], box_pos[0], position[0], position[0],
                 board, screen, is_board_fill)
        is_click(self.second, box_pos[0], box_pos[1], position[1], position[0],
                 board, screen, is_board_fill)
        is_click(self.third, box_pos[0], box_pos[2], position[2], position[0],
                 board, screen, is_board_fill)
        is_click(self.fourth, box_pos[1], box_pos[0], position[0], position[1],
                 board, screen, is_board_fill)
        is_click(self.fifth, box_pos[1], box_pos[1], position[1], position[1],
                 board, screen, is_board_fill)
        is_click(self.sixth, box_pos[1], box_pos[2], position[2], position[1],
                 board, screen, is_board_fill)
        is_click(self.seventh, box_pos[2], box_pos[0], position[0], position[2],
                 board, screen, is_board_fill)
        is_click(self.eighth, box_pos[2], box_pos[1], position[1], position[2],
                 board, screen, is_board_fill)
        is_click(self.ninth, box_pos[2], box_pos[2], position[2], position[2],
                 board, screen, is_board_fill)


def main():
    game_variable = GameVariables()
    rectangles = Rectangle()
    ai = AI()
    score = Score()
    draw_score = DrawScore()
    is_end = IsGameEnd()
    board = Board()

    rectangles.rects(game_variable.screen)
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_variable.won_x or game_variable.won_o:
                    rectangles.logic_handling(ai.is_player_click, game_variable.won,
                                              board.board, game_variable.screen,
                                              is_end.is_board_fill)
                    score.score_x(game_variable.screen)
                    score.score_o(game_variable.screen)
                    game_variable.num(is_end.check_win, draw_score.draw_text_won,
                                      board.board)
                if (game_variable.won_x is False and game_variable.won_o is False
                        and is_end.is_board_fill(board.board)):
                    draw_score.tie(game_variable.screen)
                if game_variable.is_game_end is False:
                    if is_end.check_win(1, board.board):
                        game_variable.is_game_end = True
                        game_variable.won = True
                        score.x_score += 1
                    if is_end.check_win(2, board.board):
                        game_variable.is_game_end = True
                        game_variable.won = True
                        score.o_score += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_variable.won_x = False
                    game_variable.won_o = False
                    game_variable.won = False
                    game_variable.is_game_end = False
                    board.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    game_variable.screen.fill((0, 0, 0))
                    rectangles.rects(game_variable.screen)
                    score.score_x(game_variable.screen)
                    score.score_o(game_variable.screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
