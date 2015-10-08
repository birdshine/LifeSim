"""This program will simulate life on a cellular level simplisticly in order to test
various evolutionary and biological theories.
"""

import random
import string

"""WORLD represents the physical location of the cells. x = y
A list.
"""
WORLD = []
"""FOOD_WORLD represents the location of food that the cells
need to live.
A list.
"""
FOOD_WORLD = []
"""RECORD represents every cell that has ever lived.
It will track the cell's life span before it died.
A dictionary.
"""
RECORD = {}
"""CENSUS represents every cell that is currently alive.
It will keep track of the cell's X and Y coordinates.
A list.
"""
CENSUS = []
"""BOOK_OF_LIFE keeps a record of births and deaths.
It is a list
"""
BOOK_OF_LIFE = []
"""EVE holds the first generation. It is a list."""
EVE = []

"""Functions that will do work."""
def id_generator(size=10, chars=string.digits):
    """Generates a 10 string ID of uppercase characters and integers
    unless given the arguments 1) the length 2) characters to choose from
    in generation. h/t to the internet.
    """
    return ''.join(random.choice(chars) for _ in range(size))

def census_input(cell):
    """Turns a cell's attributes into data that can be added to CENSUS."""
    census_input = [cell.id, [cell.x, cell.y]]
    return census_input

def random_location():
    """Returns a random number between 1 and 50."""
    num = random.randint(1,25)
    return num

def world_input(cell):
    "Turns a cell's attributes intos data that can be added to WORLD."""
    world_input = [cell.x, cell.y]
    return world_input

def plus_minus_same():
    """Returns 1,0, or -1 randomly."""
    coin = random.randint(0,2)
    if coin == 0:
        return -1
    elif coin == 1:
        return 0
    else:
        return 1

def coin_toss():
    """Simulates a coin toss."""
    coin = random.randint(0,1)
    if coin == 0:
        return 0
    else:
        return 1

def random_starting_food():
    """Creates random starting food."""
    food = random.randint(1,3)
    if food == 1:
        return 1
    elif food == 2:
        return 2
    else:
        return 3

def world_reset():
    """Will reset WORLD with only living cells from CENSUS."""
    del WORLD[:]
    for cell in CENSUS:
        WORLD.append([cell[1][0], cell[1][1]])

def read_book():
    """Reads BOOK_OF_LIFE in a user friendly manner."""
    for entry in BOOK_OF_LIFE:
        print(entry)

def read_census():
    """Reads CENSUS in a user friendly manner."""
    for entry in CENSUS:
        print('Name: %s x: %s y: %s' % (entry[0],entry[1][0],entry[1][1]))

def read_world():
    """Reads WORLD in user friendly manner."""
    for entry in WORLD:
        print('Cell located at x: %s y: %s.' % (entry[0],entry[1]))

def read_food_world():
    """Reads FOOD_WORLD in a user friendly manner."""
    for entry in FOOD_WORLD:
        print('Food unit located at x: %s x: %s.' % (entry[0],entry[1]))

def read_record():
    """Reads RECORD in a user friendly manner."""
    for key in RECORD:
        if key in EVE:
            print('Of the first generation, %s lived for %s generation(s).' % (key,RECORD[key]))
        else:
            print('%s lived for %s generation(s).' % (key,RECORD[key]))

def read_eve():
    """Reads EVE in a user friendly manner."""
    print('The original generation contained %s cells.' % len(EVE))
    for entry in EVE:
        print(entry)

def get_x(pair):
    """Gets x value in a pair."""
    x = pair[0]
    return x

def get_y(pair):
    """Gets y in a pair."""
    y = pair[1]
    return y

def start_food():
    """Creates random starting food from 5-10."""
    food = random.randint(5,10)
    return food
        
"""End of functions that do work."""

"""DNA Code"""
def assign_dna():
    male_or_female = random.randint(0,1)
    if male_or_female == 0:
        return 'A,A,A,A,A,A'
    else:
        return 'C,C,C,C,C,C'

