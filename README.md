# LifeSim
A python program that simulates the lives of cells in order to test various evolutionary and mathematical theories.
Cells can currently breed, hunt, fight with their competitors. Call a generation with generation(x,y,z). x = the number of cells, y = the amount of food generation per round, z = the number of generations. Then you'll want to read_book() and check out RECORD.

Each cell of the first generation will begin with either the genetic code 'A,A,A,A,A,A' or 'C,C,C,C,C,C'. A protein translator-- sperm_translator(cell)--will be called during breeding. If the mate cell--not the birthing parent--has the genetic code 'x,A,D,x,x,x' they will contrbute food to the offspring in addition to the birthing parent.
