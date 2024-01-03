import random

def compare2Dice(dieDEF, dieATK):
    
    if dieDEF >= dieATK:
        return 1        # DEF wins
    else:
        return 0        # ATK wins

def compareAll(diceDEF, diceATK, nTroopsInBattle):
    
    # Counting DEF troops' wins
    defended = 0
    for i in range( nTroopsInBattle ):
        defended += compare2Dice(diceDEF[i], diceATK[i])
        
    # print("Defended: " + str(defended))
        
    return defended

def roll(nDiceDEF, nDiceATK, diceDEF, diceATK):
    
    # Rolling dices
    for i in range(nDiceDEF):
        rolledDie = random.randint(1,6)
        diceDEF.append(rolledDie)
    
    for i in range(nDiceATK):
        rolledDie = random.randint(1,6)
        diceATK.append(rolledDie)
    
    # Sorting in descending order
    diceDEF.sort(reverse=True)
    diceATK.sort(reverse=True)
    
    # print("DEF dice: ")
    # print(diceDEF)
    # print("ATK dice: ")
    # print(diceATK)
    
def subtractingTroops(nTroopsDEF, nTroopsATK, nTroopsInBattle, defended):
    
    nTroopsDEF[0] -= nTroopsInBattle - defended
    nTroopsATK[0] -= defended
    
    # print("DEF: " + str(nTroopsDEF[0]) + " // " + "ATK: " + str(nTroopsATK[0]))
    

def battleTurn(nTroopsDEF, nTroopsATK, turn):
    
    turn[0] += 1
    # print("\n---- TURN: " + str(turn) + " ----")
    
    diceDEF = []
    diceATK = []
    
    # Defining how many dice DEF and ATK will roll
    if nTroopsDEF[0] >= 3:
        nDiceDEF = 3
    else:
        nDiceDEF = nTroopsDEF[0]
    
    if nTroopsATK[0] >= 4:
        nDiceATK = 3
    else:
        nDiceATK = nTroopsATK[0] - 1
    
    # How many troops in battle?
    nTroopsInBattle = min(nDiceDEF, nDiceATK)
    
    # Rolling dice
    roll(nDiceDEF, nDiceATK, diceDEF, diceATK)
    
    # How many did defense win?
    defended = compareAll(diceDEF, diceATK, nTroopsInBattle)
    
    subtractingTroops(nTroopsDEF, nTroopsATK, nTroopsInBattle, defended)
    
def battleTillTheLast(nTroopsDEF, nTroopsATK):
    
    turn = [0]
    
    while nTroopsDEF[0] >= 1 and nTroopsATK[0] >= 2:
        battleTurn(nTroopsDEF, nTroopsATK, turn)
        # print("DEF: " + str(nTroopsDEF[0]) + " // " + "ATK: " + str(nTroopsATK[0]))
    
    if nTroopsDEF[0] <= 0:
        return 1
        # print("ATK WINS!")
    else:
        return 0
        # print("DEF WINS")

if __name__ == "__main__":
    
    ATKwins = 0

    # Parameters. Define your own number of troops for ATK/DEF
    # as well as how many simulations (battles) will run
    nTroopsATK = 16
    nTroopsDEF = 10
    nBattles = 20000

    for i in range(nBattles):
        ATKwins += battleTillTheLast([nTroopsDEF], [nTroopsATK])

    print("Out of " + str(nBattles) + " battles, ATK won " + str(ATKwins) )
    print("ATK win percentage: " + str(ATKwins * 100 / nBattles) + "%" )
