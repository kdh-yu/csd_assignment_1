# Class settings

class Player:
    def __init__(self, name, xpos=4, ypos=4):
        self.name = name
        self.pokemon = []
        self.xpos = xpos
        self.ypos = ypos
    
    def pokemon_add(self, pokemon):
        self.pokemon.append(pokemon)

class Pokemon:
    def __init__(self, species, attribute, elemental_attack, hp, maxHP, strong_against, weak_against):
        self.species = species
        self.nickname = species
        self.attribute = attribute
        self.elemental_attack = elemental_attack
        self.physical_attack = 'Tackle'
        self.hp = hp
        self.maxHP = maxHP
        self.strong_against = strong_against
        self.weak_against = weak_against
    
    def set_nickname(self, nickname):
        self.nickname = nickname

Charmander = Pokemon('Charmander', 'Fire', 'Ember', 50, 50, 'Grass', 'Water')
Squirtle = Pokemon('Squirtle', 'Water', 'Water Gun', 50, 50, 'Fire', 'Grass')
Bulbasaur = Pokemon('Bulbasaur', 'Grass', 'Vine Whip', 50, 50, 'Water', 'Fire')

_Charmander = Pokemon('Charmander', 'Fire', 'Ember', 50, 50, 'Grass', 'Water')
_Squirtle = Pokemon('Squirtle', 'Water', 'Water Gun', 50, 50, 'Fire', 'Grass')
_Bulbasaur = Pokemon('Bulbasaur', 'Grass', 'Vine Whip', 50, 50, 'Water', 'Fire')