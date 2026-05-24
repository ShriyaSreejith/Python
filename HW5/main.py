# Name: Shriya Sreejith
# Assignment: HW5 - Game

board = [" "] * 9

def show():
    print("+---+---+---+")
    for r in range(3):
        print(f"| {board[3*r]} | {board[3*r+1]} | {board[3*r+2]} |")
        print("+---+---+---+")

def win():
    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in lines:
        if board[a] == board[b] == board[c] != " ":
            return True
    return False

def full():
    return " " not in board

player = "X"

while True:
    print("\nEnter your next move:")
    show()

    # get valid move
    while True:
        try:
            r = int(input("Row? (1-3): "))
            if r not in [1,2,3]:
                print("That's not a valid row.")
                continue
            c = int(input("Column? (1-3): "))
            if c not in [1,2,3]:
                print("That's not a valid column.")
                continue
            idx = (r-1)*3 + (c-1)
            if board[idx] != " ":
                print("That cell is already taken.")
                continue
            break
        except:
            print("Enter a number.")

    board[idx] = player
    show()

    if win():
        print("You Win!")
        break

    if full():
        print("It's a tie!")
        break

    player = "O" if player == "X" else "X"
