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

print(result)

