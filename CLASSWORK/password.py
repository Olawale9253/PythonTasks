"""
Accept user input to enter a password and analyze the password length by if password lenght is less than 8, it should print out very weak, elif the password is equal to 8 it should print out very weak, elif the password is between 8 and 16, it should print out strong and elif the password is greater than 16 it should print out very strong.

"""

password = len(input('Enter your password: '))

if (str(password <= '8')):

    print('very weak')

elif password == 8:

    print('weak')


