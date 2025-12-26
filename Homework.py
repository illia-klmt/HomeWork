print("Игра Крестики-нолики")  # Приветствие
first_player = input("Введите имя первого игрока (Крестики): ")  # Имя первого игрока
second_player = input("Введите имя второго игрока (Нолики): ")  # Имя второго игрока

players = [first_player, second_player] # Список игроков
symbols = ['X', 'O']  # Символы для игроков
current_player = 0 # Индекс текущего игрока

game_board = [['-' for _ in range(3)] for _ in range(3)] # Создаем пустое игровое поле 3x3

def print_game_board(game_board):      # Функция для печати игрового поля
    print('  0 1 2')
    for i, row in enumerate(game_board):
        print(i, ' '.join(row), end='\n')

def get_valid_number(prompt):
    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Ошибка: нужно ввести число.")
            continue

        value = int(value)

        if value < 0 or value > 2:
            print("Ошибка: число должно быть от 0 до 2.")
            continue

        return value

def make_move(player, symbol):  # Функция для выполнения хода
    while True:
        row = get_valid_number(f"Игрок {player}, введите строку (0-2): ")
        col = get_valid_number(f"Игрок {player}, введите столбец (0-2): ")
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Некорректный ввод. Попробуйте снова.")
            continue
        if game_board[row][col] == '-':
            game_board[row][col] = symbol
            break
        else:
            print("Эта клетка уже занята. Попробуйте снова.")

def check_winner(board):
    # Диагонали
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return True

    # Строки и столбцы
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return True

    return False

def check_draw(board):
    for row in board:
        if '-' in row:
            return False
    return True

while True:
    print_game_board(game_board)

    make_move(players[current_player], symbols[current_player])

    if check_winner(game_board):
        print_game_board(game_board)
        print(f"Победил игрок {players[current_player]}!")
        break

    if check_draw(game_board):
        print_game_board(game_board)
        print("Ничья!")
        break

    current_player = 1 - current_player

