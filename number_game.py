# This is a number guessing game.
import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)

# print('DEBUG: Secret number is ' + str(secretNumber)) to debug your program.

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
          


    

