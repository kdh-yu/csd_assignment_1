# Battle Action

from modules.battle import is_effective
import random, time, os
from initial_setting import cl

def skill_attack(player, enemy):
    print(f"\r{player.pokemon[0].nickname} used {player.pokemon[0].elemental_attack}!")
    time.sleep(1)
    effective_multiplier = is_effective(player.pokemon[0].attribute, enemy.attribute)
    if effective_multiplier == 2:
        print("\rIt's super effective!")
        time.sleep(1)
    elif effective_multiplier == 0.5:
        print("\rIt's not very effective...")
        time.sleep(1)
    enemy.hp -= effective_multiplier * 10

def physical_attack(player, enemy):
    print(f"{player.pokemon[0].nickname} used Tackle!")
    time.sleep(1)
    enemy.hp -= 9

def hp_restore(player):
    print(f"{player.name} used Full Restore!")
    time.sleep(1)
    print(f"{player.pokemon[0].nickname}'s HP was restored.")
    time.sleep(1)
    player.pokemon[0].hp = player.pokemon[0].maxHP

def pokeball(player, enemy):
    print(f'{player.name} used the PokeBall.')
    time.sleep(1)
    if enemy.hp < 25:
        is_catched = random.choices(['success', 'fail'], weights=[0.9, 0.1])
    else:
        is_catched = random.choices(['success', 'fail'], weights=[0.15, 0.85])
    if is_catched[0] == 'success':
        print(f"Gotcha! {enemy.species} was caught!")
        time.sleep(1)
        os.system(cl())
        print(f'''
┌────────────────────┐
    {enemy.species}
└────────────────────┘
        ''')
        change_or_not = input('Will you give your pokemon a nickname? (yes / no): ')
        if change_or_not == 'yes' or change_or_not == 'y':
            nick = input(f"What is {enemy.species}\'s nickname? : ")
            enemy.nickname = nick
        gotcha = enemy
        player.pokemon.append(gotcha)
        return True
    else:
        print("Oh no! The Pokemon broke Free!")
        time.sleep(1)
        return False

def change_pokemon(player):
    if len(player.pokemon) != 1:
        ind = 1
        for i in player.pokemon:
            print(f'{ind} : {i.nickname}')
            ind += 1
        to_what = int(input('What pokemon? : '))
        if to_what == 0 or to_what < 0 or to_what > len(player.pokemon):
            pass  # Think more
        else:
            player.pokemon[0], player.pokemon[to_what - 1] = player.pokemon[to_what - 1], player.pokemon[0]
    else:
        print("You have only one Pokemon!")

def action(act, player, enemy):
    if act == 1:
        skill_attack(player, enemy)
    elif act == 2:
        physical_attack(player, enemy)
    elif act == 3:
        hp_restore(player)
    elif act == 4:
        return pokeball(player, enemy)
    elif act == 5:
        change_pokemon(player)
    else:
        physical_attack(player, enemy)

def enemy_action(player, enemy):
    eff = is_effective(enemy.attribute, player.pokemon[0].attribute)
    if eff == 0.5:
        print(f"Wild {enemy.species} used Tackle!")
        time.sleep(1)
        player.pokemon[0].hp -= 9
    else:
        print(f"Wild {enemy.species} used {enemy.elemental_attack}!")
        time.sleep(1)
        if eff == 2:
            print("\rIt's super effective!")
            time.sleep(1)
        player.pokemon[0].hp -= eff * 10