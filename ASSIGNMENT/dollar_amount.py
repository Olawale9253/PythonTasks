def usd_to_naira(amount):
    rate = 1550  

    
    if not usd_to_naira (amount, (int, float)):
        return "Error: Amount must be a number"

    
    if amount < 0:
        return "Error: Amount cannot be negative"

    
    naira = amount * rate
    return usd_to_naira(naira, 2)



print(usd_to_naira(10))      
print(usd_to_naira(25.75))   
print(usd_to_naira(-5))     
print(usd_to_naira("abc")) 
