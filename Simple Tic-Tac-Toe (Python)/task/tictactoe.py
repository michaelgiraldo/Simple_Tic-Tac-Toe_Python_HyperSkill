def format_board(tt):
    return [' ' if c not in ['X', 'O'] else c for c in tt]


def print_board(tt):
    print("---------")
    for i in range(0, 9, 3):
        print("|", tt[i], tt[i + 1], tt[i + 2], "|")
    print("---------")


def update_board(tt, x, y, player):
    tt[3 * (x - 1) + (y - 1)] = player
    return tt


def input_board_coordinate(tt):
    while True:
        try:
            x, y = map(int, input().split())
            if 1 <= x <= 3 and 1 <= y <= 3:
                if tt[3 * (x - 1) + (y - 1)] == " ":
                    return x, y
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")


def check_board(tt):
    win = 0
    winner = ""

    # Check Horizontal
    for i in range(0, 9, 3):
        if tt[i] == tt[i + 1] == tt[i + 2] != ' ':
            winner = tt[i]
            win += 1

    # Check Vertical
    for i in range(3):
        if tt[i] == tt[i + 3] == tt[i + 6] != ' ':
            winner = tt[i]
            win += 1

    # Check Diagonals
    if tt[0] == tt[4] == tt[8] != ' ' or tt[2] == tt[4] == tt[6] != ' ':
        winner = tt[4]
        win += 1

    # Check for impossible state, win condition, draw condition, and ongoing game
    count_x = tt.count("X")
    count_o = tt.count("O")

    # impossible state
    if win > 1 or abs(count_x - count_o) > 1:
        return "Impossible"
    # win condition, draw condition, and ongoing game
    if win == 1:
        return f"{winner} wins"
    elif ' ' not in tt:
        return "Draw"
    return "Game not finished"


def main():
    tt = [' '] * 9
    print_board(tt)

    current_player = 'X'
    while True:
        x, y = input_board_coordinate(tt)
        tt = update_board(tt, x, y, current_player)
        print_board(tt)
        result = check_board(tt)

        if result in ['Draw', 'X wins', 'O wins', 'Impossible']:
            print(result)
            break
        else:
            print("Game not finished")
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()
