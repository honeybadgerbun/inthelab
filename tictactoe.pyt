board = [
    ["| |","| |","| |"],
    ["| |","| |","| |"],
    ["| |","| |","| |"]
]

gameboard = {
board[2][0]:"C1",board[2][1]:"C2",board[2][2]:"C3",
board[1][0]:"B1",board[1][1]:"B2",board[1][2]:"B3",
board[0][0]:"A1",board[0][1]:"A2",board[0][2]:"A3"}

print("This is  a game of TicTacToe.\nYou're opponent will make a move and then you will.\nEvery space is labeled A1-A3,B1-B3,C1-C3.\nFirst to get 3 of their sign in a row wins!")

for index in range(len(board)):
    print(board[index][0:3])