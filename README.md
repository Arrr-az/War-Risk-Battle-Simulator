# War-Risk-Battle-Simulator
This program simulates an all-out battle in the Grow board game: "War", based on Hasbro's "Risk". Try out different numbers of nTroopsATK and nTroopsDEF on lines 100 and 101 and run the code to see the chances of ATK winning a battle 'till the last troop. Raising the number of simulations/battles (nBattles, line 102) gives a more accurate win-rate, but 20.000 simulations will provide satisfying enough accuracy.

### GAME CONTEXT
Summarizing: in the game, multiple players populate a map, each one with a territory, the objective being to conquer territories that belong to other players, until a certain individual (and secret) goal is reached.

### BATTLE MECHANICS
At any point in the game, each player will have some number of troops in a given territory, which can go from 1 to dozens of troops. If player 1 has territory A and wants to conquer territory B, that belongs to player 2, a battle will begin.

In a battle, each troop will be represented by a die. The attack will roll a number of ATK dices, and the defense will roll a number of DEF dices. Imagine 3 dice for each: largest ATK die gets compared with largest DEF die, 2nd largest ATK die with 2nd largest DEF die... etc. Then, for each compared pair, if the DEF die is larger or equal to the ATK die, a single ATK troop gets removed from the attacking territory. If DEF die is smaller, then ATK troop wins, and a single DEF troops gets removed from the deffending territory.

If we consider only 2 battling territories, ATK wins (i.e. conquers the defending territory) if it manages to remove all defending troops. DEF wins if ATK troops are reduced to 1, which renders it unable to attack any further.

Battle rules:
- A maximum of 3 troops from ATK and DEF each can battle at the same time.
- At least 1 ATK troop must stay in the territory, and is unable to battle.
- If an unequal dice battle happens (i.e.: 2 dice x 3 dice), the dice in excess are ignored in the comparing stage. Which dice in the side with dice in excess are ignored? The smallest number(s).

Examples:
- If a 9-ATK-troops territory attacks a 4-DEF-troops territory: it's a 3x3 dice battle;
- If a 4-ATK-troops territory attacks a 1-DEF-troop territory: a 3x1 dice battle;
- If a 3-ATK-troops territory attacks a 3-DEF-troops territory: a 2x3 dice battle;
- If a 2-ATK-troops territory attacks a 1-DEF-troop territory: a 1x1 dice battle;
- If a 1-ATK-troops territory attacks a 1-DEF-troop territory: it can't.

### TRIVIA
The idea for this program came from a specific battle between me and [Dmantuan](https://github.com/Dmantuan) where he attacked my 10-DEF-troops territory with 16 troops (and LOST!). A brief discussion about how unlikely that was emerged, and I set to find out using Python, which revealed that, in fact, it was slightly likely that his attack would fail.
