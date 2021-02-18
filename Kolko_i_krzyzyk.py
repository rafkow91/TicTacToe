#Kolko_i_krzyzyk

def displayBoard(board):
    i = 0
    j = 0
    for i in range (3):
        print("-"*13+"\n| "+ str(board[i * 3])+" | " + str(board[i * 3 + 1])+" | " + str(board[i * 3 + 2])+" | ")
        i = i + 1
    print("-"*13+"\n| ")

tablica = [1,2,3,4,5,6,7,8,9]
displayBoard(tablica)