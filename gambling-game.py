import random

# variables globales
CONSTS = {
    'MIN_BET' : 50,
    'MAX_ROUND_AMOUNT' : 2000,
    'AMOUNT_TO_WIN' : 500,
    'AMOUNT_TO_LOSE' : -100,
    'INITIAL_WALLET' : 0
}
# ------------------------------------------
def generateRandomNumber():
    return random.randint(1, 6)
def isWinningNumber(randomNumber):
    return randomNumber %2 == 0
def initGame(amountToBet, maxRoundAmount, amountToWin, amountToLose, initialWallet):
    wallet = initialWallet
    for i in range(maxRoundAmount):
        if(isWinningNumber(generateRandomNumber())):
            wallet += amountToBet
        else:
            wallet -= amountToBet

        if(wallet >= amountToWin):
            return 1
        elif(wallet <= amountToLose):
            return -1
    return 0
        
def repeatGame(tries, amountToBet, maxRoundAmount, amountToWin, amountToLose, initialWallet):
    winnings = 0
    loses = 0
    draws = 0
    result = 0
    for i in range(tries):
        result = initGame(amountToBet, maxRoundAmount, amountToWin, amountToLose, initialWallet)
        if  result == 1:
            winnings += 1
        elif result == -1:
            loses += 1
        else:
            draws += 1

    print(f'Winnings: {winnings}, Loses: {loses}, Draws: {draws}')
    
        
if __name__ == "__main__":
    repeatGame(10000, CONSTS['MIN_BET'], CONSTS['MAX_ROUND_AMOUNT'], CONSTS['AMOUNT_TO_WIN'], CONSTS['AMOUNT_TO_LOSE'],  CONSTS['INITIAL_WALLET'])
