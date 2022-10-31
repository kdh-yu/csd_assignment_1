from modules.battle import pokemon_encounter, move_pos
from modules.Class import Player, _Bulbasaur, _Charmander, _Squirtle
from modules.initial_setting import set_player_name, choose_pokemon, cl
from modules.ui import battle_ui, show_map, poke_appear
from modules.battle_action import change_pokemon, action, enemy_action
import time
import os

# Play game!

# Order 1
trainer_name = set_player_name()
player = Player(trainer_name)

# Order 2, 3
choose_pokemon(player)
step = 1
clear = True

# Order 4 ~
while step <= 3:
    step += 1
    encounter_pokemon = [_Charmander, _Squirtle, _Bulbasaur, None]
    for i in encounter_pokemon:
        if i != None:
            i.hp = 50

    # Order 5
    show_map(player, None)
    while True:
        direction = input("Which way? (N, E, W, S): ")
        if direction not in 'news':
            pass
        else:
            move_pos(player, direction)
            break
    
    # Order 6
    encounter = pokemon_encounter(encounter_pokemon)[0]
    if encounter == None:  # Order 6 - A
        print("No pokemon appeared.")
        time.sleep(1)
        os.system(cl())
    else:  # Order 6 - B
        os.system(cl())
        show_map(player, None)
        time.sleep(0.5)
        os.system(cl())
        show_map(player, event=True)
        time.sleep(1)
        battle_end = False
        poke_appear()
        intro_message = 0
        while True:
            
            battle_ui(player, encounter)  # Order 10

            if intro_message == 0:
                print(f"   Wild {encounter.species} appeared!", end="\r")
                time.sleep(3)
                intro_message += 1
            print("                                                     ", end='\r')
            act = int(input('What to do? : '))
            catched = action(act, player, encounter)  # Order 8

            if catched == True:
                break
            else:
                pass

            if encounter.hp <= 0:  # Order 7
                print(f'Enemy {encounter.species} fainted!')
                time.sleep(1)
                os.system(cl())
                break

            enemy_action(player, encounter)  # Order 9 (modified) : If not effective, enemy uses tackle.
            if player.pokemon[0].hp <= 0:  # Order 7
                print(f"{player.pokemon[0].nickname} has fainted!")
                player.pokemon.remove(player.pokemon[0])
                if len(player.pokemon) == 0:  # Order 7 - A
                    print("You are out of Pokemon!")
                    step = 5
                    clear = False
                    break
                else:  # Order 7 - B
                    change_pokemon(player)

if clear:  # Order 11
    time.sleep(1)
    print(f'\n{player.name} became Pokemon Master! Congratulations!!')
else:
    time.sleep(1)
    print(f'\n{player.name} blacked out!')