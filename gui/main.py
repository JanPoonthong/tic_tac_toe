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

# Colors
WHITE = (255, 255, 255)
GREY = (72, 72, 72)
BRIGHT_GREY = (60, 60, 90)
BLACK = (0, 0, 0)
DARK_BLUE = (9, 109, 209)
PINK = (255, 0, 255)
LIGHT_BLUE = (108, 176, 243)

# Font
ARCADECLASSIC = os.path.join(project_directory,
                             "font/arcadeclassic.regular.ttf")
FONT = pygame.font.Font(ARCADECLASSIC, 32)
OVER_FONT = pygame.font.Font(ARCADECLASSIC, 50)


class GameVariables:
    def __init__(self):
        """All the Game variables"""
        # Screen
        self.width, self.height = 550, 650
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        # Images
        self.x_img = pygame.image.load(
            os.path.join(project_directory, "img/x.png"))
        self.o_img = pygame.image.load(
            os.path.join(project_directory, "img/o.png"))
        self.w_rezise, self.h_rezise = 110, 110
        self.x_img = pygame.transform.scale(self.x_img,
                                            (self.w_rezise, self.h_rezise))
        self.o_img = pygame.transform.scale(self.o_img,
                                            (self.w_rezise, self.h_rezise))
        # Game state
        self.current_player = "X"
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.won = False
        self.won_x = False
        self.won_o = False
        self.x_score = 0
        self.o_score = 0
        self.is_click = "not click"
        self.is_game_end = False
        self.current_player_turn = "X"


class DrawRectangle:
    def __init__(self):
        self.first = pygame.draw.rect(game_variable.screen, WHITE,
                                      (25, 25, 150, 150))
        self.second = pygame.draw.rect(game_variable.screen, WHITE,
                                       (200, 25, 150, 150))
        self.third = pygame.draw.rect(game_variable.screen, WHITE,
                                      (375, 25, 150, 150))
        self.fourth = pygame.draw.rect(game_variable.screen, WHITE,
                                       (25, 200, 150, 150))
        self.fifth = pygame.draw.rect(game_variable.screen, WHITE,
                                      (200, 200, 150, 150))
        self.sixth = pygame.draw.rect(game_variable.screen, WHITE,
                                      (375, 200, 150, 150))
        self.seventh = pygame.draw.rect(game_variable.screen, WHITE,
                                        (25, 375, 150, 150))
        self.eighth = pygame.draw.rect(game_variable.screen, WHITE,
                                       (200, 375, 150, 150))
        self.ninth = pygame.draw.rect(game_variable.screen, WHITE,
                                      (375, 375, 150, 150))


class IsGameEnd:
    def check_win(self, number):
        for row in game_variable.board:
            for tile in row:
                if tile == number:
                    continue
                break
            else:
                return True

        for column in range(3):
            for row in game_variable.board:
                if row[column] == number:
                    continue
                break
            else:
                return True

        for tile in range(3):
            if game_variable.board[tile][tile] == number:
                continue
            break
        else:
            return True

        for tile in range(3):
            if game_variable.board[tile][2 - tile] == number:
                continue
            break
        else:
            return True

    def num(self):
        if self.check_win(1):
            game_variable.won_x = True
        elif self.check_win(2):
            game_variable.won_o = True

    @staticmethod
    def is_board_fill():
        return game_variable.board[0][0] != 0 and game_variable.board[0][
            1] != 0 and \
               game_variable.board[0][2] != 0 and game_variable.board[1][
                   0] != 0 and \
               game_variable.board[1][1] != 0 and game_variable.board[1][
                   2] != 0 and \
               game_variable.board[2][0] != 0 and game_variable.board[2][
                   1] != 0 and \
               game_variable.board[2][2] != 0


class DrawScore:
    @staticmethod
    def score_x():
        score_value = FONT.render("X  " + str(game_variable.x_score), True,
                                  WHITE)
        game_variable.screen.blit(score_value, (50, 550))

    @staticmethod
    def score_o():
        score_value = FONT.render("O  " + str(game_variable.o_score), True,
                                  WHITE)
        game_variable.screen.blit(score_value, (50, 600))


