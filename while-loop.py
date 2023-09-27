import random

number = random.randint(1, 10)

guess_answer = True

print("Welcome to the guess the number game")
print("The rules are simple. I will think of a number and you will try to guess it.")


while guess_answer:
    guess = input("Choose a number from 1-10: ")
    if(number == int(guess) ):
        print("Congratulations! You have guessed the right number!")
    else:
        print("Sorry the answer is {}, you have guessed the wrong number! Try again.".format(number))
        