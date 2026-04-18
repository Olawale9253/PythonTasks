first_number = int(input('Enter first number: '))

second_number = int(input('Enter second number: '))

grade = int(input('Enter a grade: '))

total = first_number + second_number

multiply = first_number * second_number

division = first_number / second_number

remainder = first_number % second_number

print ('addition is: ', total)

print ('multiply is: ', multiply)

print ('division is: ', division)

print ("Remainder is: ", remainder)

if grade >= 90:

    print('A')

elif grade >= 80:

    print('B')

elif grade >= 70:

    print('C')

elif grade >= 60:

    print('D')

else:

    print ('You failed')


