# coding=utf-8
__author__ = "Laura Bolčina"

# user enters two floats and a selected operator
no1 = float(raw_input("Enter the first number: "))
no2 = float(raw_input("Enter the second number: "))
operator = raw_input("Enter an operator (+, -, *, /): ")

# check if the selected operator is one of the symbols in the string and execute operation
if operator in "+-*/":
    print eval("{0} {1} {2}".format(no1, operator, no2))
    # .format() is used to construct strings from other information - it substitutes each argument value into the place of the specification
    # eval() lets python program run python code within itself. It interprets a string as code. The reason why so many people have warned you about using this is because a user can use this as an option to run code on the computer. If you have eval(input()) and os imported, a person could type into input() os.system('rm -R *') which would delete all your files in your home directory. (Assuming you have a unix system). Using eval() is a security hole
else:
    print "Operation not supported."