balance = 312300
annualInterestRate = 0.25
###############################################################
monthlyInterestRate = annualInterestRate / 12.0
low = balance / 12
high = (balance * (1 + monthlyInterestRate)**12)/12
epsilon = 0.01

while True:
    lowestPayment = (high + low) / 2
    paidBalance = 0
    interestBalance = balance
    remainingBalance = balance
    for m in range(1,13):
        paidBalance += lowestPayment
        remainingBalance -= lowestPayment
        interestBalance += remainingBalance * monthlyInterestRate
        remainingBalance += remainingBalance * monthlyInterestRate
    if abs(paidBalance - interestBalance) <= epsilon:
        break
    elif paidBalance < interestBalance:
        low = lowestPayment
    elif paidBalance > interestBalance:
        high = lowestPayment
print "Lowest Payment:", round(lowestPayment, 2)
###############################################################
raw_input()
