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

    def draw_check_win(self, check_win, draw_text_won):
        """Check if player = 1 win or computer = 2"""
        if check_win(1):
            self.won_x = True
        elif check_win(2):
            self.won_o = True
        draw_text_won(self.won_x, self.screen, self.won_o)

    def rest_game(self, board, rectangles, score):
        self.won_x = False
        self.won_o = False
        self.won = False
        self.is_game_end = False
        board.clear()
        self.screen.fill((0, 0, 0))
        rectangles.rects(self.screen)
        score.score_x(self.screen)
        score.score_o(self.screen)


class Board:
    def __init__(self):
        self.cell = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def clear(self):
        self.cell = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def is_board_fill(self):
        """Check board is fill so that program know game is tie"""
        return self.cell[0][0] != 0 and self.cell[0][1] != 0 and \
            self.cell[0][2] != 0 and self.cell[1][0] != 0 and \
            self.cell[1][1] != 0 and self.cell[1][2] != 0 and \
            self.cell[2][0] != 0 and self.cell[2][1] != 0 and \
            self.cell[2][2] != 0

    def check_win(self, number):
        """Check all the win on the board"""
        for row in self.cell:
            for tile in row:
                if tile == number:
                    continue
                break
            else:
                return True
        for column in range(3):
            for row in self.cell:
                if row[column] == number:
                    continue
                break
            else:
                return True
        for tile in range(3):
            if self.cell[tile][tile] == number:
                continue
            break
        else:
            return True
        for tile in range(3):
            if self.cell[tile][2 - tile] == number:
                continue
            break
        else:
            return True


class DrawScore:
    def draw_text_pos(self, screen, pos_one, pos_two, apos_one, apos_two):
        screen.blit(self.over_text, (pos_one, pos_two))
        screen.blit(self.space_text, (apos_one, apos_two))

    def draw_text_won(self, won_x, screen, won_o):
        """When someone won, this function will run"""
        if won_x:
            self.over_text = OVER_FONT.render("X won", True, LIGHT_BLUE)
            self.space_text = OVER_FONT.render("Space bar for clear", True, LIGHT_BLUE)
            self.draw_text_pos(screen, 215, 230, 50, 300)
        elif won_o:
            self.over_text = OVER_FONT.render("Computer won", True, PINK)
            self.space_text = OVER_FONT.render("Space bar for clear", True, PINK)
            self.draw_text_pos(screen, 140, 230, 50, 300)

    def tie(self, screen):
        """When game tie, this function will run"""
        self.over_text = OVER_FONT.render("Tie", True, DARK_BLUE)
        self.space_text = OVER_FONT.render("Space bar for clear", True, DARK_BLUE)
        self.draw_text_pos(screen, 225, 230, 50, 300)


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
        self.w_resize, self.h_resize = 110, 110
        self.x_img = pygame.image.load(os.path.join(project_directory, "img/x.png"))
        self.o_img = pygame.image.load(os.path.join(project_directory, "img/o.png"))
        self.x_img = pygame.transform.scale(self.x_img, (self.w_resize, self.h_resize))
        self.o_img = pygame.transform.scale(self.o_img, (self.w_resize, self.h_resize))
        self.current_player_turn = "X"
        self.current_player = "X"

    def pick_random_ai(self, board, screen):
        """AI pick on the random board after best_ai()"""
        while self.current_player_turn == "Computer":
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            x_pos = [50, 225, 400][column]
            y_pos = [50, 225, 400][row]
            if board.cell[row][column] == 0:
                screen.blit(self.o_img, (x_pos, y_pos))
                board.cell[row][column] = 2
                self.current_player_turn = "X"

    def hardcode_path(self, pos_one, pos_two, cell_one, cell_two, board, screen):
        screen.blit(self.o_img, (pos_one, pos_two))
        board.cell[cell_one][cell_two] = 2
        self.current_player_turn = "X"

    def best_ai(self, board, screen):
        """Hardcode path for ai"""
        if board.cell[1][1] == 0:
            self.hardcode_path(225, 225, 1, 1, board, screen)
        elif board.cell[0][2] == 0:
            self.hardcode_path(400, 50, 0, 2, board, screen)
        elif board.cell[0][1] == 1 and board.cell[0][2] == 1 and board.cell[0][0] == 0:
            self.hardcode_path(50, 50, 0, 0, board, screen)
        elif board.cell[1][1] == 1 and board.cell[1][2] == 1 and board.cell[0][1] == 0:
            self.hardcode_path(50, 225, 1, 0, board, screen)
        elif board.cell[2][1] == 1 and board.cell[2][2] == 1 and board.cell[2][0] == 0:
            self.hardcode_path(50, 400, 2, 0, board, screen)
        elif board.cell[0][0] == 1 and board.cell[1][0] == 1 and board.cell[2][0] == 0:
            self.hardcode_path(50, 400, 2, 0, board, screen)
        else:
            self.pick_random_ai(board, screen)

    def flip_ai_player(self):
        """Change turns for player and computer"""
        if self.current_player_turn == "X":
            self.current_player_turn = "Computer"
        elif self.current_player_turn == "Computer":
            self.current_player_turn = "X"

    def is_player_click(self, position, index_board, index_board_two, x_pos,
                        o_pos, board, screen):
        """Check all the logic here, including mouse click, placing images,
        updating the board"""
        pos = pygame.mouse.get_pos()
        if position.collidepoint(pos) and board.cell[index_board][index_board_two] == 0:
            if self.current_player == "X":
                screen.blit(self.x_img, (x_pos, o_pos))
                board.cell[index_board][index_board_two] = 1
                if not board.is_board_fill():
                    self.best_ai(board, screen)
                    self.flip_ai_player()


