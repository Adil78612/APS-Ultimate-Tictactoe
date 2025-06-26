import random
import pygame





#___________________________________________________________________________________________________________________#
#pygame initialization
pygame.init()
window_size = 600
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Tic Tac Toe")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
#___________________________________________________________________________________________________________________#





#___________________________________________________________________________________________________________________#
#draws the gui for the entire game
def draw_board_gui(main_lst):

    cell_size = window_size // 10

    for i in range(11):
        for j in range(11):

            
            pygame.draw.rect(window, WHITE, (j * cell_size, i * cell_size, cell_size, cell_size), 2)
            font = pygame.font.Font(None, 24) 

            if i > 0 and j > 0:  

                if i < 10 and j < 10:

                    grid_i = (i - 1) // 3
                    grid_j = (j - 1) // 3
                    cell_i = (i - 1) % 3
                    cell_j = (j - 1) % 3
                    grid_value = main_lst[grid_i * 3 + grid_j]
                    cell_value = grid_value[cell_i * 3 + cell_j]

                    if grid_i == 0 and grid_j == 0 and cell_value == ' ':
                        small_num = (cell_i * 3 + cell_j)
                        text = font.render('a' + str(small_num), True, WHITE)
                        window.blit(text, (j * cell_size + cell_size - 25, i * cell_size + cell_size - 25))

                    elif grid_i == 0 and grid_j == 1 and cell_value == ' ':
                        small_num = (cell_i * 3 + cell_j)
                        text = font.render('b' + str(small_num), True, WHITE)
                        window.blit(text, (j * cell_size + cell_size - 25, i * cell_size + cell_size - 25))

                    elif grid_i == 0 and grid_j == 2 and cell_value == ' ':
                        small_num = (cell_i * 3 + cell_j)
                        text = font.render('c' + str(small_num), True, WHITE)
                        window.blit(text, (j * cell_size + cell_size - 25, i * cell_size + cell_size - 25))

                    elif grid_i == 1 and grid_j == 0 and cell_value == ' ':
                        small_num = (cell_i * 3 + cell_j)
                        text = font.render('d' + str(small_num), True, WHITE)
                        window.blit(text, (j * cell_size + cell_size - 25, i * cell_size + cell_size - 25))

                    elif grid_i == 1 and grid_j == 1 and cell_value == ' ':
                        small_num = (cell_i * 3 + cell_j)
                        text = font.render('e' + str(small_num), True, WHITE)
                        window.blit(text, (j * cell_size + cell_size - 25, i * cell_size + cell_size - 25))

                    elif grid_i == 1 and grid_j == 2 and cell_value == ' ':
                        small_num = (cell_i * 3 + cell_j)
                        text = font.render('f' + str(small_num), True, WHITE)
                        window.blit(text, (j * cell_size + cell_size - 25, i * cell_size + cell_size - 25))

                    elif grid_i == 2 and grid_j == 0 and cell_value == ' ':
                        small_num = (cell_i * 3 + cell_j)
                        text = font.render('g' + str(small_num), True, WHITE)
                        window.blit(text, (j * cell_size + cell_size - 25, i * cell_size + cell_size - 25))

                    elif grid_i == 2 and grid_j == 1 and cell_value == ' ':
                        small_num = (cell_i * 3 + cell_j)
                        text = font.render('h' + str(small_num), True, WHITE)
                        window.blit(text, (j * cell_size + cell_size - 25, i * cell_size + cell_size - 25))

                    elif grid_i == 2 and grid_j == 2 and cell_value == ' ':
                        small_num = (cell_i * 3 + cell_j)
                        text = font.render('i' + str(small_num), True, WHITE)
                        window.blit(text, (j * cell_size + cell_size - 25, i * cell_size + cell_size - 25))
                        
                    else:
                        text = font.render(str(cell_value), True, RED)
                        window.blit(text, (j * cell_size + cell_size // 2 - 15, i * cell_size + cell_size // 2 - 15))


    pygame.display.flip()
#___________________________________________________________________________________________________________________#





#___________________________________________________________________________________________________________________#
#converts turn into a readible format
def decipher_turn(turn):

    grids = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
    grid = grids[turn[0]]
    num = int(turn[1])

    return grid, num
#___________________________________________________________________________________________________________________#





#___________________________________________________________________________________________________________________#
#draws board on the terminal
def DrawBoard(main_lst):
    for i in range(9):

        if i % 3 == 0 and i != 0:

            print(" " + "_____" * 8)

        for j in range(9):

            if j % 3 == 0 and j != 0:

                print("|", end=" ")

            value = main_lst[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
            print(f" {value} ", end = "")
        print()
    print()
#___________________________________________________________________________________________________________________#





#___________________________________________________________________________________________________________________#
#checks turn validity
def turn_check(turn, won_local_games, last_move):

    if len(turn) == 2 and turn[0] in "abcdefghi" and turn[1] in "012345678":
        deciphered_turn = decipher_turn(turn)
        grid = deciphered_turn[0]

        if last_move is None or last_move[1] == grid:

            if not won_local_games[grid]:
                return True
            
            else:
                print(f"Local game {grid} is already won. Choose a different local game.")
                return False
            
        else:

            encoder = "abcdefghi"
            print(f"You must play in grid {encoder[last_move[1]]}. Choose a different local game.")
            return False
        
    else:
        print("Invalid input. Please enter a valid turn.")
        return False
#___________________________________________________________________________________________________________________#





#___________________________________________________________________________________________________________________#
#takes inputs conducts checks and adjusts list accordingly
def turn_play(player, main_lst, won_local_games, last_move):

    global p1, p2
    temp_lst = main_lst.copy()

    turnv = False
    

    while not turnv:

        if last_move != None:
       
            if won_local_games[last_move[1]]:
                available_grids = [i for i, won in enumerate(won_local_games) if not won]
                grid = random.choice(available_grids)
                print(f"Since grid {last_move[1]} is won, randomly choosing new grid {grid}.")
                last_move = (last_move[0], grid)


        if player == 1:
            turn = input(f"{p1} please enter your turn (e.g a1, c3, d5....): ")
        else:
            turn = input(f"{p2} please enter your turn (e.g a1, c3, d5....): ")
        turnv = turn_check(turn, won_local_games, last_move)
        if turnv:

            
            deciphered_turn = decipher_turn(turn)
            if temp_lst[deciphered_turn[0]][deciphered_turn[1]] != " ":
                turnv = False
                print("This spot is already taken, try again!")

            else:
                temp_lst[deciphered_turn[0]][deciphered_turn[1]] = "X" if player == 1 else "O"
                last_move = deciphered_turn

       

    return temp_lst, last_move
#___________________________________________________________________________________________________________________#





#___________________________________________________________________________________________________________________#
#make a local check to see if a local game has been won
def local_check(main_lst, global_lst, won_local_games):

    global p1,p2
    temp_lst = global_lst.copy()
    for num,i in enumerate(main_lst):

        if won_local_games[num] == False:


            if (i[0] == i[4] == i[8] == "X") or (i[0] == i[3] == i[6] == "X") or (i[0] == i[1] == i[2] == "X") or (i[1] == i[4] == i[7] == "X") or (i[3] == i[4] == i[5] == "X") or (i[6] == i[7] == i[8] == "X") or (i[2] == i[5] == i[8] == "X") or (i[2] == i[4] == i[6] == "X"):

                temp_lst[num] = "X"
                won_local_games[num] = True
                encoder = "abcdefghi"
                print(f"Congrats {p1}, you won grid {encoder[num]}")

            elif (i[0] == i[4] == i[8] == "O") or (i[0] == i[3] == i[6] == "O") or (i[0] == i[1] == i[2] == "O") or (i[1] == i[4] == i[7] == "O") or (i[3] == i[4] == i[5] == "O") or (i[6] == i[7] == i[8] == "O") or (i[2] == i[5] == i[8] == "O") or (i[2] == i[4] == i[6] == "O"):

                temp_lst[num] = "O"
                won_local_games[num] = True
                encoder = "abcdefghi"
                print(f"Congrats {p2}! You won grid {encoder[num]}")


    return temp_lst, won_local_games
#___________________________________________________________________________________________________________________#





#___________________________________________________________________________________________________________________#
#make a global check to see if the global game has been won
def global_check(i):
    winner = "running"  
    is_tie = True

    
    if (i[0] == i[4] == i[8] == "X") or (i[0] == i[3] == i[6] == "X") or (i[0] == i[1] == i[2] == "X") or (i[1] == i[4] == i[7] == "X") or (i[3] == i[4] == i[5] == "X") or (i[6] == i[7] == i[8] == "X") or (i[2] == i[5] == i[8] == "X") or (i[2] == i[4] == i[6] == "X"):
            winner = "p1"
            is_tie = False
            

    elif (i[0] == i[4] == i[8] == "O") or (i[0] == i[3] == i[6] == "O") or (i[0] == i[1] == i[2] == "O") or (i[1] == i[4] == i[7] == "O") or (i[3] == i[4] == i[5] == "O") or (i[6] == i[7] == i[8] == "O") or (i[2] == i[5] == i[8] == "O") or (i[2] == i[4] == i[6] == "O"):
            winner = "p2"
            is_tie = False
            
        
    if " " in i:
            is_tie = False

    if is_tie:
        winner = "tie"

    return winner
#___________________________________________________________________________________________________________________#





#ask for names

p1 = input("Player 1 enter your name: ")
p2 = input("Player 2 enter your name: ")
gamestate = "running"
won_local_games = [False, False, False, False, False, False, False, False, False]
#this stores all the moves either X or 0
main_lst = [[" ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " "]]
global_lst = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
#random generation for turn
player = random.randrange(1, 3)
last_move = None






#INITIAL STATE
while gamestate == "running":

    #checks for events in the pygame event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit() 
    
    #draws boards in terminal and gui
    draw_board_gui(main_lst)
    DrawBoard(main_lst)
    
    main_lst, last_move = turn_play(player, main_lst, won_local_games, last_move)
    global_lst, won_local_games = local_check(main_lst, global_lst, won_local_games)
    gamestate = global_check(global_lst)
   
    if gamestate == "p1":
        print(f"Jokes on you {p2}, {p1} wins")
    elif gamestate == "p2":
        print(f"Jokes on you {p1}, {p2} wins") 
    elif gamestate == "tie":
        print("It's a tie!")

    player = 3 - player







  














   


