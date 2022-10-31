# Battle Settings
import random

def pokemon_encounter(wild):
    encountered = random.choices(wild, weights=[2,2,2,4])
    if encountered[0] != None:
        encountered[0].hp = 50
    return encountered
    
def is_effective(attack, defend):
    weakenss_chart = [[1, 0.5, 2],
                    [2, 1, 0.5],
                    [0.5, 2, 1]]
    attack_index = ['Fire', 'Water', 'Grass'].index(attack)
    defend_index = ['Fire', 'Water', 'Grass'].index(defend)
    return weakenss_chart[attack_index][defend_index]

def hp_bar(now):
    left = '#' * round(now / 2)
    dmg = '─' * (25 - round(now / 2))
    return f'[{left}{dmg}]'
            
def move_pos(player, move):
    if move in 'news':
        if move == 'n':
            if player.ypos > 1: 
                player.ypos -= 1
        if move == 'e':
            if player.xpos < 77:
                player.xpos += 1
        if move == 'w':
            if player.xpos > 1:
                player.xpos -= 1
        if move == 's':
            if player.ypos < 9:
                player.ypos += 1