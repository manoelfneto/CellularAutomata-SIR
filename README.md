# CellularAutomata-SIR
Repository containing a cellular automata made with python using pygame trying to simulate a behavior of a infectious disease

This code was made by using Python and a library calling pygame to show the interactions between the cells.

**intalling** <br />
first of all you have to install pygame, on you terminal type the comand: <br />
pip install pygame <br />
**end installing**

This Automata follow somes transictions rules to the cells change the states, it is based on the compartimental models.
The cells has 3 states: susceptible (white), infectious (red) and recovered (green).
After a cell gets infected, it will keep 7 generations/unity of time/steps on that state, so 1 to 7.(this rule was based on the recover 
time of Dengue). When you run the program, the algoritm will fill the matrix with 0 (susceptible) or 1 (initial infectious state), the probability of a cell get a 0 is bigger than get a 1, thats why on the first scene you will see more white spaces than red.


**Rules to transiction:** <br />
if the cell is on state 0 (susceptible) and has more than 3 infected neighbors, it will goes to the first infected state (1). <br />
if the cell is on state 0 (susceptible) and has less than 3 infected neighbors, it will keep on state 0. <br />
<br />
if the cell is on a infected state (1,2,3,4,5,6) it will goes to the next state when the the next generation arise. <br />
if the cell is on the last infection state (7) it will goes to the transition state (8). <br />
<br />
it the cell is on te transition state (8) is will goes the recovered state (9).<br />
<br />
When the program is running you can pause (pressing the space bar), initicial a new random matrix (pressing the R) or quit (pressing the Q).




