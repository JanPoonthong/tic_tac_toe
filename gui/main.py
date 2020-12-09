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
ARCADECLASSIC = os.path.join(project_directory, "font/arcadeclassic.regular.ttf")
FONT = pygame.font.Font(ARCADECLASSIC, 32)
OVER_FONT = pygame.font.Font(ARCADECLASSIC, 50)


class GameVariables:
    def __init__(self):
        """All the Game variables"""
        # Screen
        self.width, self.height = 550, 650
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        # Images
        self.x_img = pygame.image.load(os.path.join(project_directory, "img/x.png"))
        self.o_img = pygame.image.load(os.path.join(project_directory, "img/o.png"))
        self.w_resize, self.h_resize = 110, 110
        self.x_img = pygame.transform.scale(self.x_img, (self.w_resize, self.h_resize))
        self.o_img = pygame.transform.scale(self.o_img, (self.w_resize, self.h_resize))
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

    def check_win(self, number):
        for row in self.board:
            for tile in row:
                if tile == number:
                    continue
                break
            else:
                return True

        for column in range(3):
            for row in self.board:
                if row[column] == number:
                    continue
                break
            else:
                return True

        for tile in range(3):
            if self.board[tile][tile] == number:
                continue
            break
        else:
            return True

        for tile in range(3):
            if self.board[tile][2 - tile] == number:
                continue
            break
        else:
            return True

    def num(self):
        """Check if player = 1 win or computer = 2"""
        if self.check_win(1):
            self.won_x = True
        elif self.check_win(2):
            self.won_o = True

    def is_board_fill(self):
        return self.board[0][0] != 0 and self.board[0][1] != 0 and \
               self.board[0][2] != 0 and self.board[1][0] != 0 and \
               self.board[1][1] != 0 and self.board[1][2] != 0 and \
               self.board[2][0] != 0 and self.board[2][1] != 0 and \
               self.board[2][2] != 0

    def draw_text_won(self):
        """When someone won, this function will run"""
        if self.won_x:
            over_text = OVER_FONT.render("X won", True, LIGHT_BLUE)
            space_text = OVER_FONT.render("Space bar for clear", True, LIGHT_BLUE)
            self.screen.blit(over_text, (220, 200))
            self.screen.blit(space_text, (50, 300))
        elif self.won_o:
            over_text = OVER_FONT.render("Computer won", True, PINK)
            space_text = OVER_FONT.render("Space bar for clear", True, PINK)
            self.screen.blit(over_text, (140, 200))
            self.screen.blit(space_text, (50, 300))

    def tie(self):
        """When game tie, this function will run"""
        tie_text = OVER_FONT.render("Tie", True, DARK_BLUE)
        space_text = OVER_FONT.render("Space bar for clear", True, DARK_BLUE)
        self.screen.blit(tie_text, (220, 200))
        self.screen.blit(space_text, (50, 300))


class Score:
    def score_x(self, x_score, screen):
        """Draw the score for X"""
        score_value = FONT.render("X  " + str(x_score), True, WHITE)
        screen.blit(score_value, (50, 550))

    def score_o(self, o_score, screen):
        """Draw the score for O"""
        score_value = FONT.render("O  " + str(o_score), True, WHITE)
        screen.blit(score_value, (50, 600))


