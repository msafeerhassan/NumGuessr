# ask users name -> greets him -> ask user for upper bound -> ask user for lower bound -> picks random num b/w that -> let user guess -> record number of tries -> max tries = 20 -> feedback on each try - close, very close, far away etc -> if guess correct, a quote, if wrong, so a quote

import random

userName = str(input("Hey! What's your name: "))
print(f"Welcome, {userName}. Good Luck!")
upperBound = int(input("Enter the upper bound for the random number I have to generate: "))
lowerBound = int(input("Enter the lower bound for the random number I have to generate: "))

if lowerBound >= upperBound:
    result = "Lower Bound should be lower than the Upper Bound. Please try again :("
else:
    result = random.randrange(lowerBound, upperBound, 1)

userGuess = ""
tries = 1

while userGuess != result:
    userGuess = int(input(f"""Try Number: {tries}
Guess: """))
    if userGuess > upperBound or userGuess < lowerBound:
        print("Your guess is either below Lower Bound or above Upper Bound. Please try again")
    else:
        if userGuess == result:
            print(f"You won at try number: {tries}")
            break
        else:
            if userGuess > result:
                print("Hmm... maybe a smaller number would work")
            else:
                print("Hmm... maybe a bigger number would work")
        tries += 1
        if tries == 11:
            print("You lost! Better Luck Next Time :)")
            break
        else: 
            pass