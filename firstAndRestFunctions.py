# firstAndRestFunctions

def first(mylist):
    return mylist[0]

def rest(mylist):
    return mylist[1:]

def test_first_1():
    assert first(['UCSB','UCSD','Stanford'])=='UCSB'

def test_rest_1():
    assert rest(['UCSB','UCSD','Stanford'])==['UCSD','Stanford']


def totalLength(listOfStrings):
    if listOfStrings==[]:
       return 0
    else:
       return   len(first(listOfStrings))  + totalLength(rest(listOfStrings))

def countEvens(listOfInts):
    if listOfInts==[]:
        return 0
    if first(listOfInts)%2==0:
        return 1 + countEvens(rest(listOfInts))
    else:
        return 0 + countEvens(rest(listOfInts))
          
