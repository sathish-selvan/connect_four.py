import numpy as np
import pygame 
import sys
import math
pygame.init()
SQUAARESIZE = 100
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
RADIUS = int(SQUAARESIZE/2 - 5)
width = 7 * 100
height = 7 *100
size = (width,height)
screen = pygame.display.set_mode(size)
board = np.zeros((6,7))
myfont = pygame.font.SysFont("monospace",72)

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
    else:
        return True



def check_win(board):
    empty_list = []
    for k in range(0,4):
        for j in range(0,3):
            for i in range(0,4):
                empty_list.append(list(board[0+i+j][0+k:4+k]))
                #print(empty_list)

            if is_wins(empty_list)==False:
                return "end"
            else:
                empty_list.clear()

            # print(empty_list)
            # a = input()
def draw_board(board):
    
    for i in range(7):
        for j in range(6):
            pygame.draw.rect(screen , BLUE ,(i*SQUAARESIZE,j*SQUAARESIZE+SQUAARESIZE,SQUAARESIZE, SQUAARESIZE))
            if board[j][i] ==0:
                pygame.draw.circle(screen, BLACK,(int(i*SQUAARESIZE+SQUAARESIZE/2),int(j*SQUAARESIZE+SQUAARESIZE+SQUAARESIZE/2)), RADIUS)
            elif board[j][i] == 1:
                pygame.draw.circle(screen, RED,(int(i*SQUAARESIZE+SQUAARESIZE/2),int(j*SQUAARESIZE+SQUAARESIZE+SQUAARESIZE/2)), RADIUS) 
            elif board[j][i] == 2:
                pygame.draw.circle(screen, GREEN,(int(i*SQUAARESIZE+SQUAARESIZE/2),int(j*SQUAARESIZE+SQUAARESIZE+SQUAARESIZE/2)), RADIUS)   
    pygame.display.update()
draw_board(board)

turn = 0
flag = True

def main_loop(flag,turn,board):
    print(board)
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK,(0,0,width,SQUAARESIZE))

                posx = event.pos[0]
                if turn % 2 == 0 :
                    pygame.draw.circle(screen,RED,(posx ,int(SQUAARESIZE/2)),RADIUS)
                else:
                    pygame.draw.circle(screen,GREEN,(posx ,int(SQUAARESIZE/2)),RADIUS)
            pygame.display.update()



            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                posx = event.pos[0]
                if turn % 2 == 0:
                    a = int(math.floor(posx/SQUAARESIZE))
                    if board[0][a] == 0:
                        for i in range(5,-1,-1):
                            if board[i][a] == 0:
                                board[i][a] = 1
                                print(board)
                                draw_board(board)
                                result = check_win(board)
                                if result == "end":
                                    pygame.draw.rect(screen,BLACK,(0,0,width,SQUAARESIZE))
                                    lable = myfont.render("Player 1 WINS",1,RED)
                                    screen.blit(lable,(40,10))
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                                    board = np.zeros((6,7))
                                    draw_board(board)
                                    main_loop(True,0,board)
                                turn += 1
                                break

                    else:
                        print("Please enter valid input")
                else:
                    b = int(math.floor(posx/SQUAARESIZE))
                    if board[0][b] == 0:
                        for i in range(5,-1,-1):
                            if board[i][b] == 0:
                                board[i][b] = 2
                                print(board)
                                draw_board(board)
                                result = check_win(board)
                                if result == "end":
                                    pygame.draw.rect(screen,BLACK,(0,0,width,SQUAARESIZE))
                                    lable = myfont.render("Player 2 WINS",1,GREEN)
                                    screen.blit(lable,(40,10))
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                                    board = np.zeros((6,7))
                                    draw_board(board)
                                    main_loop(True,0,board)
                                turn += 1
                                break

                        
                    else:
                        print("Please enter valid input")

main_loop(flag,turn,board)
