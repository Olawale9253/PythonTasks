"""prompt user to enter a number, by using a for loop the number should display multiplication table

"""


#
#num = int(input("Enter a number: "))
#
#
#for number in range(1, 11):
#
#    print((num * number))
#

print("\tMultiplication Table")

for table in range(1, 10):
    for number in range(1, 10):
       
        print((table * number), end = "\t ")

    print()


