import random

# variables globales
CONSTS = {
    'MIN_BET' : 5,
    'MAX_ROUND_AMOUNT' : 1000,
    'AMOUNT_TO_WIN' : 500,
    'AMOUNT_TO_LOSE' : 0,
}
wallet = 100
play = True
tries = 0
lineSpace = 42
numbers = {  
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}
# ------------------------------------------
def generateRandomNumber():
    return random.randint(1, 6)
def isWinningNumber(randomNumber):
    return randomNumber %2 == 0
def getPares():
    return numbers[6] + numbers[4] + numbers[2]
def getImpares():
    return numbers[5] + numbers[3] + numbers[1]


def cleanNumbers():
    numbers[1] = 0
    numbers[2] = 0
    numbers[3] = 0
    numbers[4] = 0
    numbers[5] = 0
    numbers[6] = 0
    


print('*'*lineSpace)
print('*'+'Hola bienvenido a Gambling game'.center(lineSpace-2)+'*')
print('*'*lineSpace)
tries = 0
while(play):
    print('Tu saldo en la cartera es: ' + str(wallet))
    print('Cuanto vas a apostar?')
    amountToBet = int(input())
    if amountToBet < CONSTS['MIN_BET'] or amountToBet > wallet:
        while(amountToBet < CONSTS['MIN_BET'] or amountToBet > wallet):
            if amountToBet < CONSTS['MIN_BET']:
                print('Debe ser mayor o igual a ' + str(CONSTS['MIN_BET']))
                amountToBet = int(input())
            elif amountToBet > wallet:
                print('No puedes apostar mas de ' + str(wallet))
                amountToBet = int(input())
    print('El juego va a comenzar, presiona ENTER para continuar')
    input()
    for i in range(CONSTS['MAX_ROUND_AMOUNT']):
        if(wallet >= CONSTS['AMOUNT_TO_WIN'] or wallet <= CONSTS['AMOUNT_TO_LOSE']):
            break
        randomNumber = generateRandomNumber()
        if(isWinningNumber(randomNumber)):
            wallet += amountToBet
        else:
            wallet -= amountToBet
        numbers[randomNumber] +=  1
        tries = tries + 1
    if wallet >= CONSTS['AMOUNT_TO_WIN']:
        print('*'*lineSpace)
        print('*'+'GANASTE!!!'.center(lineSpace-2)+'*')
        print('*'*lineSpace)
    elif wallet <= CONSTS['AMOUNT_TO_LOSE']:
        print('*'*lineSpace)
        print('*'+'Perdiste'.center(lineSpace-2)+'*')
        print('*'*lineSpace)
    else:
        print('*'*lineSpace)
        print('*'+' Sigue jugando, no pierdas la esperanza!'.center(lineSpace-2)+'*')
    print('*'*lineSpace)
    print('*'+'Datos generales'.center(lineSpace-2)+'*')
    print('*'*lineSpace)
    print('*'+(' Saldo: ' + str(wallet)).ljust(lineSpace-2,' ')+'*')
    print('*'+(' Intentos: ' + str(tries)).ljust(lineSpace-2,' ')+'*')
    print('*'*lineSpace)
    print('*'+'Tiradas'.center(lineSpace-2)+'*')
    print('*'*lineSpace)
    print('*'+(' 1: ' + f'{numbers[1]} ({((numbers[1]/tries)*100):.2f}%)').ljust(lineSpace-2,' ')+'*')
    print('*'+(' 2: ' + f'{numbers[2]} ({((numbers[2]/tries)*100):.2f}%)').ljust(lineSpace-2,' ')+'*')
    print('*'+(' 3: ' + f'{numbers[3]} ({((numbers[3]/tries)*100):.2f}%)').ljust(lineSpace-2,' ')+'*')
    print('*'+(' 4: ' + f'{numbers[4]} ({((numbers[4]/tries)*100):.2f}%)').ljust(lineSpace-2,' ')+'*')
    print('*'+(' 5: ' + f'{numbers[5]} ({((numbers[5]/tries)*100):.2f}%)').ljust(lineSpace-2,' ')+'*')
    print('*'+(' 6: ' + f'{numbers[6]} ({((numbers[6]/tries)*100):.2f}%)').ljust(lineSpace-2,' ')+'*')
    print('*'+(' Pares: ' + f'{getPares()} ({((getPares()/tries)*100):.2f}%)').ljust(lineSpace-2,' ')+'*')
    print('*'+(' Inpares: ' + f'{getImpares()} ({((getImpares()/tries)*100):.2f}%)').ljust(lineSpace-2,' ')+'*')
    print('*'*lineSpace)

    if( wallet >= CONSTS['AMOUNT_TO_WIN'] or wallet <= CONSTS['AMOUNT_TO_LOSE']):
        cleanNumbers()
        tries = 0
        wallet = 50
    
    print('deseas jugar de nuevo?')
    play = (input() == 'si')
        