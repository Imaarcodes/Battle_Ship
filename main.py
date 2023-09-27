import random


ran_int = random.randint(0,10)


rows = 16
cols = 16

GL_board = [["~" for i in  range (cols)]for j in range(rows)]
Player_board = [["~" for i in  range (cols)]for j in range(rows)]

print("    0    1    2    3    4    5    6    7    8    9    10    11    12    13    14")
for i in range (0,15):
    print(i, Player_board[i])
#only odd boats
#total of 6 boats
xinput = int(input("give me x"))
yinput = int(input("give me y"))
axis = input("L/R or U/D")



for small_coor in range(0, 15):
    #rant_int = random.randint(0, 10)
    board[xinput][yinput] = "B"

print("    0    1    2    3    4    5    6    7    8    9     10     11     12     13     14")
for i in range (0,15):
    print(i, GL_board[i])

def three_boat ():
    if axis == "U" or axis == "D" or axis == "U/D" or axis == "u" or axis == "d" or axis == "u/d" :
        Player_board[xinput][yinput] = "B"
        Player_board[xinput + 1][yinput]
        Player_board[xinput - 1][yinput]
    else:
        Player_board[xinput][yinput] = "B"
        Player_board[xinput][yinput + 1]
        Player_board[xinput][yinput - 1]

#this is the 3 boatd gl place
def three_boat_gl ():
    ran_dir = random.randint(0,1)
    xinput = random.randint(3,12)
    yinput = random.randint(3,12)

    if ran_dir == 1:
        if GL_board [xinput][yinput] == "~" and board[xinput + 1][yinput] and board[xinput - 1][yinput] == "~":
            GL_board[xinput][yinput] = "B"
            GL_board[xinput + 1][yinput] = "B"
            GL_board[xinput - 1][yinput] = "B"
    else:
        if GL_board[xinput][yinput] == "~" and board[xinput][yinput + 1] and board[xinput][yinput - 1] == "~":
            GL_board[xinput][yinput] = "B"
            GL_board[xinput][yinput + 1] = "B"
            GL_board[xinput][yinput - 1] = "B"

def print_gl_board():
    for i in range (0,15):
        print(i, board[i])



def pick_target():
    Target_X = int(input("Select a X coordinate of the target you would like to hit"))
    Target_Y = int(input("Select a Y coordinate of the target you would like to hit"))
    if board [Target_X][Target_Y] == "B":
        print("Direct Hit!")
        board [Target_X][Target_Y] = "X"
    elif board [Target_X][Target_Y] == "X" or  board [Target_X][Target_Y] == "O":
        print("You already guessed here. You loose your turn!")
    else:
        board [Target_X][Target_Y] = "O"
    print_gl_board()


def place_boats_gl():
    three_boat()
    three_boat()
    three_boat_gl()
    pick_target()
    print_gl_board()

place_boats_gl()