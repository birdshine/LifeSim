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

def d100():
    """Probability."""
    d100 = random.randint(1,100)
    return d100

def random_starting_food():
    """Creates random starting food."""
    food = random.randint(1,3)
    if food == 1:
        return 1
    elif food == 2:
        return 2
    else:
        return 3

def census_yield():
    """Yields census for world_reset()"""
    for cell in CENSUS:
        yield [cell[1][0], cell[1][1]]

def world_reset():
    """Will reset WORLD with only living cells from CENSUS."""
    del WORLD[:]
    WORLD.extend(census_yield())

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

def food_set(food):
    """Returns a list of food locations for food amount given."""
    food = range(1,(food*100)+1)
    for i in food:
        yield [random_location(),random_location()]
    
        
"""End of functions that do work."""

"""DNA CODE SIGNIFICANCE
[5][6] = CELL MEMBRANE controls whether or not cell can survive the presence of toxic chemical Kyrptonite in the environment.
[1][2] = SEXUAL VALUES controls whether the cell is a spem or an egg.
"""

def assign_dna():
    """Assigns either the genetic string 'A,A,A,A,A,A' or 'C,C,C,C,C,C' to the cell.dna of the
    first generation's cells.
    """
    male_or_female = random.randint(0,1)
    if male_or_female == 0:
        return 'A,A,A,A,A,A'
    else:
        return 'C,C,C,C,C,C'

"""Protein Translators"""
def sperm_translator(cell):
    """If the cell has the DNA for food donation to its offspring, giving 1/6th of its
    food in addition to the birthing partner, it is a sperm.
    Active DNA: x,B,(D/C),x,x,x
    """
    dna = cell.dna.split(',')
    if dna[1] == 'B' and dna[2] == 'D':
        return True
    elif dna[1] == 'B' and dna[2] == 'C':
        return True
    else:
        return False
    del dna[:]

def egg_translator(cell):
    """If the cell has the DNA for harboring its offspring  inside it, granting it additional food
    and protection at the risk of the parent cell, it is an egg.
    Active DNA: x,A,(C/D),x,x,x
    """
    dna = cell.dna.split(',')
    if dna[1] == 'A' and dna[2] == 'C':
        return True
    elif dna[1] == 'A' and dna[2] == 'D':
        return True
    else:
        return False
    del dna[:]

