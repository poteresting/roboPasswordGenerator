# A program that generates password for you
import random, string

print("I am RoboPass, I generate password that are strong and easy to remember.")
print("Please note your password, as it will be completely forgotten after program terminates!\n")
#Get the length of the password

passlen = input("What should be the length of your password?\n(Press Enter-key for password of any length) ==> ")
while type(passlen) == str:
    try:
        if passlen == '':
            passlen = random.randint(10, 18)
        if passlen == '0':
            passlen = input("You need to enter more than 0, to create a password!\n(Recommended is atleast 12 for strong passwords) ==> ")
        passlen = int(passlen)
    except ValueError:
        passlen = input("Please enter the length of your password in digits (example: 8, 12, 15) or Enter-key for password of any length ==> ")

password = ''
while password == '':
    #Get some details about what must the password contain
    print("\nTo generate your password, please tell us what should your password consist. Type 'y' for yes or 'n' for no")
    if_upperch = input("Password should have atleast an uppercase character (y/n) ==> ").lower()
    if_lowerch = input("Password should have atleast a lowercase character (y/n) ==> ").lower()
    if_numch = input("Password should have atleast a number (y/n) ==> ").lower()
    if_symch = input("Password should have atleast a symbol (y/n) ==> ").lower()
    if_start = input("Should your password start with something?\n(If yes, then please write the word, or press Enter-key to ignore) ==> ")

    while len(if_start) >= passlen:
        if len(if_start) == passlen:
            if_start = input("The length of " + if_start + " is same to the length of password you requested.\nLet's try another word to start with, or press Enter-key to ignore ==> ")
        elif len(if_start) > passlen:
            if_start = input("The length of " + if_start + " is more than the length of password you requested.\nLet's try another word to start with, or press Enter-key to ignore ==> ")

    if_ambch = input(r'''Password should avoid ambiguous characters such as (!?()[]{};:<>,.`'"~/\|-+=) (y/n) ==> ''').lower()

    #Formation of the password
    try:  
        for i in range(0, passlen-len(if_start)):

            #Based upon the user's choices we choose whether to assign a value or nothing to the character variables
            if if_upperch == 'y':
                upperch = random.choice(string.ascii_uppercase)
            elif if_upperch == 'n':
                upperch = ''

            if if_lowerch == 'y':
                lowerch = random.choice(string.ascii_lowercase)
            elif if_lowerch == 'n':
                lowerch = ''

            if if_numch == 'y':
                numch = random.randint(0, 9)
            elif if_numch == 'n':
                numch = ''

            if if_symch == 'y':
                symch = random.choice('@#$%^&*_')
            elif if_symch == 'n':
                symch = ''

            if if_ambch == 'n': #The question is phrased in a way asking if it should be avoided
                ambch = random.choice(r'!?()[]{};:<>,.`\'"~/\|-+=')
            elif if_ambch == 'y':
                ambch = ''

            password += random.choice(upperch + lowerch + str(numch) + symch + ambch)
    except IndexError:
        print("\nYou need to choose atleast one type of character to make your password.")

print('\nRoboPass suggests the password ==> ', if_start + password)