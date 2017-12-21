def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    guess = (len(aStr))/2
    if aStr == "":
        return False
    elif aStr[guess] == char:
        return True
    elif len(aStr) == 1:
        return False
    elif aStr[guess] < char:
        return isIn(char, aStr[guess:])
    else:
        return isIn(char, aStr[:guess])
            
        
