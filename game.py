'''
Sequence Guessing Game
Version 1.0
Developer : Surabhi Ojha 
Rules:
The player has to guess the next number of a already existing sequence
First 10 numbers will be displayed of every sequence
After the player has guessed the sequence numbers correctly, a new sequence is displayed
This game is a basic implementation of AI
This game never ends
The level number,level score and game total is diplayed after every round and is stored in a text file as well
'''

import series                             #for series
import os                                 #for clear scree
import time
from random import choice
from series import series_return_function
from series import series_description_return_function


def firstsampleseries():
    unused_variable = os.system("cls") # on windows
    print("This is the demo of how this game works.")
    print("You have to guess the next number of series.")
    print("The series changes to a new series after a number of moves.")
    print("-----You Can Never Win This Game------")
    print("-----------Name of series will be displayed after every round-----------")
    print("******************************************************************************")
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    le = len(l)
    for i in range(6):
        print(l[i],end=" ")
    print(" ")
    print("Guess the next numbers of the series")
    f = 0
    for i in range(6,le):
        print("Guess Next Number----------")
        
        t = int(input())
         

        if t == l[i]:
            print("Correct Guess")
            print(" ")
        else:
            f = 1
            print("Wrong Guess")
            break
    print("*********************************************************************************")
    print("------------------------Moving to original game--------------------")
   
    time.sleep(2)
    unused_variable = os.system("cls") # on windows
    
#######################################################################################################################3

def the_real_game():  
    game_series_random_list = [i for i in range(0,20)]
    level_number = 1 #level _number
    game_total = 0 #Game total
    player="" #player name
    print("Enter The Player Name")
    player = input()
    file = open('mark.txt','a') 
    file.write("************************************************************************************************* \n")
    file.write("THE GAME DETAILS \n") 
    file.write("Player Name = ")
    file.write(player)
    file.write("\n")
    #infinite loop
    while True:
        #variables declaration
        series_list = [] 
        level_point = 0
        series_description = ""
        temp = 0
        random_series_list = game_series_random_list #making the random list equal to initial game random list

        #random function
        selection = choice(random_series_list) #storing random value in selection
        random_series_list.remove(selection) #deleting the selected value from list so that series doesn't repeat

        if(len(random_series_list)==0):
            random_series_list = game_series_random_list
    
        #print(selection)
        
        #series based on random number
        series_list = series_return_function(selection) #function of series file
        series_description = series_description_return_function(selection) #series description return
        #series_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        le = len(series_list)

        print("*******************************************************************************************************")
        print("-----------------------------------------------------------------------------------------------------")
        print("*********The Integer Sequence Game***********")
        print("Level Number = ",end=" ")
        print(level_number)
        print("--------------------------------------------------------------------------------------------------------")
        for i in range(10):
            print(series_list[i],end=" ")
        print(" ")
        print("Guess the next numbers of the series")
        f = 0 #flag
        for i in range(10,le):
            print("Guess Next Number----------")
            
            temp = int(input())
            if temp == series_list[i]:
                print("Correct Guess")
                print(" ")
                level_point = level_point + level_number
            else:
                f = 1
                print("------------------------------You lost-----You can never win this game---------------------------------")
                break
                
        
        print("-----------------------------------Level Detail----------------------------------------------------")
        print("Level_point = ",end=" ")
        print(level_point)
        print("The Given Series is Called : ",end=" ")
        print(series_description)

        #file write
        file.write("------------------------------------------------------- \n")
        file.write("Level Number = ") 
        file.write(str(level_number))
        file.write("\n")
        file.write("Level point = ")
        file.write(str(level_point))
        file.write("\n")
        
        
        if f==0:
            level_number = level_number + 1
            game_total = game_total + level_point
            print("Total game point = ",end=" ")
            print(game_total)
            #file write
            file.write("Game Total = ")  
            file.write(str(game_total))
            file.write("\n")
            print("----------------------------------Moving to next level---------------------------------------------")
        elif f==1:
            print("Total game point = ",end=" ")
            print(game_total)
            #file write
            file.write("Game Total = ")  
            file.write(str(game_total))
            file.write("\n")
            print("----------------------------------Closing The Game---------------------------------------------")
            break
        
        
        print("*********************************************************************************************************")
        
        #clear screen
        time.sleep(6)
        unused_variable = os.system("cls") # on windows
    file.write("********************************************************************************\n\n\n")    
    file.close()

    
    
   
##############################################################################################################################
print("Do you want to see the demo?  Enter")
print("1 for Yes")
print("2 for No")
n = int(input())
if n == 1:
    firstsampleseries()
the_real_game()



        

