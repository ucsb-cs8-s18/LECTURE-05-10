# screenFuncs.py
# functions for dealing with pixels on a screen


def makeScreen(rows,cols,pixelValue):
    """ return a list of lists, representing pixels in rows and cols """
    screen = []
    for r in range(rows):        
        thisRow = []
        for c in range(cols):
            thisRow.append(pixelValue)
        # now this row is full of pixelValue p, e.g.
        # [p, p, p, p, ... ] 
        screen.append(thisRow)    
    return screen

def makeEmptyScreen(rows,cols):
    return makeScreen(rows,cols,0)

def makeFullScreen(rows,cols):
    return makeScreen(rows,cols,1)


def printScreen(screen):

    for row in range(len(screen)):   # how many rows are there in screen?
      for col in range(len(screen[0])):  # how many columns are there in screen?
        if screen[row][col]==1 :    # screen at this row and column 
          print('*',end="")
        else:
          print(' ',end="")
      print("")
          
def test_makeScreen_3_rows_2_cols():

    assert makeScreen(3,2,0)==[ [0,0],
                              [0,0],
                              [0,0] ]

def test_makeScreen_4_rows_6_cols():

    assert makeScreen(4,6,1)==[ [1,1,1,1,1,1],
                                [1,1,1,1,1,1],
                                [1,1,1,1,1,1],
                                [1,1,1,1,1,1]]


def clearRow(screen,row):
    " set all values in a certain row of screen to zero"
    numberOfColumns = len(screen[0])
    screen[row] = []
    for i in range(numberOfColumns):
       screen[row].append(0)
        

def test_clearRow_1():
    screen = makeFullScreen(3,4)
    clearRow(screen,1)
    expected = [ [1,1,1,1],
                 [0,0,0,0],
                 [1,1,1,1] ]
    assert(screen==expected)

def test_clearRow_2():
    screen = makeFullScreen(4,5)
    clearRow(screen,2)
    expected = [ [1,1,1,1,1],
                 [1,1,1,1,1],
                 [0,0,0,0,0],
                 [1,1,1,1,1] ]
    assert(screen==expected)









    
