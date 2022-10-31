# UI

from modules.battle import hp_bar
import time
import os
from modules.initial_setting import cl

def name_displayer(name):
    return name + ' ' * (10 - len(name))

def hp_num_displayer(hp):
    if hp >= 10:
        return int(hp)
    else:
        return '0' + str(int(hp))

def battle_ui(player, enemy):
    os.system(cl())
    print(f'''
┌─────────────────────────────────────────────────────────────────────────────┐
│                                    Enemy: {name_displayer(enemy.species)}                        │
│                                    {hp_bar(enemy.hp)} ({hp_num_displayer(enemy.hp)} / 50)    │
│                                                                             │
│                                                                             │
│                                                                             │
│                                                                             │
│                                                    1. Skill Attack          │
│                                                    2. Physical Attack       │
│You: {name_displayer(player.pokemon[0].nickname)}                                     3. Cure                  │
│{hp_bar(player.pokemon[0].hp)} ({hp_num_displayer(player.pokemon[0].hp)} / 50)               4. Capture               │
│                                                    5. Change Pokemon        │
└─────────────────────────────────────────────────────────────────────────────┘''')

def show_map(player, event=None):
    ui_map = [['  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']]
    xpos, ypos = player.xpos, player.ypos
    ui_map[ypos][xpos] = ' 𖨆'
    if event == True:
        ui_map[ypos-1][xpos] = '❕'
    print('┌────────────────────┐')
    for i in ui_map:
        print('│', end='')
        for j in i:
            print(j, end='')
        print('│')
    print('└────────────────────┘')

def poke_appear():
    flash_1 = '''
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
    '''
    flash_2 = '''
    







    
    '''

    for i in range(3):
        os.system(cl())
        print(flash_1)
        time.sleep(0.3 + 0.1*i)
        os.system(cl())
        print(flash_2)
        time.sleep(0.3 + 0.1*i)
    
    
