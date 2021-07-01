from math import log, sqrt
from random import randrange
from time import sleep


board = ["000000000", "000000000"]

wins = [
    "100100100",  # 1st column
    "010010010",  # 2nd column
    "001001001",  # 3rd column
    "111000000",  # 1st row
    "000111000",  # 2nd row
    "000000111",  # 3rd row
    "100010001",  # 1st diagonal
    "001010100",  # 2nd diagonal
]

squares = [
    "100000000",
    "010000000",
    "001000000",
    "000100000",
    "000010000",
    "000001000",
    "000000100",
    "000000010",
    "000000001",
]

side = 0


def winner(board: list) -> int:
    for i in range(len(wins)):
        if not int(board[0], 2) & int(wins[i], 2) ^ int(wins[i], 2):
            return 1
        elif not int(board[1], 2) & int(wins[i], 2) ^ int(wins[i], 2):
            return -1
    return 0


def change_side(side: int):
    return side ^ 1


def list_to_str(list_: list) -> str:
    str_ = ""
    for i in list_:
        str_ += i
    return str_


def empty(board: list, square: int, side: int) -> bool:
    if board[side][square] == "1":
        return False
    elif board[side ^ 1][square] == "1":
        return False
    return True


def make_move(board: list, square: int, side: int) -> str:
    if empty(board, square, side):
        magic = list(board[side])
        if side:
            magic[square] = "1"
        else:
            magic[square] = "1"
        board[side] = list_to_str(magic)
    return board


def print_board(board: list):
    for i in range(9):
        if not i % 3 and i != 0:
            print()
        if board[0][i] == "0" and board[1][i] == "0":
            print(" - ", end="")
        elif board[0][i] == "0" and board[1][i] == "1":
            print(" O ", end="")
        else:
            print(" X ", end="")
    print()


def thinking():
    while True:
        t = "Thinking"
        print(t)
        sleep(0.5)
        for i in range(3):
            t += "."
            sleep(0.5)


def legal_moves(board: list) -> list:
    legal_moves = []
    for i in range(9):
        if int(board[0][i]) or int(board[1][i]):
            continue
        legal_moves.append(i)
    return legal_moves


def uct(scores: list, visits: list, iterations: int) -> list:
    c = sqrt(2)
    ucb = []
    x = 0
    for i in scores:
        s = (float(scores[x]) / float(visits[x])) + \
            c * sqrt(log(iterations) / float(visits[x]))
        ucb.append(s)
        x += 1
    return ucb


def get_move_index(legal_moves: list, move: float) -> int:
    c = 0
    for i in legal_moves:
        if i == move:
            return c
        c += 1
    return -1


def random_choice(board: list, legal_moves: list) -> int:
    choice = randrange(len(legal_moves))
    return legal_moves[choice]


def is_game_over(board: list) -> bool:
    if len(legal_moves(board)) == 0 or winner(board) != 0:
        return True
    return False


def rollout(board: list, side: int, selected: int) -> int:
    c = True
    side_ = side
    while not is_game_over(board):
        if c:
            board = make_move(board, selected, side_)
            side_ = change_side(side_)
            c = False
            continue

        legal_moves_ = legal_moves(board)
        move_ = random_choice(board, legal_moves_)
        board = make_move(board, move_, side_)
        side_ = change_side(side_)
    return winner(board)


def mcts(board: list, side: int, iterations: int):
    board_ = board[:]
    legal_moves_ = legal_moves(board_)
    ucb = []
    selected = 0.
    visits = [1 for i in range(len(legal_moves_))]
    scores = [0. for i in range(len(legal_moves_))]

    for i in range(iterations):
        ucb = uct(scores, visits, i+1)
        selected = max(ucb)
        index = get_move_index(ucb, selected)

        board = board_[:]
        winner = rollout(board, side, legal_moves_[index])

        visits[index] += 1
        scores[index] += winner
    """
    print(scores)
    print(visits)
    print(ucb)
    """
    print("Score: " + str(round(scores[get_move_index(ucb, selected)] /
                                visits[get_move_index(ucb, selected)], 2)))

    return legal_moves_[get_move_index(ucb, selected)]


while not is_game_over(board):
    print_board(board)

    # cpu
    cpu_move = mcts(board, side, 1000)
    print("Computer move: " + str(cpu_move) + "\n")
    board = make_move(board, cpu_move, side)

    if is_game_over(board):
        break

    print_board(board)
    side = change_side(side)

    # human
    user_move = input("Your move: ")
    print()
    board = make_move(board, int(user_move), side)

    side = change_side(side)

print_board(board)

result = winner(board)
if result == 1:
    result = "CPU wins"
elif result == -1:
    result = "User wins"
else:
    result = "Tie"

print("Result: " + result)

input()
