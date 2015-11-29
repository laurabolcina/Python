# Laura Bolčina
# coding=utf-8

stevilo = 23
ugibaj = True

while ugibaj:
    ugani = int(raw_input("Ugani skrito število: "))
    if ugani < stevilo:
        print "Število žal ni pravilno. Skrito število je večje. Poskusi znova."
    elif ugani > stevilo:
        print "Število žal ni pravilno. Skrito število je manjše. Poskusi znova."
    else:
        print "Bravo, uganil si pravo število!"
        ugibaj = False