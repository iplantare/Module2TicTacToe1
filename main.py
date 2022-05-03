# This is the first draft
#comment
row1 = [1,2,3] 
row2 = [4,5,6]
row3 = [7,8,9]


def print_board():    
    print(row1)

    print(row2)

    print(row3)

def hello():
    keep_playing = True 
    player = 0
    winner = False

    while keep_playing == True and winner == False:
        # Handle turn of player one
        if player % 2 == 0:
            player1 = int(input("X's turn to choose "))
            for num in row1:
                if num == player1:
                    row1[num - 1] = "x"
            for num in row2: 
                if num == player1:
                    row2[num - 4] = "x"
            for num in row3:
                if num == player1:
                    row3[num - 7] = "x"
        
            # Same as player =  player + 1
            player += 1

            print_board()
        # handle turn of player 2
        elif player % 2 == 1:
            player2 = int(input("O's turn to choose "))
            for num in row1:
                if num == player2:
                    row1[num - 1] = "o"
            for num in row2:
                if num == player2:
                    row2[num -4] = "o"
            for num in row3:
                if num == player2:
                    row3[num - 7] = "o"

            # Same as player = player + 1
            player += 1       
            print_board()


        # Check if there is a winner
        
        if row1[0] == row1[1] and row1[1] == row1[2]:
            winner = True
        if row2[0] == row2[1] and row2[1] == row2[2]:
            winner = True
        if row3[0] == row3[1] and row3[1] == row3[2]:
            winner = True
        if row1[0] == row2[0] and row2[0] == row3[0]:
            winner = True
        if row1[1] == row2[1] and row2[1] == row3[1]:
            winner = True
        if row1[2] == row2[2] and row2[2] == row3[2]:
            winner = True
        if row1[0] == row2[1] and row2[1] == row3[2]:
            winner = True
        if row1[2] == row2[1] and row2[1] == row3[0]:
            winner = True 
        

        
          
    # if there has been 9 turns and there is not a winner then: 
        if player >= 9 and winner != True:
          print("There is not a winner. Cat!")

        # row1 = [1,2,3] 
        # row2 = [4,5,6]
        # row3 = [7,8,9]
        if winner == True:
            print("winner")

def main():
    print_board()
    hello()

main()

def next_step():
    pass

