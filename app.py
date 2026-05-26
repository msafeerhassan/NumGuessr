# ask users name -> greets him -> ask user for upper bound -> ask user for lower bound -> picks random num b/w that -> let user guess -> record number of tries -> max tries = 20 -> feedback on each try - close, very close, far away etc -> if guess correct, a quote, if wrong, so a quote

import random

userName = str(input("Hey! What's your name: "))
status = ""
bestScore = 20
while True:
    print(f"Welcome, {userName}. Good Luck!")
    upperBound = int(input("Enter the upper bound for the random number I have to generate: "))
    lowerBound = int(input("Enter the lower bound for the random number I have to generate: "))

    while lowerBound >= upperBound:
        print("Lower Bound should be lower than the Upper Bound. Please try again :(")
        upperBound = int(input("Enter the upper bound for the random number I have to generate: "))
        lowerBound = int(input("Enter the lower bound for the random number I have to generate: "))
    
    result = random.randint(lowerBound, upperBound)

    userGuess = ""
    tries = 1

    winningQuotes = ["You were born to win, but to be a winner, you must plan to win, prepare to win, and expect to win.", "The difference between a successful person and others is not a lack of knowledge, but a lack of will.", "If you think you can win, you can win. Faith is necessary to victory.", "Victory belongs to the most persevering.", "Never dream about success, work for it.", "You have to win; they don't necessarily have to lose for you!", "Be bigger than your excuses."]

    losingQuotes = ["Success is a lousy teacher. It seduces smart people into thinking they can’t lose.", "We must accept finite disappointment, but never lose infinite hope.", "Sometimes by losing a battle you find a new way to win the war.", "It is worth remembering that the time of greatest gain in terms of wisdom and inner strength is often that of greatest difficulty.", "Sometimes you must lose everything to gain it again, and the regaining is the sweeter for the pain of loss."]

    while userGuess != result:
        userGuess = int(input(f"""Try Number: {tries}
        Guess: """))
        if userGuess > upperBound or userGuess < lowerBound:
            print("Your guess is either below Lower Bound or above Upper Bound. Please try again")
        else:
            if userGuess == result:
                print(f"You won at try number: {tries}")
                status = "win"
                if tries < bestScore:
                    bestScore = tries
                    print(f"This is your best score with only {bestScore} tries.")
                else:
                    pass
                print("Here's a quote for you:", random.choice(winningQuotes))
                break
            else:
                diff = result - userGuess
                if diff <= 5 and diff >= -5:
                    print("You are very close")
                elif diff <=10 and diff >= -10:
                    print("You are close.")
                elif diff <= 20 and diff >= -20:
                    print("Somewhere close :)")
                else:
                    print("POV: your whole bloodline watching you fail at guessing a number while they even guessed the enemy's correct move in war")
            tries += 1
            if tries == 21:
                print("You lost! Better Luck Next Time :)")
                status = "lost"
                print("Here's a quote for you:", random.choice(losingQuotes))
                break
            else: 
                pass
    while True:
        if status == "lost" or status == "win":
            consent = str(input("Would you like to replay? (y/n): "))
            if consent == "y" or consent == "Y":
                print("Great! Let's start again")
                break
            elif consent == "N" or consent == "n":
                print("Oh! Sad :(")
                exit()
            else:
                print("Please either choose Y or N")