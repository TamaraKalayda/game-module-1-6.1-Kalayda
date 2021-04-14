field = [[" "] * 3 for i in range(3)]
def show():
    print("  0 1 2")
    for i in range(3):
        rows = " ".join(field[i])
        print(f"{i} {rows}")

def play():
    while True:
        moves = input("Для Вашего хода введите две координаты через пробел:").split()

        if len(moves) != 2:
            print("Ведите две координаты")
            continue

        x, y = moves
        x, y = int(x), int(y)

        if any([0 > x, x > 2, 0 > y, y > 2]):
            print("Нет таких координат")
            continue

        if field[x][y] != " ":
            print("Данная клетка уже занята. Выберите другую")
            continue

        return x, y

def win():
    winner = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for moves in winner:
        symbols = []
        for c in moves:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграли 'крестики'")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграли 'нолики'")
            return True
    return False

print("Первая введенная цифра - это номер строки, вторая - столбца")
count = 0
while True:
    count += 1

    show()

    if count % 2 == 1:
        print("Ход 'крестика'")
    else:
        print("Ход 'нолика'")

    x, y = play()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if count == 9:
        print("Игра окончена. Ничья")
        break





