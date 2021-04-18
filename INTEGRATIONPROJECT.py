"""Integration Project For COP 1500. This is a DnD Dice roller/TTRPG dice
roller."""
import random
import math

__author__ = "John Nguyen"

print("Project made by", "John Nguyen")
print("jdnguyen1381", end="@")
print("eagle.fgcu.edu")
print("Project Started: ", end=" ")
print("2", "6", "2021", sep="-")
print("Project Checkpoint: ", end=" ")
print("3", "20", "2021", sep="-")

print("-" * 100)


# -----------------------------------------------------------------------------

def random_int_roller(user_input):
    """This function rolls a number between 1 and the number(user_input)

    :param user_input: It is the number put in random.randint(1, user_input)
    :return: Returns the number rolled by the function.
    """
    rolling = random.randint(1, user_input)
    # makes it so it rolls a number between 1 and the inputted number
    return rolling


# -----------------------------------------------------------------------------


def choice_2_chosen_dice_roller():
    """This function is a loop that will allow you to roll from 1 to random
    number until it is stopped either by pressing Enter or inputting any
    other value.
    """
    continue_choice2 = True
    while continue_choice2:
        # Loops the statements indented until continue_program2 is set to False
        # TRY EXCEPT HACKERRANK CAME IN HANDY
        # Try and Except makes it tests the inputted variable.
        try:
            dice2_rolling = int(input(
                "Enter the amount of sides you want to roll "
                "\nIf you want to stop, Press Enter"
                "\nThe function will terminate if any other value than a "
                "positive integer is inputted"
                "\nInput: "))
            dice2_result = random_int_roller(dice2_rolling)
            print("You rolled", dice2_result)
        except ValueError:
            print("Terminated")
            continue_choice2 = False
        # Terminates the function is anything else is inputted


# -----------------------------------------------------------------------------


def standard_dnd_process():
    """
This function just runs the "standard process" of a DnD turn.
    """
    rolled_int = []
    try:
        rolled_int_input = int(input("Enter the amount of "
                                     "times you want to roll"
                                     "\nPress Enter or anything else if you "
                                     "want to exit"
                                     "\ninput: "))
        if rolled_int_input >= 1:
            for x in range(0, rolled_int_input):
                accuracy_roll = random_int_roller(20)
                rolled_int.append(accuracy_roll)
            # print("You Rolled", accuracy_roll)
            print(rolled_int)
            dis_advantage_check = input(
                "Do you have (Advantage/Disadvantage), if neither press "
                "ENTER: ")
            if dis_advantage_check == "Advantage":
                accuracy_rolled = max(rolled_int)
                critical_check(accuracy_rolled)
                print("Your highest roll was", accuracy_rolled)
            elif dis_advantage_check == "Disadvantage":
                accuracy_rolled = min(rolled_int)
                critical_check(accuracy_rolled)
                print("Your lowest rolled was", accuracy_rolled)
            else:
                accuracy_rolled = rolled_int[0]
                critical_check(accuracy_rolled)
                print("You rolled", accuracy_rolled)
            # return accuracy_rolled
            damage_phase()

        elif rolled_int_input < 0:
            print("Invalid Input. Please input a positive number")
            standard_dnd_process()

    except ValueError:
        print("Terminated")
        main()
    # Terminates the function if anything else is inputted.

# When you input the amount of times you want to roll it puts the numbers
# into a list for which it can be called by boolean functions. Advantage
# means that it'll take the largest number in the list. Disadvantage means
# that it'll take the lowest number. Inputting anything else would give the
# user the first number in the list.

# -----------------------------------------------------------------------------


def damage_phase():
    """
This is the damage portion of the "standard" DnD turn
    """
    damage_dealt = None
    try:
        damage_roll = int(input("Enter damage dice: "))
        damage_dealt = random.randint(1, damage_roll)
        damage_dealt = int(damage_dealt)
        print(damage_dealt)
    except ValueError:
        damage_phase()

    try:
        damage_modifiers = int(input("Input Damage Modifiers: "))
    except ValueError:
        damage_modifiers = 0

    critical_input = input("Did you get a critical? (Yes/No) "
                           "\nInput: ")

    if critical_input == "Yes" or critical_input == "yes":
        critical_damage = int(damage_dealt * 2)
        total_damage = (critical_damage + damage_modifiers)
        print("Your total damage is: ", total_damage)

    elif critical_input == "No" or critical_input == "no":
        total_damage = (damage_dealt + damage_modifiers)
        print("Your total damage is: ", total_damage)

    else:
        print("Continuing")
        total_damage = (damage_dealt + damage_modifiers)
        print("Your total damage is: ", total_damage)

    weakness_input = input(
        "Do they resist your damage type or are you using their weakness "
        "against them? "
        "\n Input(resist/weakness/Enter(if neutral) "
        "\nInput: ")

    if weakness_input == "resist" or weakness_input == "Resist":
        weakness_total_damage = math.ceil(total_damage / 2)
        print("Your total damage is", weakness_total_damage)

    elif weakness_input == "weakness" or weakness_input == "Weakness":
        weakness_total_damage = math.ceil(total_damage * 2)
        print("Your total damage is", weakness_total_damage)

    else:
        print("Your total damage is", total_damage)