class DrawWonText:
    @staticmethod
    def draw_text_won():
        if game_variable.won_x:
            over_text = OVER_FONT.render("X won", True, LIGHT_BLUE)
            space_text = OVER_FONT.render("Space bar for clear", True,
                                          LIGHT_BLUE)
            game_variable.screen.blit(over_text, (220, 200))
            game_variable.screen.blit(space_text, (50, 300))
        elif game_variable.won_o:
            over_text = OVER_FONT.render("Computer won", True, PINK)
            space_text = OVER_FONT.render("Space bar for clear", True, PINK)
            game_variable.screen.blit(over_text, (140, 200))
            game_variable.screen.blit(space_text, (50, 300))

    @staticmethod
    def tie():
        tie_text = OVER_FONT.render("Tie", True, DARK_BLUE)
        space_text = OVER_FONT.render("Space bar for clear", True, DARK_BLUE)
        game_variable.screen.blit(tie_text, (220, 200))
        game_variable.screen.blit(space_text, (50, 300))


class AI:
    @staticmethod
    def ai():
        while game_variable.current_player_turn == "Computer":
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            x = [50, 225, 400][column]
            y = [50, 225, 400][row]
            if game_variable.board[row][column] == 0:
                game_variable.screen.blit(game_variable.o_img, (x, y))
                game_variable.board[row][column] = 2
                game_variable.current_player_turn = "X"

    @staticmethod
    def best_ai():
        if game_variable.board[1][1] == 0:
            game_variable.screen.blit(game_variable.o_img, (225, 225))
            game_variable.board[1][1] = 2
            game_variable.current_player_turn = "X"

        elif game_variable.board[0][2] == 0:
            game_variable.screen.blit(game_variable.o_img, (400, 50))
            game_variable.board[0][2] = 2
            game_variable.current_player_turn = "X"

        elif game_variable.board[0][1] == 1 and game_variable.board[0][
                2] == 1 and game_variable.board[0][0] == 0:
            x = [50, 225, 400][0]
            y = [50, 225, 400][0]
            game_variable.board[0][0] = 2
            game_variable.screen.blit(game_variable.o_img, (x, y))
            game_variable.current_player_turn = "X"

        elif game_variable.board[1][1] == 1 and game_variable.board[1][
                2] == 1 and game_variable.board[0][1] == 0:
            x = [50, 225, 400][0]
            y = [50, 225, 400][1]
            game_variable.board[1][0] = 2
            game_variable.screen.blit(game_variable.o_img, (x, y))
            game_variable.current_player_turn = "X"

        elif game_variable.board[2][1] == 1 and game_variable.board[2][
                2] == 1 and game_variable.board[2][0] == 0:
            x = [50, 225, 400][0]
            y = [50, 225, 400][2]
            game_variable.board[2][0] = 2
            game_variable.screen.blit(game_variable.o_img, (x, y))
            game_variable.current_player_turn = "X"

        elif game_variable.board[0][0] == 1 and game_variable.board[1][
                0] == 1 and game_variable.board[2][0] == 0:
            x = [50, 225, 400][0]
            y = [50, 225, 400][2]
            game_variable.board[2][0] = 2
            game_variable.screen.blit(game_variable.o_img, (x, y))
            game_variable.current_player_turn = "X"

        else:
            ai.ai()

    @staticmethod
    def flip_ai_player():
        if game_variable.current_player_turn == "X":
            game_variable.current_player_turn = "Computer"
        elif game_variable.current_player_turn == "Computer":
            game_variable.current_player_turn = "X"


