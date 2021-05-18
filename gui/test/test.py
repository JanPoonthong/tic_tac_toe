import sys

sys.path.append("../")
import main

game_variable = main.GameVariables()


def test_color():
    assert main.WHITE == (255, 255, 255)
    assert main.GREY == (72, 72, 72)
    assert main.BRIGHT_GREY == (60, 60, 90)
    assert main.BLACK == (0, 0, 0)
    assert main.DARK_BLUE == (9, 109, 209)
    assert main.PINK == (255, 0, 255)
    assert main.LIGHT_BLUE == (108, 176, 243)


def test_screen():
    assert game_variable.width == 550
    assert game_variable.height == 650


def test_fps():
    assert main.FPS == 15
