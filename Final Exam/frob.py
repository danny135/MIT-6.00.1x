# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    before = atMe.getBefore()
    after = atMe.getAfter()
    
    if atMe.name < newFrob.name:
        if after == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif newFrob.name < after.name:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            newFrob.setAfter(after)
            after.setBefore(newFrob)
        else:
            insert(after, newFrob)
    elif newFrob.name < atMe.name:
        if before == None:
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
        elif before.name < newFrob.name:
            before.setAfter(newFrob)
            newFrob.setBefore(before)
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
        else:
            insert(before, newFrob)
    else:
        if before == None:
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
        else:
            before.setAfter(newFrob)
            newFrob.setBefore(before)
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
        

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')
danny = Frob('danny')
bob = Frob('bob')
jeff = Frob('jeff')
john = Frob('john')
jeb = Frob('jeb')

frobs = [eric, andrew, ruth, fred, martha, danny, bob, jeff, jeb, john, jeb]

for frob in frobs [1:]:
    insert(eric,frob)

frob = andrew
while frob != None:
    print frob
    frob = frob.getAfter()