class GameLogic:
    @staticmethod
    def mode_ai():
        pos = pygame.mouse.get_pos()

        if game_variable.won is not True:
            if draw_rectangle.first.collidepoint(pos) and \
                    game_variable.board[0][0] == 0:
                if game_variable.current_player == "X":
                    game_variable.screen.blit(game_variable.x_img, (50, 50))
                    game_variable.board[0][0] = 1
                    if not is_game_end.is_board_fill():
                        ai.best_ai()
                        ai.flip_ai_player()

            if draw_rectangle.second.collidepoint(pos) and \
                    game_variable.board[0][1] == 0:
                if game_variable.current_player == "X":
                    game_variable.screen.blit(game_variable.x_img, (225, 50))
                    game_variable.board[0][1] = 1
                    if not is_game_end.is_board_fill():
                        ai.best_ai()
                        ai.flip_ai_player()

            if draw_rectangle.third.collidepoint(pos) and \
                    game_variable.board[0][2] == 0:
                if game_variable.current_player == "X":
                    game_variable.screen.blit(game_variable.x_img, (400, 50))
                    game_variable.board[0][2] = 1
                    if not is_game_end.is_board_fill():
                        ai.best_ai()
                        ai.flip_ai_player()

            if draw_rectangle.fourth.collidepoint(pos) and \
                    game_variable.board[1][0] == 0:
                if game_variable.current_player == "X":
                    game_variable.screen.blit(game_variable.x_img, (50, 225))
                    game_variable.board[1][0] = 1
                    if not is_game_end.is_board_fill():
                        ai.best_ai()
                        ai.flip_ai_player()

            if draw_rectangle.fifth.collidepoint(pos) and \
                    game_variable.board[1][1] == 0:
                if game_variable.current_player == "X":
                    game_variable.screen.blit(game_variable.x_img, (225, 225))
                    game_variable.board[1][1] = 1
                    if not is_game_end.is_board_fill():
                        ai.best_ai()
                        ai.flip_ai_player()

            if draw_rectangle.sixth.collidepoint(pos) and \
                    game_variable.board[1][2] == 0:
                if game_variable.current_player == "X":
                    game_variable.screen.blit(game_variable.x_img, (400, 225))
                    game_variable.board[1][2] = 1
                    if not is_game_end.is_board_fill():
                        ai.best_ai()
                        ai.flip_ai_player()

            if draw_rectangle.seventh.collidepoint(pos) and \
                    game_variable.board[2][0] == 0:
                if game_variable.current_player == "X":
                    game_variable.screen.blit(game_variable.x_img, (50, 400))
                    game_variable.board[2][0] = 1
                    if not is_game_end.is_board_fill():
                        ai.best_ai()
                        ai.flip_ai_player()

            if draw_rectangle.eighth.collidepoint(pos) and \
                    game_variable.board[2][1] == 0:
                if game_variable.current_player == "X":
                    game_variable.screen.blit(game_variable.x_img, (225, 400))
                    game_variable.board[2][1] = 1
                    if not is_game_end.is_board_fill():
                        ai.best_ai()
                        ai.flip_ai_player()

            if draw_rectangle.ninth.collidepoint(pos) and \
                    game_variable.board[2][2] == 0:
                if game_variable.current_player == "X":
                    game_variable.screen.blit(game_variable.x_img, (400, 400))
                    game_variable.board[2][2] = 1
                    if not is_game_end.is_board_fill():
                        ai.best_ai()
                        ai.flip_ai_player()


game_variable = GameVariables()
is_game_end = IsGameEnd()
draw_score = DrawScore()
draw_won_text = DrawWonText()
ai = AI()
game_logic = GameLogic()
draw_rectangle = DrawRectangle()

while True:
    CLICK = pygame.mouse.get_pressed()
    game_variable.clock.tick(game_variable.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_variable.won_x = False
                game_variable.won_o = False
                game_variable.won = False
                game_variable.is_game_end = False
                game_variable.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                game_variable.screen.fill((0, 0, 0))
                DrawRectangle()
                ai.best_ai()
                ai.flip_ai_player()

        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                game_logic.mode_ai()
            except NameError:
                pass

            is_game_end.check_win(is_game_end.num)
            is_game_end.num()

            if (game_variable.won_x is False and game_variable.won_o is
                    False and is_game_end.is_board_fill()):
                draw_won_text.tie()

            if game_variable.is_game_end is False:
                if is_game_end.check_win(1):
                    game_variable.is_game_end = True
                    game_variable.won = True
                    game_variable.x_score += 1
                if is_game_end.check_win(2):
                    game_variable.is_game_end = True
                    game_variable.won = True
                    game_variable.o_score += 1

            draw_won_text.draw_text_won()

        draw_score.score_x()
        draw_score.score_o()

    pygame.display.update()
