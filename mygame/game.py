# game.py
# import the draw module
from draw import draw_game


def play_game():
    return 5


def main():
    result = play_game()
    draw_game(result)


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
