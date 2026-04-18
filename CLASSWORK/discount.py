"""
Collect the user input to know how much the user is spending, if the amount is between 1,000 or greater than equal to 10,000 the customer should receive 5% discount

or if the purchase is between 10,000 or greater than equal to 50,000, the customer should receive a 10% discount

or if the purchase is greater than 50,000 the customer should receive 2 20% discount.

"""

discount = int (input('Enter a number'))

discount = 1000

if discount == 1000:


    print(discount / 100 * 5)