"""Classes that define entities."""
class Cell():
    """The unit of life for the simulation."""

    def __init__(self):
        """Creates a cell in limbo."""
        self.id = id_generator()
        self.life_span = 1
        self.food = start_food()
        self.mate = False
        self.mature = False
        self.dna = assign_dna()
        RECORD[self.id] = 1

    def world_set(self,x=False,y=False):
        """Sets the cell on the world and gives it life."""
        self.alive = True
        self.life_span = 1
        if x == False:
            self.x = random_location()
        else:
            self.x = x
        if y == False:
            self.y = random_location()
        else:
            self.y = y
        RECORD[self.id] = 1
        """Starting location for cells is limbo, location determined
        by parents.
        """
        WORLD.append(world_input(self))
        CENSUS.append(census_input(self))

    def move_location(self,x,y):
        """Moves cell to new location in the world."""
        WORLD.remove(world_input(self))
        CENSUS.remove(census_input(self))
        self.x = x
        self.y = y
        WORLD.append(world_input(self))
        CENSUS.append(census_input(self))

    def food_adj(self,cost):
        """Gives or takes food from a cell."""
        CENSUS.remove(census_input(self))
        self.food += cost
        CENSUS.append(census_input(self))
        if self.food < 0:
            cell_death(cell)
            print('The cell %s has died due food expenditure.' % self.id)

    def dna_inheritor(self,parent,mate):
        """Inherits DNA from parents instead of randomly generating."""
        pair1 = coin_toss()
        pair2 = coin_toss()
        pair3 = coin_toss()
        pair4 = coin_toss()
        pair5 = coin_toss()
        pair6 = coin_toss()
        alpha_raw = mate.dna.split(',')
        alpha = []
        for code in alpha_raw:
            if code == 'A':
                alpha.append('B')
            elif code == 'B':
                alpha.append('A')
            elif code == 'C':
                alpha.append('D')
            else:
                alpha.append('C')
        beta_raw = parent.dna.split(',')
        beta = []
        for code in beta_raw:
            if code == 'A':
                beta.append('B')
            elif code == 'B':
                beta.append('A')
            elif code == 'C':
                beta.append('D')
            else:
                beta.append('C')
        child = []
        if pair1 == 0:
            child.append('%s,' % beta[0])
        else:
            child.append('%s,' % alpha[0])
        if pair2 == 0:
            child.append('%s,' % beta[1])
        else:
            child.append('%s,' % alpha[1])
        if pair3 == 0:
            child.append('%s,' % beta[2])
        else:
            child.append('%s,' % alpha[2])
        if pair4 == 0:
            child.append('%s,' % beta[3])
        else:
            child.append('%s,' % alpha[3])
        if pair5 == 0:
            child.append('%s,' % beta[4])
        else:
            child.append('%s,' % alpha[4])
        if pair6 == 0:
            child.append('%s' % beta[5])
        else:
            child.append('%s' % alpha[5])
        child_str = ''.join(child)
        self.dna = child_str

    def food_zero(self):
        self.food = 0
"""End of classes that define entities."""

"""Biological Functions"""
def cell_death(cell):
    CENSUS.remove(census_input(cell))
    WORLD.remove(world_input(cell))
    cell.alive = False
    world_reset()
    
def mate_attempt(cell,mate):
    """Function will attempt to mate called cell with all other applicable cells."""
    valid_mates = 0
    for other in CENSUS:
        """If cell is adjacent shares x but not y, or vice versa,
        they can mate.
        """
        if other[1][0] == cell.x:
            if other[1][1] == cell.y:
                pass
            else:
                if mate.id == other[0]:
                    valid_mates += 1
        """If the cell is adjacent in x and/or y they can mate."""
        if other[1][0] == (cell.x + 1) or other[0] == (cell.x -1):
            if other[1][1] == (cell.y + 1) or other[1][1] == (cell.y -1):
                if mate.id == other[0]:
                    valid_mates += 1
    """Self cell must have enough food."""
    if cell.food < 1:
        valid_mates = 0
    """Cells can only have four babies at maximum."""
    if valid_mates > 3:
        valid_mates = 3
    """Let's make baby cells now."""
    if valid_mates > 0:
        offspring_id = []
        """Loops through creating ID's for baby cells, costing food."""
        while True:
            for i in range(1,(valid_mates + 1)):
                offspring_id.append(id_generator())
                cell.food += -1
            break
        for baby in offspring_id:
            original_id = baby
            baby = Cell()
            baby.id = original_id
            baby_x = (cell.x + plus_minus_same())
            baby_y = (cell.y + plus_minus_same())
            baby.dna_inheritor(cell,mate)
            baby.world_set(baby_x,baby_y)
            food_start = (cell.food / 3)
            baby.food_zero()
            baby.food_adj(food_start)
            BOOK_OF_LIFE.append('%s was born to %s on x: %s y: %s DNA: %s' \
                                    % (baby.id,cell.id,baby.x,baby.y,baby.dna))
            return baby
    if cell.food < 0:
        cell_death(cell)
        BOOK_OF_LIFE.append('%s died due to child birth.' % cell.id)

