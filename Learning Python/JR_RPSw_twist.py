'''
jaffer razavi
nov 10 2019
rock paper scissors game
'''

import random
import time
import sys

#initializing variables
Player = ' '    # Player choice
Winct = 0       # Player Win Count
Chosen = ' '    # Computer Choice
Computer = 0    # Computer Choice Generator
ROCK = 1        # Rock's value
PAPER = 2       # Paper's value
Losect = 0      # Player Lose Count
Tiect = 0       # Player Tie COunt
Chance = 0      # Death chance (5%)
Start = ''      # Starts the game

# creates a subroutine that allows the output to print slower
def PrintSlow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
        
# creates a subroutine that allows the output to print fafter
def PrintFast(str):
    for letters in str:
        sys.stdout.write(letters)
        sys.stdout.flush()
        time.sleep(0.001)

#Intro Splash Screen
print('''
                            =======================================================================================================================================
                             .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. 
                            | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
                            | | _____  _____ | | |  _________   | | |   _____      | | |     ______   | | |     ____     | | | ____    ____ | | |  _________   | |
                            | ||_   _||_   _|| | | |_   ___  |  | | |  |_   _|     | | |   .' ___  |  | | |   .'    `.   | | ||_   \  /   _|| | | |_   ___  |  | |
                            | |  | | /\ | |  | | |   | |_  \_|  | | |    | |       | | |  / .'   \_|  | | |  /  .--.  \  | | |  |   \/   |  | | |   | |_  \_|  | |
                            | |  | |/  \| |  | | |   |  _|  _   | | |    | |   _   | | |  | |         | | |  | |    | |  | | |  | |\  /| |  | | |   |  _|  _   | |
                            | |  |   /\   |  | | |  _| |___/ |  | | |   _| |__/ |  | | |  \ `.___.'\  | | |  \  `--'  /  | | | _| |_\/_| |_ | | |  _| |___/ |  | |
                            | |  |__/  \__|  | | | |_________|  | | |  |________|  | | |   `._____.'  | | |   `.____.'   | | ||_____||_____|| | | |_________|  | |
                            | |              | | |              | | |              | | |              | | |              | | |              | | |              | |
                            | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
                             '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' 
                            =======================================================================================================================================
''',end = '',)
PrintFast('''
                            Welcome!  This program will simulate a game of rock, paper, scissors.  You will be asked to type either "rock", "paper" or "scissors".
                            You can type "exit" for the game to end.  

                            NOTE: Please make the window fullscreen!


                            Another note, there is a 25% chance that you will die on starting the game...

                            You're gonna have a bad time.
                            
''')
print('''
                            =======================================================================================================================================
''')
# Waits for the user to read the welcome screen
time.sleep(2)

PrintFast('Press enter to start')
Start = input('')

# This allows the death chance to only happen at start
Chance = random.randint(1,10)