def kryptonite_env_translator(cell):
    """This protein transaltor will test the cell's membrane and see if they are resistant
    to kryptonite, an imagined toxic substance in the environment's whos copyrights are
    owned by DC comics, I'm sure.
    Active DNA: x,x,x,x,(C/D),(A/B)
    """
    dna = cell.dna.split(',')
    if dna[4] == 'C' or dna[4] == 'D':
        if dna[5] == 'A' or dna[5] == 'B':
            return True
    else:
        return False
    del dna[:]
            
    
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
        self.pregnant = False
        self.gestating = False
        self.dna = assign_dna()
        self.parent = None

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
            cell_death(self)
            BOOK_OF_LIFE.append('The cell %s has died due food expenditure.' % self.id)

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
        """Zeros out food. Used for babies."""
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
                cell.food += -(cell.food / 6)
            break
        for baby in offspring_id:
            original_id = baby
            baby = Cell()
            baby.id = original_id
            baby.dna_inheritor(cell,mate)
            baby.parent = cell.id
            baby_x = (cell.x + plus_minus_same())
            baby_y = (cell.y + plus_minus_same())
            baby.world_set(baby_x,baby_y)
            food_start = (cell.food / 6)
            if sperm_translator(mate) is True:
                """Run sperm protein translator to test DNA of mate and see if mate is
                a sperm or not.
                """
                food_start += (mate.food / 6)
                mate.food_adj = -(mate.food / 6)
                BOOK_OF_LIFE.append('%s is a sperm and has contributed to its offspring %s.' \
                                    % (mate.id,baby.id))
            baby.food_zero()
            baby.food_adj(int(food_start))
            if egg_translator(cell) is True:
                """Runs egg protein translator to test DNA of cell and see if cell is
                an egg or not.
                """
                cell.pregnant = True
                baby.gestating = True
                cell_food = cell.food
                baby_food = baby.food
                cell.food = (cell_food + baby_food)
                baby.food = (cell_food + baby_food)
                baby.move_location(cell.x,cell.y)
                world_reset()
                BOOK_OF_LIFE.append('%s is an egg and nurtured its offspring %s.' % (cell.id,baby.id))
            BOOK_OF_LIFE.append('%s was born to %s and %s on x: %s y: %s DNA: %s' \
                                    % (baby.id,cell.id,mate.id,baby.x,baby.y,baby.dna))
            if sperm_translator(cell) == True or sperm_translator(mate) == True:
                if egg_translator(cell) == True or egg_translator(mate) == True:
                    BOOK_OF_LIFE.append('%s was born to both a sperm and an egg.' % baby.id)
            return baby

    if cell.food < 0:
        cell_death(cell)
        BOOK_OF_LIFE.append('%s died due to child birth.' % cell.id)
    if mate.food < 0:
        cell_death(mate)
        BOOK_OF_LIFE.append('%s died from donating food to its offspring.' % mate.id)

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
        print(WORLD)
    """Goes through num generations."""
    for gen in range(1,(num+1)):
        """Cells will fight other cells occupying the same square in the WORLD.
        """
        for cell in cell_classes:
            for enemy in cell_classes:
                if enemy.x == cell.x and enemy.y == cell.y:
                    if enemy.id != cell.id:
                        if cell.alive == True and enemy.alive == True:
                            if cell.pregnant == False and enemy.pregnant == False:
                                if cell.gestating == False and enemy.gestating == False:
                                    if cell.mature == True and enemy.mature == True:
                                        enemy_cell = enemy
            try:
                if cell.food > enemy_cell.food:
                    cell_death(enemy_cell)
                    BOOK_OF_LIFE.append('%s was killed by the larger %s.' % (enemy_cell.id,cell.id))
                    if enemy_cell.pregant == True:
                        for gestator in cell_classes:
                            if gestator.alive == True and gestator.parent == enemy_cell.id:
                                cell_death(gestator)
                                BOOK_OF_LIFE.append('%s was killed in %s\'s womb.' % (gestator.id,enemy_cell.id))
                if cell.food == enemy_cell.food:
                    coin = coin_toss()
                    if coin == 1:
                        cell_death(enemy_cell)
                        BOOK_OF_LIFE.append('%s was killed by %s' % (enemy_cell.id,cell.id))
                        if enemy_cell.pregant == True:
                            for gestator in cell_classes:
                                if gestator.alive == True and gestator.parent == enemy_cell.id:
                                    cell_death(gestator)
                                    BOOK_OF_LIFE.append('%s was killed in %s\'s womb.' % (gestator.id,enemy_cell.id))
                    else:
                        cell_death(cell)
                        BOOK_OF_LIFE.append('%s was killed by %s.' % (cell.id,enemy_cell.id))
                        if cell.pregant == True:
                            for gestator in cell_classes:
                                if gestator.alive == True and gestator.parent == cell.id:
                                    cell_death(gestator)
                                    BOOK_OF_LIFE.append('%s was killed in %s\'s womb.' % (gestator.id,cell.id))
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
                        cell.food = (cell.food + hunt)

            cell.food += -1
            if cell.food < 0 and cell.alive == True:
                cell_death(cell)
                BOOK_OF_LIFE.append('%s has died of starvation.' % cell.id)
        """Cells attempt to mate."""
        for cell in cell_classes:
            babies = []
            if cell.alive == True and cell.mature == True:
                for other in cell_classes:
                    if other.alive == True and other.mature == True:
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
                if cell.pregnant == True:
                    cell.pregnant = False
                    for gestator in cell_classes:
                        if gestator.alive == True:
                            if gestator.gestating == True and gestator.parent == cell.id:
                                cell.food = int(cell.food / 2)
                                gestator.food = int(gestator.food / 2)
                                baby_x = (cell.x + plus_minus_same())
                                baby_y = (cell.y + plus_minus_same())
                                gestator.move_location(baby_x,baby_y)
                                gestator.gestating == False
        """Spawn food for generation."""
        del FOOD_WORLD[:]
        FOOD_WORLD.extend(food_set(food))
        """Kyrptonite environment toxin danger. 10% encounter. 30% chance of dying without resistance,
        15% with."""
        for cell in cell_classes:
            if cell.alive == True:
                kryptonite_enc_chance = d100()
                survive_chance = d100()
                if  kryptonite_enc_chance <= 1:
                    resistance_check = kryptonite_env_translator(cell)
                    if resistance_check == True:
                        if survive_chance <= 4:
                            cell_death(cell)
                            BOOK_OF_LIFE.append('%s has died from toxic kyrptonite in the environment, despite its resistance.' % cell.id)
                    else:
                        if survive_chance <= 8:
                            cell_death(cell)
                            BOOK_OF_LIFE.append('%s died from toxic krptonite in the environment, having no resistance.' % cell.id)
        times += 1
    """Ensures that WORLD and CENSUS only hold the living."""
    del CENSUS[:]
    for cell in cell_classes:
        if cell.alive == True:
            CENSUS.append([cell.id, [cell.x,cell.y]])
    world_reset()
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
                if sperm_translator(cell) == True:
                    print('Evolution: Sperm')
                if egg_translator(cell) == True:
                    print('Evolution: Egg')
                if kryptonite_env_translator(cell) == True:
                    print('Evolution: Resistant to Kryptonite')
        print(WORLD)
        print(times)
        
"""Copyright Patrick Morgan 2015, you may use, edit, and
distribute non-commercially. Made on the Raspberry Pi.
"""
