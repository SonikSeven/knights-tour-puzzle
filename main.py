from field import Field
import copy


def main():
    while True:
        try:
            x, y = (int(n) for n in input("Enter your board dimensions: ").split())
            field = Field(x, y)
            break
        except ValueError:
            print("Invalid dimensions!")
    while True:
        try:
            x, y = (int(n) for n in input("Enter the knight's starting position: ").split())
            field[x, y] = "X"
            break
        except (ValueError, IndexError):
            print("Invalid position!")
    while True:
        choice = input("Do you want to try the puzzle? (y/n): ").lower()
        if choice == "y":
            solution = find_solution(field, x, y)
            return print(move(field, x, y) if solution else "No solution exists!")
        elif choice == "n":
            solution = find_solution(field, x, y)
            return print(f"\nHere's the solution!\n{solution}" if solution else "No solution exists!")
        else:
            print("Invalid input!")


def move(field, x, y, counter=1):
    valid_moves = {}
    field[x, y] = "X"
    warnsdorff(field, valid_moves, x, y)
    del valid_moves[x, y]
    for i, n in valid_moves.items():
        field[i] = n
    print(field)
    field[x, y] = "*"
    for i in valid_moves:
        del field[i]

    if counter == field.length:
        return "What a great tour! Congratulations!"
    if not valid_moves:
        return f"No more possible moves!\nYour knight visited {counter} squares!"
    while True:
        try:
            x, y = (int(n) for n in input("Enter your next move: ").split())
            assert (x, y) in valid_moves
            return move(field, x, y, counter + 1)
        except (ValueError, AssertionError):
            print("Invalid move! ", end="")


def warnsdorff(field, valid_moves, x, y, depth=0):
    if depth > 1:
        return 1
    counter = 0
    for a, b in (1, 2), (2, 1), (-1, -2), (-2, -1), (-1, 2), (2, -1), (1, -2), (-2, 1):
        a, b = a + x, b + y
        if 0 < a <= field.width and 0 < b <= field.height and not field[a, b]:
            counter += warnsdorff(field, valid_moves, a, b, depth + 1)
    valid_moves[x, y] = counter
    return 1


def find_solution(field, x, y, depth=1):
    field[x, y] = depth
    if depth == field.length:
        return field
    valid_moves = {}
    warnsdorff(field, valid_moves, x, y)
    del valid_moves[x, y]
    for i, n in sorted(valid_moves.items(), key=lambda a: a[1]):
        result = find_solution(copy.copy(field), *i, depth + 1)
        if result:
            return result
    return False


if __name__ == "__main__":
    main()
