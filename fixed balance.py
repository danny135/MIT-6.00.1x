balance = 428
annualInterestRate = 0.25
##########################################################################################
calculated = False
lowestPayment = 0
monthlyInterest = annualInterestRate / 12
while not calculated:
    lowestPayment += 0.01
    paidBalance = 0
    interestBalance = balance
    remainingBalance = balance
    for m in range(1,13):
        paidBalance += lowestPayment
        remainingBalance -= lowestPayment
        interestBalance += remainingBalance * monthlyInterest
        remainingBalance += remainingBalance * monthlyInterest
    if paidBalance >= interestBalance:
        calculated = True
print "Lowest Payment:", lowestPayment
##########################################################################################
print "Is it 40?"
raw_input()