# This function rolls for the damage dealt and asks two things, if they have
# critical and weakness. Critical either doubles your damage dealt or it
# keeps it the same. While weakness either doubles damage, halves damage,
# or keeps it the same.


#   --------------------------------------------------------------------------


def critical_check(check_critical):
    """
Checks if you rolled either a 20 or a 1 naturally. It will print Critical
Hit or Critical Failure respectively.
    :param check_critical: The number that was rolled will be passed in to
     check.
    """
    if check_critical == 20:
        print("Critical Hit!")
    elif check_critical == 1:
        print("Critical Failure!")
    else:
        pass


# ----------------------------------------------------------------------------

def choice_3_chosen_checks():
    """This function essentially makes it so you have to beat the number
    inputted.
    In DnD, the monster would have you do a check in which you
    have to roll higher than the number the monster has. When you roll you
    get the base roll plus any modifiers that your character has.

    """
    input("Press Enter to start")
    program_3_continue = True
    while program_3_continue:
        try:
            opponent_check = int(input("Enter the amount you need to beat ("
                                       "input a number between 1 and 20): "))
            if opponent_check < 1 or opponent_check > 20:
                raise ValueError
            # If the number is outside of the range given it will go to the
            # exception part.
            else:
                input("Press Enter to Roll ")
                user_check = random_int_roller(20)
                print("You rolled", user_check)
                try:
                    check_modifier = int(input("Input Modifiers: "))
                except ValueError:
                    check_modifier = 0

                total_user_check = int(user_check + check_modifier)
                print(user_check + check_modifier)

                if total_user_check > opponent_check:
                    print("You passed the check")
                elif not (total_user_check > opponent_check):
                    print("You failed the check")
                program_3_continue = False

        except ValueError:
            print("Invalid Input. Please put a number between 1 and 20")


# ----------------------------------------------------------------------------
def choice_4_unused():
    """
This function essentially is used for operators or requirements that didn't
fit in the the main program.
    """
    continue_function_4 = True
    while continue_function_4:
        print("Enter the choice you want to see")
        print("1. Inverted Triangle (range function)")
        print("2. Numeric Operators Samples")
        print("3. Terminate function")
        user_input_function4 = input("Input: ")
        if user_input_function4 == "1":
            inverted_triangle()
        if user_input_function4 == "2":
            numeric_operators()
        if user_input_function4 == "3":
            continue_function_4 = False
        else:
            print("Invalid Input")


# -----------------------------------------------------------------------------
def numeric_operators():
    """
This function is for unused operators and shows examples of how they are used.
    """
    print("Which operator would you like to see?")
    print("1. Modulus (%) ")
    print("2. Floor Division (//) ")
    print("3. Exponent (**) ")
    user_input_no = input("Input: ")
    if user_input_no == "1":
        print("The modulus function is used to return the remainder after "
              "dividing.")
        print("Example: 7 % 3 = 1")
        print("3 goes into 7 two times which leaves a 1 as the remainder")
    if user_input_no == "2":
        print("The floor division function is used to get the integer of a "
              "division.")
        print("Example: 7 // 3 =  2")
        print("Normally it would output 2.33 but with floor division it "
              "rounds down to the nearest whole number. In this case it is 2.")
    if user_input_no == "3":
        print("The exponent function is used to multiply a number by its "
              "exponent.")
        print("Example: 4 ** 3 = 64")
        print("4 is multiplied by itself 3 times.")
    else:
        numeric_operators()


# -----------------------------------------------------------------------------

def inverted_triangle():
    """
Creates an inverted triangle.
    """
    try:
        user_input = int(input("How many rows? (Please input a positive "
                               "number)"
                               "\nIf you want to exit input anything else"
                               "\nInput: "))
        if user_input > 0:
            user_input += 1
            for column in range(1, user_input):
                for user_input in range(1, user_input):
                    print(user_input, end=" ")
                print()
            else:
                inverted_triangle()
    except ValueError:
        print("Terminated")
# This function creates an inverted triangle. This is caused by the "for
# column in range(1,user_input): and the "for user_input in range(1,
# user_input". These combined with the accumulator is what causes the
# triangle to become inverted.


# ----------------------------------------------------------------------------

def main():
    """
A menu stub that will allow you to open up other functions.
    """
    continue_program_main = True
    while continue_program_main:
        print("Enter the choice for what you want to do "
              "\nExample: you would input 1 for the first option")
        print("1. The standard DND turn process")
        print("2. A dice roller")
        print("3. Checks")
        print("4. Unused requirements in main program")
        print("5. Break/Finish")
        user_input_menu = input()
        if user_input_menu == "1":
            # if statements allow for conditions to happen
            standard_dnd_process()

        elif user_input_menu == "2":
            choice_2_chosen_dice_roller()

        elif user_input_menu == "3":
            choice_3_chosen_checks()

        elif user_input_menu == "4":
            choice_4_unused()

        elif user_input_menu == "5":
            print("Goodbye. Thank you for using my program")
            continue_program_main = False

        else:
            print("Not a valid input")
# This is, metaphorically, the trunk of a tree. The main function is where
# the program starts off and branches off into other functions. Using the
# menu stub hackerrank. This allows for the numerical choices to go to
# different functions.


# -----------------------------------------------------------------------------

if __name__ == '__main__':
    main()
