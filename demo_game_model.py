import numpy as np

board = np.zeros((6,7))

print(board)
def is_wins(empty_list):
    global flag
    #horizontal check:
    for i in range(0,4):
        if empty_list[0+i][0] == empty_list[0+i][1] == empty_list[0+i][2] == empty_list[0+i][3] and empty_list[0+i][0] != 0 :
            if empty_list[0+i][0] == 1 :
                print("player one wins")
                return False
                
            elif empty_list[0+i][0] == 2 :
                print("player two wins")
                
                return False
                
            
    #vertical check:  
    for j in range(0,4):
        if empty_list[0][0+j] == empty_list[1][0+j] == empty_list[2][0+j] == empty_list[3][0+j] and empty_list[0][0+j] != 0 :
            if empty_list[0][0+j] == 1 :
                print("player one wins")
                
                return False
                
            elif empty_list[0][0+j] == 2 :
                print("player two wins")
                return False
                
    #diagonal check:
    if empty_list[0][0] == empty_list[1][1] == empty_list[2][2] == empty_list[3][3] and empty_list[0][0] != 0 :
        if empty_list[0][0] == 1 :
            print("player one wins")
            return False
            
        elif empty_list[0][0] == 2 :
            print("player two wins")
            return False
            
    if empty_list[0][3] == empty_list[1][2] == empty_list[2][1] == empty_list[3][0] and empty_list[0][3] != 0 :
        if empty_list[0][3] == 1 :
            print("player one wins")
            return False
            
        elif empty_list[0][3] == 2 :
            print("player two wins")
            return False

    
            
def check_win(board):
    empty_list = []
    for k in range(0,4):
        for j in range(0,3):
            for i in range(0,4):
                empty_list.append(list(board[0+i+j][0+k:4+k]))
                #print(empty_list)

            is_wins(empty_list)
            empty_list.clear()
    


#a = int(input("Enter the number 0-6: "))
#board[5][a] = 1
#print(board)
turn = 0
flag = True
while flag:
    if turn % 2 == 0:
        a = int(input("Enter the number 0-6: "))
        if board[0][a] == 0:
            for i in range(5,-1,-1):
                if board[i][a] == 0:
                    board[i][a] = 1
                    check_win(board)
                    turn += 1
                    break
            
            print(board)

        else:
            print("Please enter valid input")
    if turn %2 != 0:
        b = int(input("Enter the number 0-6: "))
        if board[0][b] == 0:
            for i in range(5,-1,-1):
                if board[i][b] == 0:
                    board[i][b] = 2
                    check_win(board)
                    turn += 1
                    break
            
            print(board)
        else:
            print("Please enter valid input")