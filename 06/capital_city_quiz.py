# coding=utf-8
__author__ = "Laura Bolčina"

capital_cities = {
    "Slovenia": "Ljubljana",
    "Austria": "Vienna",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Denmark": "Copenhagen",
    "Portugal": "Lisbon",
    "France": "Paris",
    "United Kingdom": "London",
    "Spain": "Madrid",
    "Slovakia": "Bratislava",
    "Serbia": "Belgrade",
    "Luxembourg": "Luxembourg",
    "Finland": "Helsinki",
    "Estonia": "Tallinn",
    "Switzerland": "Bern",
    "Albania": "Tirana",
    "Belgium": "Brussels",
    "Bosnia and Herzegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Czech Republic": "Prague",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Vatican City": "Vatican City",
    "Latvia": "Riga",
    "Lithuania": "Vilnius",
    "Liechtenstein": "Vaduz",
    "Macedonia": "Skopje",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam",
    "Poland": "Warsaw",
    "Romania": "Bucharest",
    "San Marino": "San Marino",
    "Ukraine": "Kiev",
    "Andorra": "Andorra la Vella",
    "Moldova": "Chisinau",
    "Ireland": "Dublin",
    "Belarus": "Minsk",
    "Russia": "Moscow",
    "Cyprus": "Nicosia",
    "Greenland": "Nuuk",
    "Iceland": "Reykjavik",
    "Malta": "Valletta"
}

print "Welcome to the capital city quiz!"

guess = True

while guess:
    for country in capital_cities:
        city = raw_input("What is the capital city of %s? "  % (country))
        city = city.lower()
        if city == capital_cities[country].lower():
            print "Your answer is correct!"
        else:
            print "No, it\'s %s." % (capital_cities[country])

# functions

def capital_city(country):
    city = capital_cities[country]
    return city

def check_capital_city(city, country):
    assert capital_city(country) == city
    return "check_capital_city() passed successfully"