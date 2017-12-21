balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
######################################################################
monthlyInterestRate = annualInterestRate / 12
paidBalance = 0

for m in range(1,13):
    print "Month:", m
    print "Minimum monthly payment:", round(balance * monthlyPaymentRate, 2)
    paidBalance += round(balance * monthlyPaymentRate, 2)
    balance -= round(balance * monthlyPaymentRate, 2)
    balance += round(balance * monthlyInterestRate, 2)
    print "Remaining balance:", round(balance, 2)
print "Total paid:", round(paidBalance, 2)
print "Remaining balance:", round(balance, 2)
######################################################################
raw_input()
	