if Chance == 3:
    print('''
                                                                    ░░░░░░░░░░░░░░░░██████████████████░░░░░░░░░░░░░░░░░
                                                                    ░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░
                                                                    ░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░
                                                                    ░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░
                                                                    ░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░
                                                                    ░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██████░░░░██░░░░░░░░░
                                                                    ░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██████░░░░██░░░░░░░░░
                                                                    ░░░░░░░░██░░░░██████░░░░██░░░░██████░░░░██░░░░░░░░░
                                                                    ░░░░░░░░░░██░░░░░░░░░░██████░░░░░░░░░░██░░░░░░░░░░░
                                                                    ░░░░░░░░████░░██░░░░░░░░░░░░░░░░░░██░░████░░░░░░░░░
                                                                    ░░░░░░░░██░░░░██████████████████████░░░░██░░░░░░░░░
                                                                    ░░░░░░░░██░░░░░░██░░██░░██░░██░░██░░░░░░██░░░░░░░░░
                                                                    ░░░░░░░░░░████░░░░██████████████░░░░████░░░░░░░░░░░
                                                                    ░░░░░░░░██████████░░░░░░░░░░░░░░██████████░░░░░░░░░
                                                                    ░░░░░░██░░██████████████████████████████░░██░░░░░░░
                                                                    ░░░░████░░██░░░░██░░░░░░██░░░░░░██░░░░██░░████░░░░░
                                                                    ░░░░██░░░░░░██░░░░██████░░██████░░░░██░░░░░░██░░░░░
                                                                    ░░██░░░░████░░██████░░░░██░░░░██████░░████░░░░██░░░
                                                                    ░░██░░░░░░░░██░░░░██░░░░░░░░░░██░░░░██░░░░░░░░██░░░
                                                                    ░░██░░░░░░░░░░██░░██░░░░░░░░░░██░░██░░░░░░░░░░██░░░
                                                                    ░░░░██░░░░░░██░░░░████░░░░░░████░░░░██░░░░░░██░░░░░
                                                                    ░░░░░░████░░██░░░░██░░░░░░░░░░██░░░░██░░████░░░░░░░
                                                                    ░░░░░░░░██████░░░░██████████████░░░░██████░░░░░░░░░
                                                                    ░░░░░░░░░░████░░░░██████████████░░░░████░░░░░░░░░░░
                                                                    ░░░░░░░░██████████████████████████████████░░░░░░░░░
                                                                    ░░░░░░░░████████████████░░████████████████░░░░░░░░░
                                                                    ░░░░░░░░░░████████████░░░░░░████████████░░░░░░░░░░░
                                                                    ░░░░░░██████░░░░░░░░██░░░░░░██░░░░░░░░██████░░░░░░░
                                                                    ░░░░░░██░░░░░░░░░░████░░░░░░████░░░░░░░░░░██░░░░░░░
                                                                    ░░░░░░░░██████████░░░░░░░░░░░░░░██████████░░░░░░░░░
                                                                        ===========================================
                                                                         __  ______  __  __  ___  ___________    __
                                                                         \ \/ / __ \/ / / / / _ \/  _/ __/ _ \  / /
                                                                          \  / /_/ / /_/ / / // // // _// // / /_/ 
                                                                          /_/\____/\____/ /____/___/___/____/ (_)  
                                                                        ===========================================
''')
    quit()
