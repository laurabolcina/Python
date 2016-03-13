# coding=utf-8
__author__ = "Laura Bolčina"

dna_data = raw_input("Enter the name of the file with DNA data for analysis: ")
dna = open(dna_data, "r").read()
print "DNA of the criminal: ", dna

# suspects database
suspects = {"Žiga": ["white", "male", "ginger", "brown", "round"],
            "Matej": ["white", "male", "black", "blue", "oval"],
            "Miha": ["white", "male", "brown", "green", "square"]}

criminal = []

race_dna = ["AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]
race = ["white", "black", "Asian"]

gender_dna = ["TGCAGGAACTTC", "TGAAGGACCTTC"]
gender = ["male", "female"]

hair_colour_dna = ["CCAGCAATCGC", "GCCAGTGCCG", "TTAGCTATCGC"]
hair_colour = ["black", "brown", "ginger"]

eye_colour_dna = ["TTGTGGTGGC", "GGGAGGTGGC", "AAGTAGTGAC"]
eye_colour = ["blue", "green", "brown"]

face_dna = ["GCCACGG", "ACCACAA", "AGGCCTCA"]
face = ["square", "round", "oval"]

# zip returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
race_base = zip(race_dna, race)
gender_base = zip(gender_dna, gender)
hair_base = zip(hair_colour_dna, hair_colour)
eye_base = zip(eye_colour_dna, eye_colour)
face_base = zip(face_dna, face)

database = race_base + gender_base + hair_base + eye_base + face_base

for i in database:
    if dna.find(i[0]) != -1:
        criminal.append(i[1])

for suspect, properties in suspects.items():
    if criminal == properties:
        print "The analysed DNA belongs to {0}." .format(suspect)