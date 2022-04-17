secretNumber = 10
userInput = 0
guessCount = 0
guessLimit = 3
while  guessCount < guessLimit:
    guess = int(input("Guess: "))
    guessCount += 1
    if guess == secretNumber:
        print('You Won!')
        break
else: 
    print('Sorry you lose!')