"""User command functions."""
def generation(first,food,num):
    """Primary call function of LifeSim engine."""
    cell_classes = []
    times = 1
    if times == 1:
        for cell in range(1,(first+1)):
                cell = Cell()
                cell_classes.append(cell)
                cell.world_set()
                BOOK_OF_LIFE.append('%s was born of the first generation at x: %s y: %s.' \
                                    % (cell.id,cell.x,cell.y))
                EVE.append('NAME: %s DNA: %s' % (cell.id,cell.dna))
                times += 1
        read_eve()
    """Goes through num generations."""
    for gen in range(1,(num+1)):
        """Fight other's in their own square."""
        for cell in cell_classes:
            for enemy in cell_classes:
                if enemy.x == cell.x and enemy.y == cell.y:
                    if enemy.id != cell.id:
                        if cell.alive == True and enemy.alive == True:
                            enemy_cell = enemy
            try:
                if cell.food > enemy_cell.food:
                    cell_death(enemy_cell)
                    BOOK_OF_LIFE.append('%s was killed by the larger %s.' % (enemy_cell.id,cell.id))
                if cell.food == enemy_cell.food:
                    coin = coin_toss()
                    if coin == 1:
                        cell_death(enemy_cell)
                        BOOK_OF_LIFE.append('%s was killed by %s' % (enemy_cell.id,cell.id))
                    else:
                        cell_death(cell)
                        BOOK_OF_LIFE.append('%s was killed by %s.' % (cell.id,enemy_cell.id))
                del enemy_cell
            except:
                pass                        
            
        """Hunt"""
        for cell in cell_classes:
            location = []
            location.append([cell.x,cell.y])
            for key in location:
                hunt = FOOD_WORLD.count(key)
                if hunt > 0:
                    if cell.alive == True:
                        cell.food_adj(hunt)
            cell.food += -1
            if cell.food < 0 and cell.alive == True:
                cell_death(cell)
                BOOK_OF_LIFE.append('%s has died of starvation.' % cell.id)
        """Cells attempt to mate."""
        for cell in cell_classes:
            babies = []
            if cell.alive == True:
                if cell.mature == True:
                    for other in cell_classes:
                        if other.alive == True:
                            if other.mature == True:
                                baby = mate_attempt(cell,other)
                                if baby is not None:
                                    cell_classes.append(baby)
        """Age the cells."""
        for cell in cell_classes:
            if cell.alive == True:
                cell.life_span += 1
                RECORD[cell.id] = cell.life_span
                if cell.life_span == 2:
                    cell.mature = True
        """Spawn food for generation."""
        del FOOD_WORLD[:]
        for item in range(1,(food+1)):
            FOOD_WORLD.append([random_location(),random_location()])
    """Ensures that WORLD and CENSUS only hold the living."""
    del WORLD [:]
    del CENSUS[:]
    for cell in cell_classes:
        if cell.alive == True:
            WORLD.append([cell.x,cell.y])
            CENSUS.append([cell.id, [cell.x,cell.y]])
    """Survivor check."""
    if times > num:
        survivor_list = []
        dead_list = []
        for cell in cell_classes:
            if cell.alive == True:
                survivor_list.append(cell.id)
            else:
                dead_list.append(cell)
        total_survivors = len(survivor_list)
        total_dead = len(dead_list)
        print('%s Dead' % total_dead)
        print('%s Survivors' % total_survivors)
        for cell in cell_classes:
            if cell.alive == True:
                print('Name: %s Lifespan: %s Food: %s DNA: %s' % (cell.id,cell.life_span,cell.food,cell.dna))
        
"""Copyright Patrick Morgan 2015, you may use, edit, and
distribute non-commercially. Made on the Raspberry Pi.
"""
