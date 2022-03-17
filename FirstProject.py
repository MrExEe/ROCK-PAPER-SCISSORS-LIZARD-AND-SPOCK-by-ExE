#FirstProject
print("ROCK , PAPER , SCISSORS , LIZARD AND SPOCK by ExE")
        
import random

options=['Rock' , 'Paper' , 'Scissors' , 'Lizard' , 'Spock']
numbers=random.randint(0,4)
Bot=options[numbers]
print("Bot Selection: ",Bot)

you=input("Option: ")
print("Your selection: ",you)


if (you == Bot) :
    print("Draw")

if (you == 'Rock'):
    if (Bot == 'Scissors'):
        print("You win")
    if (Bot == 'Paper'):
        print("You lose")
    if (Bot == 'Lizard'):
        print("You win")
    if (Bot == 'Spock'):
        print("You lose")

if (you == 'Scissors'):
    if (Bot == 'Rock'):
        print("You lose")
    if (Bot == 'Paper'):
        print("You win")
    if (Bot == 'Lizard'):
        print("You win")
    if (Bot == 'Spock'):
        print("You lose")

if (you == 'Spock'):
    if (Bot == 'Scissors'):
        print("You win")
    if (Bot == 'Paper'):
        print("You lose")
    if (Bot == 'Lizard'):
        print("You lose")
    if (Bot == 'Rock'):
        print("You win")

if (you == 'Lizard'):
    if (Bot == 'Scissors'):
        print("You lose")
    if (Bot == 'Paper'):
        print("You win")
    if (Bot == 'Rock'):
        print("You lose")
    if (Bot == 'Spock'):
        print("You win")

if (you == 'Paper'):
    if (Bot == 'Scissors'):
        print("You lose")
    if (Bot == 'Rock'):
        print("You win")
    if (Bot == 'Lizard'):
        print("You lose")
    if (Bot == 'Spock'):
        print("You win")