class AI:
    def pick_random_ai(self, current_player_turn, o_img, board, screen):
        """AI pick on the random board after best_ai()"""
        while current_player_turn == "Computer":
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            x_pos = [50, 225, 400][column]
            y_pos = [50, 225, 400][row]
            if board[row][column] == 0:
                screen.blit(o_img, (x_pos, y_pos))
                board[row][column] = 2
                current_player_turn = "X"

    def best_ai(self, board, screen, current_player_turn, o_img):
        """Hardcode path for ai"""
        if board[1][1] == 0:
            screen.blit(o_img, (225, 225))
            board[1][1] = 2
            current_player_turn = "X"
        elif board[0][2] == 0:
            screen.blit(o_img, (400, 50))
            board[0][2] = 2
            current_player_turn = "X"
        elif board[0][1] == 1 and board[0][2] == 1 and board[0][0] == 0:
            x_pos = [50, 225, 400][0]
            y_pos = [50, 225, 400][0]
            board[0][0] = 2
            screen.blit(o_img, (x_pos, y_pos))
            current_player_turn = "X"
        elif board[1][1] == 1 and board[1][2] == 1 and board[0][1] == 0:
            x_pos = [50, 225, 400][0]
            y_pos = [50, 225, 400][1]
            board[1][0] = 2
            screen.blit(o_img, (x_pos, y_pos))
            current_player_turn = "X"
        elif board[2][1] == 1 and board[2][2] == 1 and board[2][0] == 0:
            x_pos = [50, 225, 400][0]
            y_pos = [50, 225, 400][2]
            board[2][0] = 2
            screen.blit(o_img, (x_pos, y_pos))
            current_player_turn = "X"
        elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 0:
            x_pos = [50, 225, 400][0]
            y_pos = [50, 225, 400][2]
            board[2][0] = 2
            screen.blit(o_img, (x_pos, y_pos))
            current_player_turn = "X"
        else:
            self.pick_random_ai(game_variable.current_player_turn, game_variable.o_img, game_variable.board, game_variable.screen)

    def flip_ai_player(self, current_player_turn):
        """Change turns for player and computer"""
        if current_player_turn == "X":
            current_player_turn = "Computer"
        elif current_player_turn == "Computer":
            current_player_turn = "X"

    def is_player_click(self, position, index_board, index_board_two, x_pos, o_pos, board, x_img, current_player, screen):
        """Check all the logic here, including mouse click, placing images,
        updating the board"""
        pos = pygame.mouse.get_pos()
        if position.collidepoint(pos) and board[index_board][index_board_two] == 0:
            if current_player == "X":
                screen.blit(x_img, (x_pos, o_pos))
                board[index_board][index_board_two] = 1
                if not game_variable.is_board_fill():
                    self.best_ai(game_variable.board, game_variable.screen, game_variable.current_player_turn, game_variable.o_img)
                    self.flip_ai_player(game_variable.current_player_turn)


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
        self.first = pygame.draw.rect(screen, WHITE, (position[0], position[0], width, height))
        self.second = pygame.draw.rect(screen, WHITE, (position[1], position[0], width, height))
        self.third = pygame.draw.rect(screen, WHITE, (position[2], position[0], width, height))
        self.fourth = pygame.draw.rect(screen, WHITE, (position[0], position[1], width, height))
        self.fifth = pygame.draw.rect(screen, WHITE, (position[1], position[1], width, height))
        self.sixth = pygame.draw.rect(screen, WHITE, (position[2], position[1], width, height))
        self.seventh = pygame.draw.rect(screen, WHITE, (position[0], position[2], width, height))
        self.eighth = pygame.draw.rect(screen, WHITE, (position[1], position[2], width, height))
        self.ninth = pygame.draw.rect(screen, WHITE, (position[2], position[2], width, height))

    def logic_handling(self, is_click):
        """All the logic handling happens here"""
        position = [50, 225, 400]
        box_pos = [0, 1, 2]
        if game_variable.won:
            return
        is_click(self.first, box_pos[0], box_pos[0], position[0], position[0], game_variable.board, game_variable.x_img, game_variable.current_player, game_variable.screen)
        is_click(self.second, box_pos[0], box_pos[1], position[1], position[0], game_variable.board, game_variable.x_img, game_variable.current_player, game_variable.screen)
        is_click(self.third, box_pos[0], box_pos[2], position[2], position[0], game_variable.board, game_variable.x_img, game_variable.current_player, game_variable.screen)
        is_click(self.fourth, box_pos[1], box_pos[0], position[0], position[1], game_variable.board, game_variable.x_img, game_variable.current_player, game_variable.screen)
        is_click(self.fifth, box_pos[1], box_pos[1], position[1], position[1], game_variable.board, game_variable.x_img, game_variable.current_player, game_variable.screen)
        is_click(self.sixth, box_pos[1], box_pos[2], position[2], position[1], game_variable.board, game_variable.x_img, game_variable.current_player, game_variable.screen)
        is_click(self.seventh, box_pos[2], box_pos[0], position[0], position[2], game_variable.board, game_variable.x_img, game_variable.current_player, game_variable.screen)
        is_click(self.eighth, box_pos[2], box_pos[1], position[1], position[2], game_variable.board, game_variable.x_img, game_variable.current_player, game_variable.screen)
        is_click(self.ninth, box_pos[2], box_pos[2], position[2], position[2], game_variable.board, game_variable.x_img, game_variable.current_player, game_variable.screen)


game_variable = GameVariables()
rectangles = Rectangle()
ai = AI()
score = Score()
rectangles.rects(game_variable.screen)


while True:
    game_variable.clock.tick(game_variable.fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_variable.won_x or game_variable.won_o:
                rectangles.logic_handling(ai.is_player_click)
                score.score_x(game_variable.x_score, game_variable.screen)
                score.score_o(game_variable.o_score, game_variable.screen)
                game_variable.check_win(game_variable.num)
                game_variable.num()
                game_variable.draw_text_won()

            if game_variable.won_x is False and game_variable.won_o is False and game_variable.is_board_fill():
                game_variable.tie()
            if game_variable.is_game_end is False:
                if game_variable.check_win(1):
                    game_variable.is_game_end = True
                    game_variable.won = True
                    game_variable.x_score += 1
                if game_variable.check_win(2):
                    game_variable.is_game_end = True
                    game_variable.won = True
                    game_variable.o_score += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_variable.click = True
                game_variable.won_x = False
                game_variable.won_o = False
                game_variable.won = False
                game_variable.is_game_end = False
                game_variable.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                game_variable.screen.fill((0, 0, 0))
                rectangles.rects(game_variable.screen)
                ai.best_ai(game_variable.board, game_variable.screen, game_variable.current_player_turn, game_variable.o_img)
                ai.flip_ai_player(game_variable.current_player_turn)
                score.score_x(game_variable.x_score, game_variable.screen)
                score.score_o(game_variable.o_score, game_variable.screen)
    pygame.display.update()
