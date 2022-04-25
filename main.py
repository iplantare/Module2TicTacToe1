row1 = [1, 2, 3] 
row2 = [4,5,6]
row3 = [7,8,9]

def learning():    
    print(row1)

    print(row2)

    print(row3)

def hello():
    keep_playing = True 
    player = 0
    while keep_playing == True:
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
        
            player += 1
            learning()
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

            player += 1       
            learning()


def main():
    learning()
    hello()

main()

def next_step():
    pass