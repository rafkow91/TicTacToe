#Kolko_i_krzyzyk

def displayBoard(board):
    i = 0
    for i in range (3):
        print("-"*13+"\n| "+ str(board[i * 3])+" | " + str(board[i * 3 + 1])+" | " + str(board[i * 3 + 2])+" | ")
        i = i + 1
    print("-"*13)

def enterMove(board):
    while True:
        a = int(input("Podaj nr pola, ktore chcesz zajac:\t"))
        if type(board[a-1]) == int:
            board[a-1] = "O"
            break
        else:
            print("Podales zly nr pola")    
#main program
tablica = [1,2,3,"x",5,6,7,8,9]
displayBoard(tablica)
enterMove(tablica)
displayBoard(tablica)