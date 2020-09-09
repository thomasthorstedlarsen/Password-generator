#definitions:
from Randomcharacter import randomcharacter
def menu():
    print("This is a random password generator.")
    print("Do you want to generate a password with a lenght of 8 characters press 1.")
    print("Do you want to generate a password with a lenght of 12 characters press 2.")
    print("Do you want to generate a password with a lenght of 20 characters press 3.")
    print("Do you want to exit the program, press another key.")
    menuvalg=int(input())

    if menuvalg == 1:
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        return menu()
    elif menuvalg == 2:
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        return menu()
    elif menuvalg == 3:
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        randomcharacter(), randomcharacter(), randomcharacter(), randomcharacter(),
        return menu()
    else:
        exit(0)


state=menu()
while state:
    state=menu()



