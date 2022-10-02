board = [
    ["|a|","|b|","|c|"],
    ["|d|","|e|","|g|"],
    ["|f|","|h|","|i|"]
]

gameboard = {
board[2][0]:"C1",board[2][1]:"C2",board[2][2]:"C3",
board[1][0]:"B1",board[1][1]:"B2",board[1][2]:"B3",
board[0][0]:"A1",board[0][1]:"A2",board[0][2]:"A3"}

print("This is  a game of TicTacToe.\nYou're opponent will make a move and then you will.\nEvery space is labeled A1-A3,B1-B3,C1-C3.\nFirst to get 3 of their sign in a row wins!")

first = 0
second = 0

for i in range(9):
    print(board[first][second],end="")
    if i == 2 or i == 5 or i == 9:
        print("")
    if second != 2:
        second += 1 
    elif second == 2:
        second = 0
        first += 1
    