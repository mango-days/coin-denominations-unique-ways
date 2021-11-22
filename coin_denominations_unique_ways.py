def count ( denominations , size , price ):
    if price == 0 :
        return 1
    elif price < 0 or size < 0 :
        return 0
 
    incl = count ( denominations , size , price - denominations [ size ] )
    excl = count ( denominations , size - 1, price)
    return incl + excl

denominations = [ 1, 2, 5 ]
price = 20
print ( 'ways =' , count ( denominations , len ( denominations ) - 1 , price ) )