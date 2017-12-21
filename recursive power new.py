def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if base <= 0:
        print "1"
        return 1
    elif base % 2 == 0: #Even
        print "Even", base * recurPowerNew(base * base,exp/2)
        return base * recurPowerNew(base * base,exp/2)
    elif base % 2 == 1:
        print "Odd", base * recurPowerNew(base,exp - 1)
        return base * recurPowerNew(base,exp - 1)
        