else:

     #Rock Paper Scissors game code
    while Player != "exit":
        PrintFast("Rock, Paper, or Scissors? \n")
        Player = input("")
        Player = Player.lower()
        PrintSlow("Computer's turn ... \n")
        #make player choice lowercase 
        Computer = random.randint(1,3)
        # Determines computer choice
        if Computer == ROCK:
            Chosen = 'rock'
        elif Computer == PAPER:
            Chosen = 'paper'
        else:
            Chosen = 'scissors'
        #deciding outcomes
        #tie outcome
        if Player == Chosen:
            print('Computer chooses',Chosen)
            print('''
                                                                                ==========================
                                                                                      __________________
                                                                                     /_  __/  _/ ____/ /
                                                                                      / /  / // __/ / / 
                                                                                     / / _/ // /___/_/  
                                                                                    /_/ /___/_____(_)
                                                                                ==========================
''')
            #Adds 1 to the tie count
            Tiect = Tiect + 1 
        #player wins
        elif Player == 'rock' and Chosen == 'scissors':
            PrintFast('Computer chooses scissors')
            print('''
                                                ==================================================================================================
                                                    ____  ____  ________ __    _    _______         _____ ____________________ ____  ____  _____
                                                   / __ \/ __ \/ ____/ //_/   | |  / / ___/        / ___// ____/  _/ ___/ ___// __ \/ __ \/ ___/
                                                  / /_/ / / / / /   / ,<      | | / /\__ \         \__ \/ /    / / \__ \\__ \/ / / / /_/ /\__ \ 
                                                 / _, _/ /_/ / /___/ /| |     | |/ /___/ /  _     ___/ / /____/ / ___/ /__/ / /_/ / _, _/___/ / 
                                                /_/ |_|\____/\____/_/ |_|     |___//____/  (_)   /____/\____/___//____/____/\____/_/ |_|/____/  
                                                                                                                                                
                                                    ____  __    _____  ____________     _       _______   _______    __
                                                   / __ \/ /   /   \ \/ / ____/ __ \   | |     / /  _/ | / / ___/   / /
                                                  / /_/ / /   / /| |\  / __/ / /_/ /   | | /| / // //  |/ /\__ \   / / 
                                                 / ____/ /___/ ___ |/ / /___/ _, _/    | |/ |/ // // /|  /___/ /  /_/  
                                                /_/   /_____/_/  |_/_/_____/_/ |_|     |__/|__/___/_/ |_//____/  (_)
                                                ==================================================================================================
''')
            #add 1 to win count
            Winct = Winct + 1
            
        #computer wins
        elif Player == 'rock' and Chosen == 'paper':
            PrintFast('Computer chooses paper')
            print('''
                                                =============================================================================================
                                                    ____  ____  ________ __    _    _______         ____  ___    ____  __________  
                                                   / __ \/ __ \/ ____/ //_/   | |  / / ___/        / __ \/   |  / __ \/ ____/ __ \      
                                                  / /_/ / / / / /   / ,<      | | / /\__ \        / /_/ / /| | / /_/ / __/ / /_/ /          
                                                 / _, _/ /_/ / /___/ /| |     | |/ /___/ /  _    / ____/ ___ |/ ____/ /___/ _, _/         
                                                /_/ |_|\____/\____/_/ |_|     |___//____/  (_)  /_/   /_/  |_/_/   /_____/_/ |_|           
                                                                                                                                  
                                                   __________  __  _______  __  __________________     _       _______   _______    __
                                                  / ____/ __ \/  |/  / __ \/ / / /_  __/ ____/ __ \   | |     / /  _/ | / / ___/   / /
                                                 / /   / / / / /|_/ / /_/ / / / / / / / __/ / /_/ /   | | /| / // //  |/ /\__ \   / / 
                                                / /___/ /_/ / /  / / ____/ /_/ / / / / /___/ _, _/    | |/ |/ // // /|  /___/ /  /_/  
                                                \____/\____/_/  /_/_/    \____/ /_/ /_____/_/ |_|     |__/|__/___/_/ |_//____/  (_)
                                                =============================================================================================
''')
            #add 1 to lose count
            Losect = Losect + 1
            
        #player wins
        elif Player == 'paper' and Chosen == 'rock':
            PrintFast('Computer chooses rock')
            print('''
                                                ======================================================================================
                                                    ____  ___    ____  __________     _    _______         ____  ____  ________ __
                                                   / __ \/   |  / __ \/ ____/ __ \   | |  / / ___/        / __ \/ __ \/ ____/ //_/
                                                  / /_/ / /| | / /_/ / __/ / /_/ /   | | / /\__ \        / /_/ / / / / /   / ,<   
                                                 / ____/ ___ |/ ____/ /___/ _, _/    | |/ /___/ /  _    / _, _/ /_/ / /___/ /| |  
                                                /_/   /_/  |_/_/   /_____/_/ |_|     |___//____/  (_)  /_/ |_|\____/\____/_/ |_|  
                                                                                                                                  
                                                    ____  __    _____  ____________     _       _______   _______    __
                                                   / __ \/ /   /   \ \/ / ____/ __ \   | |     / /  _/ | / / ___/   / /
                                                  / /_/ / /   / /| |\  / __/ / /_/ /   | | /| / // //  |/ /\__ \   / / 
                                                 / ____/ /___/ ___ |/ / /___/ _, _/    | |/ |/ // // /|  /___/ /  /_/  
                                                /_/   /_____/_/  |_/_/_____/_/ |_|     |__/|__/___/_/ |_//____/  (_)
                                                ======================================================================================
                                                                               
''')
            #add 1 to win count
            Winct = Winct + 1
            
        #computer wins
        elif Player == 'paper' and Chosen == 'scissors':
            PrintFast('Computer chooses scissors')
            print('''
                                            ========================================================================================================
                                                ____  ___    ____  __________     _    _______         _____ ____________________ ____  ____  _____
                                               / __ \/   |  / __ \/ ____/ __ \   | |  / / ___/        / ___// ____/  _/ ___/ ___// __ \/ __ \/ ___/
                                              / /_/ / /| | / /_/ / __/ / /_/ /   | | / /\__ \         \__ \/ /    / / \__ \\__ \/ / / / /_/ /\__ \ 
                                             / ____/ ___ |/ ____/ /___/ _, _/    | |/ /___/ /  _     ___/ / /____/ / ___/ /__/ / /_/ / _, _/___/ / 
                                            /_/   /_/  |_/_/   /_____/_/ |_|     |___//____/  (_)   /____/\____/___//____/____/\____/_/ |_|/____/  
                                                                                                                                                   
                                               __________  __  _______  __  __________________     _       _______   _______    __
                                              / ____/ __ \/  |/  / __ \/ / / /_  __/ ____/ __ \   | |     / /  _/ | / / ___/   / /
                                             / /   / / / / /|_/ / /_/ / / / / / / / __/ / /_/ /   | | /| / // //  |/ /\__ \   / / 
                                            / /___/ /_/ / /  / / ____/ /_/ / / / / /___/ _, _/    | |/ |/ // // /|  /___/ /  /_/  
                                            \____/\____/_/  /_/_/    \____/ /_/ /_____/_/ |_|     |__/|__/___/_/ |_//____/  (_)
                                            ========================================================================================================
                                                                                              
''')
            #add 1 to lose count
            Losect = Losect + 1

        #player wins
        elif Player == 'scissors' and Chosen == 'paper':
            PrintFast('Computer chooses paper')
            print('''
                                            ========================================================================================================
                                               _____ ____________________ ____  ____  _____    _    _______         ____  ___    ____  __________ 
                                              / ___// ____/  _/ ___/ ___// __ \/ __ \/ ___/   | |  / / ___/        / __ \/   |  / __ \/ ____/ __ \ 
                                              \__ \/ /    / / \__ \\__ \/ / / / /_/ /\__ \    | | / /\__ \        / /_/ / /| | / /_/ / __/ / /_/ / 
                                             ___/ / /____/ / ___/ /__/ / /_/ / _, _/___/ /    | |/ /___/ /  _    / ____/ ___ |/ ____/ /___/ _, _/  
                                            /____/\____/___//____/____/\____/_/ |_|/____/     |___//____/  (_)  /_/   /_/  |_/_/   /_____/_/ |_|   
                                                                                                                                                
                                                ____  __    _____  ____________     _       _______   _______    __
                                               / __ \/ /   /   \ \/ / ____/ __ \   | |     / /  _/ | / / ___/   / /
                                              / /_/ / /   / /| |\  / __/ / /_/ /   | | /| / // //  |/ /\__ \   / / 
                                             / ____/ /___/ ___ |/ / /___/ _, _/    | |/ |/ // // /|  /___/ /  /_/  
                                            /_/   /_____/_/  |_/_/_____/_/ |_|     |__/|__/___/_/ |_//____/  (_)
                                            ========================================================================================================
                                                                               
''')
            #add 1 to win count
            Winct = Winct + 1

        #computer wins
        elif Player == 'scissors' and Chosen == 'rock':
            PrintFast('Computer chooses rock')
            print('''
                                                ===================================================================================================
                                                   _____ ____________________ ____  ____  _____    _    _______         ____  ____  ________ __
                                                  / ___// ____/  _/ ___/ ___// __ \/ __ \/ ___/   | |  / / ___/        / __ \/ __ \/ ____/ //_/
                                                  \__ \/ /    / / \__ \\__ \/ / / / /_/ /\__ \    | | / /\__ \        / /_/ / / / / /   / ,<   
                                                 ___/ / /____/ / ___/ /__/ / /_/ / _, _/___/ /    | |/ /___/ /  _    / _, _/ /_/ / /___/ /| |  
                                                /____/\____/___//____/____/\____/_/ |_|/____/     |___//____/  (_)  /_/ |_|\____/\____/_/ |_|  
                                                                                                                                               
                                                   __________  __  _______  __  __________________     _       _______   _______    __
                                                  / ____/ __ \/  |/  / __ \/ / / /_  __/ ____/ __ \   | |     / /  _/ | / / ___/   / /
                                                 / /   / / / / /|_/ / /_/ / / / / / / / __/ / /_/ /   | | /| / // //  |/ /\__ \   / / 
                                                / /___/ /_/ / /  / / ____/ /_/ / / / / /___/ _, _/    | |/ |/ // // /|  /___/ /  /_/  
                                                \____/\____/_/  /_/_/    \____/ /_/ /_____/_/ |_|     |__/|__/___/_/ |_//____/  (_)
                                                ===================================================================================================
                                                                                                                                      
''')
            #add 1 to lose count
            Losect = Losect + 1
        #invalid entry
        elif Player != 'exit':
            PrintFast('''
Invalid Entry.
Try again...
''')
        #Partial Twist - the computer gets angry
        if (Winct > 2) and (Losect < Winct):
            PrintFast('''
THATS ENOUGH!
YOU WERE SUPPOSED TO LOSE!!

p l a y e r   h a s   d i e d
''')
            #kills the program/quits it
            exit()
        
        
        #Score Chart
        PrintFast('{0:2}{1:2}{2:2}{3:5}{4:2}{5:3}{6:2}{7:5}'.format('Your Score: \n',
                                                                '-----------',
                                                                '\n Wins:', Winct, 
                                                                '\n Losses:', Losect,
                                                                '\n Ties:', Tiect))
        print('\n')
    # play count
    print("You played",Losect + Tiect + Winct,"times")

    # final outcomes
    # tied war

    if (Winct == Losect):
        print("""
                                                =================================================================================================
                                                __  ______  __  __   ____________________     ________  ________   _       _____    ____     __
                                                \ \/ / __ \/ / / /  /_  __/  _/ ____/ __ \   /_  __/ / / / ____/  | |     / /   |  / __ \   / /
                                                 \  / / / / / / /    / /  / // __/ / / / /    / / / /_/ / __/     | | /| / / /| | / /_/ /  / / 
                                                 / / /_/ / /_/ /    / / _/ // /___/ /_/ /    / / / __  / /___     | |/ |/ / ___ |/ _, _/  /_/  
                                                /_/\____/\____/    /_/ /___/_____/_____/    /_/ /_/ /_/_____/     |__/|__/_/  |_/_/ |_|  (_)
                                                =================================================================================================
                                                                                                   
    """)

        # player wins war
    elif (Winct > Losect):
        print("""
                                                =================================================================================================
                                                __  ______  __  __   _       ______  _   __   ________  ________   _       _____    ____     __
                                                \ \/ / __ \/ / / /  | |     / / __ \/ | / /  /_  __/ / / / ____/  | |     / /   |  / __ \   / /
                                                 \  / / / / / / /   | | /| / / / / /  |/ /    / / / /_/ / __/     | | /| / / /| | / /_/ /  / / 
                                                 / / /_/ / /_/ /    | |/ |/ / /_/ / /|  /    / / / __  / /___     | |/ |/ / ___ |/ _, _/  /_/  
                                                /_/\____/\____/     |__/|__/\____/_/ |_/    /_/ /_/ /_/_____/     |__/|__/_/  |_/_/ |_|  (_)
                                                =================================================================================================
                                                                                            
    """)
        # player loses war
    else:
        print("""
                                                =================================================================================================
                                                __  ______  __  __   __    ____  ___________   ________  ________   _       _____    ____     __
                                                \ \/ / __ \/ / / /  / /   / __ \/ ___/_  __/  /_  __/ / / / ____/  | |     / /   |  / __ \   / /
                                                 \  / / / / / / /  / /   / / / /\__ \ / /      / / / /_/ / __/     | | /| / / /| | / /_/ /  / / 
                                                 / / /_/ / /_/ /  / /___/ /_/ /___/ // /      / / / __  / /___     | |/ |/ / ___ |/ _, _/  /_/  
                                                /_/\____/\____/  /_____/\____//____//_/      /_/ /_/ /_/_____/     |__/|__/_/  |_/_/ |_|  (_)
                                                =================================================================================================
                                                                                                
    """)

    # ending splash screen
    print("""
                                            ============================================================================================================
                                              ________  _____    _   ____ _______    __________  ____     ____  __    _____  _______   ________   __
                                             /_  __/ / / /   |  / | / / //_/ ___/   / ____/ __ \/ __ \   / __ \/ /   /   \ \/ /  _/ | / / ____/  / /
                                              / / / /_/ / /| | /  |/ / ,<  \__ \   / /_  / / / / /_/ /  / /_/ / /   / /| |\  // //  |/ / / __   / / 
                                             / / / __  / ___ |/ /|  / /| |___/ /  / __/ / /_/ / _, _/  / ____/ /___/ ___ |/ // // /|  / /_/ /  /_/  
                                            /_/ /_/ /_/_/  |_/_/ |_/_/ |_/____/  /_/    \____/_/ |_|  /_/   /_____/_/  |_/_/___/_/ |_/\____/  (_)   
                                            ============================================================================================================
    """)














