# coding=utf-8
__author__ = "Laura Bolčina"

number = 23
guessing = True

while guessing:
    guess = int(raw_input("Guess a secret number: "))
    if guess < number:
        print "Your guess is too low. Try again."
    elif guess > number:
        print "Your guess is too high. Try again."
    else:
        print "Congratulations, you guessed the secret number!"
        guessing = False