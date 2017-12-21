def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    y = 0
    while b**y < x:
        if b**(y + 1) <= x:
            y += 1
        else:
            break
    return y

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    laced = ""
    while s1 + s2 != "":
        if s1 != "":
            laced += s1[0]
            s1 = s1[1:]
        if s2 != "":
            laced += s2[0]
            s2 = s2[1:]
    return laced

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return out + helpLaceStrings(s1[1:], s2[1:], s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')

def f(x):
    return x / 100

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

def sqrt1(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)

def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt2(a):
    return fixedPoint(babylon(a), 0.0001)

def McNuggets2(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    a = 0
    b = 0
    c = 0
    while True:
        guess = 6*a + 9*b + 20*c
        if  guess != n:
            if n - guess >= 20:
                c += 1
            elif n - guess >= 9:
                b += 1
            elif n - guess >= 6:
                a += 1
        else:
            return True
    else:
        return False

from random import randint

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    a = 0
    b = 0
    c = 0
    if n == 6 or n == 9 or n == 20:
        return True
    elif n < 6:
        return False
    
    for i in range(500):
        guess = 6*a + 9*b + 20*c
        if guess == n:
            return True
        elif guess < n:
            if 1 <= n/20:
                c = randint(0,int(n/20))
            if 1 <= n/9:
                b = randint(0,int(n/9))
            if 1 <= n/6:
                a = randint(0,int(n/6))
        elif guess > n:
            a = 0
            b = 0
            c = 0
    else:
        return False
