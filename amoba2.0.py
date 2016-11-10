import sys
global field
import time
import random
import string
string.ascii_letters
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'



def create_field():
    field = []
    for x in range(0,3):
        field.append(['_'] * 3)
    return field

def field_print(field):
    for i in field:
        print(' '.join(i))
    print("")


def hit1(field, characters):
    x = input("Enter in a row! (Choose one of the following number: 1, 2, 3): ")
    y = input("Enter in a column! (Choose one of the following number: 1, 2, 3): ")
    print("")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Give me a " + bcolors.WARNING + "NUMBER! " + bcolors.ENDC + " \n")
    if (x > 3 or x < 0 or y > 3 or y <0):
        print("Out of " + bcolors.FAIL + "range. " + bcolors.ENDC + " \n")
    x, y = x - 1, y - 1
    if (field[x][y] == characters[0] or field[x][y] == characters[1]):
        print("You can't mark " + bcolors.UNDERLINE + "that" + bcolors.ENDC + " spot. \n")
    field[x][y] = characters[0]


def get_winner(field, characters):
    win = False
    winner = ""
    if ((field[0][0] == characters[0] and field[0][1] == characters[0] and field[0][2] == characters[0]) or
        (field[1][0] == characters[0] and field[1][1] == characters[0] and field[1][2] == characters[0]) or
        (field[2][0] == characters[0] and field[2][1] == characters[0] and field[2][2] == characters[0]) or
        (field[0][0] == characters[0] and field[1][1] == characters[0] and field[2][2] == characters[0]) or
        (field[0][2] == characters[0] and field[1][1] == characters[0] and field[2][0] == characters[0]) or
        (field[0][0] == characters[0] and field[1][0] == characters[0] and field[2][0] == characters[0]) or
        (field[0][1] == characters[0] and field[1][1] == characters[0] and field[2][1] == characters[0]) or
        (field[0][2] == characters[0] and field[1][2] == characters[0] and field[2][2] == characters[0]) or
        (field[0][0] == characters[0] and field[1][0] == characters[0] and field[2][0] == characters[0]) or
        (field[0][1] == characters[0] and field[1][1] == characters[0] and field[2][1] == characters[0]) or
        (field[0][2] == characters[0] and field[1][2] == characters[0] and field[2][2] == characters[0])):
        win = True
        winner = characters[0]
    elif ((field[0][0] == characters[1] and field[0][1] == characters[1] and field[0][2] == characters[1]) or
        (field[1][0] == characters[1] and field[1][1] == characters[1] and field[1][2] == characters[1]) or
        (field[2][0] == characters[1] and field[2][1] == characters[1] and field[2][2] == characters[1]) or
        (field[0][0] == characters[1] and field[1][1] == characters[1] and field[2][2] == characters[1]) or
        (field[0][2] == characters[1] and field[1][1] == characters[1] and field[2][0] == characters[1]) or
        (field[0][0] == characters[1] and field[1][0] == characters[1] and field[2][0] == characters[1]) or
        (field[0][1] == characters[1] and field[1][1] == characters[1] and field[2][1] == characters[1]) or
        (field[0][2] == characters[1] and field[1][2] == characters[1] and field[2][2] == characters[1]) or
        (field[0][0] == characters[1] and field[1][0] == characters[1] and field[2][0] == characters[1]) or
        (field[0][1] == characters[1] and field[1][1] == characters[1] and field[2][1] == characters[1]) or
        (field[0][2] == characters[1] and field[1][2] == characters[1] and field[2][2] == characters[1])):
        win = True
        winner = characters[1]
    elif (field[0][0] != '_' and field[0][2] != '_' and field[2][0] != '_' and field[2][2] != '_' and
        field[0][1] != '_' and field[1][0] != '_' and field[1][1] != '_' and field[1][2] != '_' and
        field[2][1] != '_' and win == False):
        winner = "Tie."
    return winner
        
        
def welcome():
    print("Welcome to Amőba!")
    print("In this game your goal is to put 3 of your choosed character in a row or a column or a diagonal.")
    
def get_gamemode():
    gamemode = input("Choose game mode. Press 1 to singleplayer or press 2 to multiplayer: ")
    while gamemode != "1" and gamemode != "2":        
        gamemode = input("Choose 1(singleplayer) or 2(multiplayer): ")
    
    return gamemode

def get_characters(gamemode):
    characters = ["",""]
    if gamemode  == "1":
        print("You choosed singleplayer. Good luck.")
        characters[0] = input("Now first player choose a character: ")
        while len(characters[0]) != 1:
            ValueError
            characters[0] = input("Give me 1 character: ")
        print("You selected " + characters[0] + ".")
        characters[1] = random.choice(string.ascii_letters)
        while characters[1] == characters[0]:
            ValueError
            characters[1] = random.choice(string.ascii_letters)
        print(" Ai selected " + characters[1] + ".")
        characters.append(characters[0])
        characters.append(characters[1])
    elif gamemode == "2":
        print("You choosed multiplayer.")
        characters[0] = input("Now first player choose a character: ")
        while len(characters[0]) != 1:
            ValueError
            characters[0] = input("Give me 1 character: ")
        print("You selected " + characters[0] + ".")
        characters[1] = input("Now second player choose a character: ")
        while len(characters[1]) != 1:
            ValueError
            characters[1] = input("Give me 1 character: ")
        while characters[1] == characters[0]:
            ValueError
            characters[1] = input("This symbol is unavailable.Choose another character: ")
            while len(characters[1]) != 1:
                ValueError
                characters[1] = input("Give me 1 character: ")
        print("You selected " + characters[1] + ".")
        characters.append(characters[0])
        characters.append(characters[1])
    return characters

def hit_ai(field, characters):
    airow = random.randint(0,2)
    aicolumn = random.randint(0,2)
    while (field[airow][aicolumn] != '_'):
        airow = random.randint(0,2)
        aicolumn = random.randint(0,2)
    field[airow][aicolumn] = characters[1]

def hit2(field, characters):
    x = input("Enter in a row! (Choose one of the following number: 1, 2, 3): ")
    y = input("Enter in a column! (Choose one of the following number: 1, 2, 3): ")
    print("")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Give me a " + bcolors.WARNING + "NUMBER! " + bcolors.ENDC + " \n")
    if (x > 3 or x < 0 or y > 3 or y <0):
        print("Out of " + bcolors.FAIL + "range. " + bcolors.ENDC + " \n")
    x, y = x - 1, y - 1
    if (field[x][y] == characters[0] or field[x][y] == characters[1]):
        print("You can't mark " + bcolors.UNDERLINE + "that" + bcolors.ENDC + " spot. \n")
    field[x][y] = characters[1]


def run_game(gamemode, characters):
    field = create_field()
    input("Okay, lets play! Press enter to continue.")
    winner = ""
    player = 0
    field_print(field)
    while winner == "":
        print("Now turn " + characters[player] + ".\n")
        if player == 0:
            hit1(field, characters)
            player = 1
        elif player == 1 and gamemode == "1":
            hit_ai(field, characters)
            player = 0
        elif player == 1 and gamemode == "2":
            hit2 (field, characters)
            player = 0
        field_print(field)
        winner = get_winner(field, characters)
    if winner == "Tie.":
        print("Tie.")
    else:
        print("The winner is : " + winner + ".")



if __name__ == '__main__':
    welcome()
    gamemode = get_gamemode()
    chars = get_characters(gamemode)
    run_game(gamemode, chars)