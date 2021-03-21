#John Nguyen
#Dnd dice roller/ TTRPG dice roller
#possibly integrating it as a discord bot
#Possibly thinking of making different modes or different TTRPG

import random
#Got this from www.pythonforbeginners.com/code-snippets-source-code/game-rolling-the-dice
#A basic guide to making a dice simulator game
import math
#Learned in clas, basically  just imports the library of functions like math.ceil and math.sqrt


print("Project made by","John Nguyen", sep =" ")
print("jdnguyen1381", end = "@")
print("eagle.fgcu.edu")
print("Project Started: ", end = " ")
print("2","6","2021", sep = "-")
print("Project Checkpoint: ", end = " ")
print("3", "20", "2021", sep = "-")
#sep= puts a space inbetween the two strings
#end= makes it so the line below it will output into one like with what was put in the quotations.

print("-"*100)
# *80 multiplies the text inside the quote 80 times.

#def random_int_roller() makes makes random_int_roller() into a function for me to call in another program.


def random_int_roller(user_input):
    rolling = random.randint(1,user_input)
    #random.randint(1,user_input) makes it so it rolls a number between 1 and the inputted number
    print("You Rolled", rolling)
    return rolling


def damage_phase():
    try:
        damage_roll = int(input("Enter damage dice"))
        damage_dealt = random.randint(1,damage_roll)
        print(damage_dealt)
    except:
        damage_phase()
    damage_modifiers = int(input("Input Damage Modifiers: "))
    critical_input = input("Did you get a critical? (Yes/No) \n*Case sensitive* \nInput: ")


    if critical_input == "Yes" or critical_input == "yes":
        critical_damage = int(damage_dealt * 2)
        total_damage = (critical_damage + damage_modifiers)
        print("Your total damage is: ", total_damage)
    elif critical_input == "No" or critical_input == "no":
        total_damage = (damage_dealt + damage_modifiers)
        print("Your total damage is: ", total_damage)
    else:
        print("Invalid Response. No Double Damage")
        total_damage = (damage_dealt + damage_modifiers)
        print("Your total damage is: ", total_damage)

    #Couldn't get this to work for now
    #if accuracy_roll == 20 :
    #    critical_damage = (damage1 *2)
    #    total_damage = (critical_damage + damage_modifiers)
    #    print("Your total damage is:  ", total_damage)
    #else:
    #    total_damage = (damage1 + damage_modifiers)
    #    print("Your total damage is: ", total_damage)

    weakness_input = input("Do they resist your damage type or are you using their weakness against them? \n Input(resist/weakness/Enter(if neutral) \nInput: ")
    if weakness_input == "resist" or weakness_input == "Resist":
    #These lines of code basically makes it so either it halves or doubles damage or does nothing.
        weakness_total_damage = math.ceil(total_damage / 2)
        print("Your total damage is", weakness_total_damage)

    elif weakness_input == "weakness" or weakness_input == "Weakness":
        weakness_total_damage = math.ceil(total_damage * 2)
        print("Your total damage is", weakness_total_damage)

    else:
        print("Your total damage is", total_damage)


def standard_dnd_process():
    accuracy = input("Press Enter to roll for accuracy")
    #accuracy_roll = random.randint(1, 20)
    accuracy_roll = random_int_roller(20)
    print(accuracy_roll)
    if accuracy_roll == 20:
        print("Critical Hit!")
    elif accuracy_roll == 1:
        print("Critical Failure!")
    else:
        pass

    #accuracy_mods = int(input("Any modifiers for accuracy?: "))
    try:
        accuracy_mods = int(input("Any modifiers for accuracy?: "))
    except:
        accuracy_mods = 0

    #accuracyMods = int(accuracyMods)
    #This is to make sure the accuracy numbers don't go higher than 20 or below 1
    total_accuracy = (accuracy_roll + accuracy_mods)
    if total_accuracy > 20:
        total_accuracy = 20
    elif total_accuracy < 1:
        total_accuracy = 1
    else:
        pass
    print(total_accuracy)

#MENU STUB HACKERRANK CAME IN HANDY
#basically the main function where everything breaks out from.
def main():
    continue_program = True
    while continue_program:
        print("Enter the choice for what you want to do")
        print("1. The standard DND turn process")
        print("2. A dice roller")
        print("3. (Undecided)")
        print("4. Break/Finish")
        user_input_menu = input()
# if statements allow for conditions to happen and tell the computer what to do.
        if user_input_menu == "1":
            standard_dnd_process()
            print("-" * 80)
            print("DAMAGE PHASE")
            damage_phase()

        elif user_input_menu == "2":
            continue_choice2 = True
            #Loops the statements indented until continue_program2 is set to False
            while continue_choice2:
                #TRY EXCEPT HACKERRANK CAME IN HANDY
                #Try and Except makes it tests the inputted variable.
                #rolling_accuracy = int(input("Enter the amount of sides you want to roll"))
                try:
                    rolling_accuracy = int(input("Enter the amount of sides you want to roll \nIf you want to stop, Press Enter \nInput: "))
                    random_int_roller(rolling_accuracy)
                except:
                    print("Terminated")
                    continue_choice2 = False
                #if rolling_accuracy == int()
                #random_int_roller(rolling_accuracy)

        elif user_input_menu == "3":
            print("Currently Nothing Yet")
            print("I think I'll use this as links to rules or as as some spell lists")

        elif user_input_menu =="4":
            print("Program Terminated")
            continue_program = False
        #Stops the program from running


main()

#All in all, There a lot of things I can improve on and will continue to work on it.
#Problem#1: Can't figure out how to call variable from one function to another without it bugging out
#Problem#2: I think the naming scheme could be better
#Problem#3: I have to implement an advantage and disadvantage system
#Still need to think of more options to add
#Possibly adding links for rules or links for DND spells.