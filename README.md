# LifeSim
A python program that simulates the lives of cells in order to test various evolutionary and mathematical theories.
Cells can currently breed, hunt, fight with their competitors. Call a generation with generation(x,y,z). x = the number of cells, y = the amount of food generation per round, z = the number of generations. Then you'll want to read_book() and check out RECORD.

Each cell of the first generation will begin with either the genetic code 'A,A,A,A,A,A' or 'C,C,C,C,C,C'.

Protein translators:

1. Sperm Translator Active DNA: x,B,(C/D),x,x,x. Cell contributes food to its offspring.
2. Egg Translator Active DNA: x,A,(C/D),x,x,x Cell gestates offspring for one generation.
3. Kryptonite Environment Translatore Active DNA: x,x,x,x,[C/D],[A/B] Cell is half as likely to die from environment krptonite toxin.
