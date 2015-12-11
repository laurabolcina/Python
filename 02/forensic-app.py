# coding=utf-8
__author__ = "Laura Bolčina"

dna_data = raw_input("Submit the name of the file with DNA data for analysis: ")
dna = open(dna_data, "r").read()
print "DNA of the criminal: ", dna

# suspects database
ziga = ["white", "m", "ginger", "brown", "round"]
matej = ["white", "m", "black", "blue", "oval"]
miha = ["white", "m", "brown", "green", "square"]

criminal = []

# analyse DNA for race
if dna.find("AAAACCTCA") != -1:
    print "The criminal is white",
    criminal.append("white")
elif dna.find("CGACTACAG") != -1:
    print "The criminal is black",
    criminal.append("black")
elif dna.find("CGCGGGCCG") != -1:
    print "The criminal is Asian",
    criminal.append("Asian")

# analyse DNA for gender
if dna.find("TGCAGGAACTTC") != -1:
    print "male,",
    criminal.append("m")
elif dna.find("TGAAGGACCTTC") != -1:
    print "female,",
    criminal.append("f")

# analyse DNA for hair colour
if dna.find("CCAGCAATCGC") != -1:
    print "black-haired,",
    criminal.append("black")
elif dna.find("GCCAGTGCCG") != -1:
    print "brown-haired,",
    criminal.append("brown")
elif dna.find("TTAGCTATCGC") != -1:
    print "ginger,",
    criminal.append("ginger")

# analyse DNA for eye colour
if dna.find("TTGTGGTGGC") != -1:
    print "has blue eyes",
    criminal.append("blue")
elif dna.find("GGGAGGTGGC") != -1:
    print "has green eyes",
    criminal.append("green")
elif dna.find("AAGTAGTGAC") != -1:
    print "has brown eyes"
    criminal.append("brown")

# analyse DNA for face shape
if dna.find("GCCACGG") != -1:
    print "and square face."
    criminal.append("square")
elif dna.find("ACCACAA") != -1:
    print "and round face."
    criminal.append("round")
elif dna.find("AGGCCTCA") != -1:
    print "and oval face."
    criminal.append("oval")

# check if the properties of the criminal match to any of the suspects in the database
if criminal == ziga:
    print "The analysed DNA belongs to Žiga."
elif criminal == matej:
    print "The analysed DNA belongs to Matej."
elif criminal == miha:
    print "The analysed DNA belongs to Miha."
else:
    print "The analysed DNA was not found in your database."
