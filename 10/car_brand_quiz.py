# coding=utf-8
__author__ = "Laura Bolčina"

from random import choice

class Car(object):

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

cars = []

cars.append(Car("Daewoo", "Lanos", 2000))
cars.append(Car("Renault", "Clio", 2004))
cars.append(Car("Volkswagen", "Golf", 2014))
cars.append(Car("Hyundai", "i30", 2010))
cars.append(Car("Audi", "A4", 2007))
cars.append(Car("Zastava", "128", 1990))
cars.append(Car("Fiat", "500", 2011))
cars.append(Car("Ford", "Focus", 2003))

ready = raw_input("Are you ready to start the quiz? (y/n) ")
if ready in "yY":
    game = True
    while game:
        the_car = choice(cars) # chooses a random car
        guessed = False
        while not guessed: # asks the question over and over for the same car until guessed correctly - then the loop starts over, chooses a new car and continues the quiz
            guess = raw_input("What brand is " + the_car.model + ", year " + str(the_car.year) + "? ")
            guess = guess.capitalize()
            if guess in "qQ":
                print "Thanks for playing. Have a nice day!"
                guessed = True
                game = False
            elif guess != the_car.brand:
                print "Sorry, " + guess + " is not correct answer. Try again."
            else:
                print "Congratulations, your guess is correct!"
                guessed = True
else:
    print "Bye then."