class Rectangle:
    def __init__(self):
        self.boxs = []

    def rects(self, screen):
        """Draw all the nine box for place x and o images"""
        width, height = 150, 150
        position = [25, 200, 375]
        for i in range(3):
            for j in range(3):
                self.boxs.append(pygame.draw.rect(screen, WHITE,
                                                  (position[j], position[i],
                                                   width, height)))

    def logic_handling(self, is_click, won, board, screen):
        """All the logic handling happens here"""
        position = [50, 225, 400]
        box_pos = [0, 1, 2]
        count = 0
        if won:
            return
        for i in range(3):
            for j in range(3):
                is_click(self.boxs[count], box_pos[i], box_pos[j], position[j],
                         position[i], board, screen)
                count += 1


def main():
    game_variable = GameVariables()
    rectangles = Rectangle()
    ai = AI()
    score = Score()
    draw_score = DrawScore()
    board = Board()

    rectangles.rects(game_variable.screen)
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                """Execute everytime when mouse is click"""
                if not game_variable.won_x or game_variable.won_o:
                    rectangles.logic_handling(ai.is_player_click, game_variable.won,
                                              board, game_variable.screen)
                    score.score_x(game_variable.screen)
                    score.score_o(game_variable.screen)
                    game_variable.draw_check_win(board.check_win, draw_score.draw_text_won)
                """If baord is fill(game tie) then draw tie text on the screen"""
                if (game_variable.won_x is False and game_variable.won_o is False
                        and board.is_board_fill()):
                    draw_score.tie(game_variable.screen)
                """If game is not yet end, keep on checking who who(player or AI)"""
                if game_variable.is_game_end is False:
                    if board.check_win(1):
                        game_variable.is_game_end = True
                        game_variable.won = True
                        score.x_score += 1
                    if board.check_win(2):
                        game_variable.is_game_end = True
                        game_variable.won = True
                        score.o_score += 1
            """If Space Bar is hit, rest the game state"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_variable.rest_game(board, rectangles, score)
        pygame.display.update()


if __name__ == '__main__':
    main()
