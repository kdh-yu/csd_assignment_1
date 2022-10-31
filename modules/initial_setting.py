# Initial Settings
from modules.Class import Charmander, Squirtle, Bulbasaur
import time, os

def set_player_name():
    os.system('clear')
    name = input('What is your name? : ')
    print(f'Oh, {name}... What a good name!')
    return name

def choose_pokemon(player):
    time.sleep(1)
    print("I'll give you a pokemon for a partner.")
    time.sleep(0.5)
    print('''
    1. Charmander
    2. Squirtle
    3. Bulbasaur\n''')
    time.sleep(1)
    while True:
        chosen_pokemon = int(input("What pokemon do you want? : "))

        if chosen_pokemon not in [1, 2, 3]:
            pass
        else:
            if chosen_pokemon == 1:
                player.pokemon_add(Charmander)
            elif chosen_pokemon == 2:
                player.pokemon_add(Squirtle)
            elif chosen_pokemon == 3:
                player.pokemon_add(Bulbasaur)
            break
    
    print(f"You recieved {player.pokemon[0].species}!")
    time.sleep(1)
    nickname_change_or_not = input("Will you give your pokemon a nickname? (yes / no)\n: ")

    if nickname_change_or_not == 'yes' or nickname_change_or_not == 'y':
        nickname = input(f'What is {player.pokemon[0].species}\'s nickname? : ')
        player.pokemon[0].set_nickname(nickname)
    else:
        pass
    
    print(f"A world of dreams and adventures with Pokemon awaits! Let's Go!")
    time.sleep(2)
    os.system('clear')