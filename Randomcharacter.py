import random

def randomcharacter():
    char8shift=random.randrange(1,20)
    if char8shift <= 5:
        char8shift01 = random.randrange(1,26)
        if char8shift01 == 1:
            print("A")
        elif char8shift01 == 2:
            print("B")
        elif char8shift01 == 3:
            print("C")
        elif char8shift01 == 4:
            print("D")
        elif char8shift01 == 5:
            print("E")
        elif char8shift01 == 6:
            print("F")
        elif char8shift01 == 7:
            print("G")
        elif char8shift01 == 8:
            print("H")
        elif char8shift01 == 9:
            print("I")
        elif char8shift01 == 10:
            print("J")
        elif char8shift01 == 11:
            print("K")
        elif char8shift01 == 12:
            print("L")
        elif char8shift01 == 13:
            print("M")
        elif char8shift01 == 14:
            print("N")
        elif char8shift01 == 15:
            print("O")
        elif char8shift01 == 16:
            print("P")
        elif char8shift01 == 17:
            print("Q")
        elif char8shift01 == 18:
            print("R")
        elif char8shift01 == 19:
            print("S")
        elif char8shift01 == 20:
            print("T")
        elif char8shift01 == 21:
            print("U")
        elif char8shift01 == 22:
            print("V")
        elif char8shift01 == 23:
            print("W")
        elif char8shift01 == 24:
            print("X")
        elif char8shift01 == 25:
            print("Y")
        elif char8shift01 == 26:
            print("Z")
        else:
            print("Error! Something went wrong.")
    elif char8shift >= 6 and char8shift <= 10:
        char8shift11 = random.randrange(1,26)
        if char8shift11 == 1:
            print("a")
        elif char8shift11 == 2:
            print("b")
        elif char8shift11 == 3:
            print("c")
        elif char8shift11 == 4:
            print("d")
        elif char8shift11 == 5:
            print("e")
        elif char8shift11 == 6:
            print("f")
        elif char8shift11 == 7:
            print("g")
        elif char8shift11 == 8:
            print("h")
        elif char8shift11 == 9:
            print("i")
        elif char8shift11 == 10:
            print("j")
        elif char8shift11 == 11:
            print("k")
        elif char8shift11 == 12:
            print("l")
        elif char8shift11 == 13:
            print("m")
        elif char8shift11 == 14:
            print("n")
        elif char8shift11 == 15:
            print("o")
        elif char8shift11 == 16:
            print("p")
        elif char8shift11 == 17:
            print("q")
        elif char8shift11 == 18:
            print("r")
        elif char8shift11 == 19:
            print("s")
        elif char8shift11 == 20:
            print("t")
        elif char8shift11 == 21:
            print("u")
        elif char8shift11 == 22:
            print("v")
        elif char8shift11 == 23:
            print("w")
        elif char8shift11 == 24:
            print("x")
        elif char8shift11 == 25:
            print("y")
        elif char8shift11 == 26:
            print("z")
        else:
            print("Error! Something went wrong.")
    elif char8shift >= 11 and char8shift <= 15:
        char8shift21 = random.randrange(1,9)
        if char8shift21 == 1:
            print("1")
        elif char8shift21 == 2:
            print("2")
        elif char8shift21 == 3:
            print("3")
        elif char8shift21 == 4:
            print("4")
        elif char8shift21 == 5:
            print("5")
        elif char8shift21 == 6:
            print("6")
        elif char8shift21 == 7:
            print("7")
        elif char8shift21 == 8:
            print("8")
        elif char8shift21 == 9:
            print("9")
        else:
            print("Error! Something went wrong.")

    elif char8shift >= 16 and char8shift <= 20:
        char8shift31 = random.randrange(1,9)
        if char8shift31 == 1:
            print(".")
        elif char8shift31 == 2:
            print(",")
        elif char8shift31 == 3:
            print("-")
        elif char8shift31 == 4:
            print("*")
        elif char8shift31 == 5:
            print("!")
        elif char8shift31 == 6:
            print("%")
        elif char8shift31 == 7:
            print("?")
        elif char8shift31 == 8:
            print("=")
        elif char8shift31 == 9:
            print("/")
        else:
            print("Error! Something went wrong.")
    else:
        print("Error! Something went wrong.")

