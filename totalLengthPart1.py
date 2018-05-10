
# To review... adding up the lengths of strings in a list
# e.g. totalLength(["UCSB","Apple","Pie"]) should be: 12
# because len("UCSB")=4, len("Apple")=5, and len("Pie")=3, and 4+5+3 = 12

def totalLength(listOfStrings):
    " add up length of all the strings "


    # for now, ignore errors.. assume they are all of type str

    count = 0
    for string in listOfStrings:
        count = count + len(string)

    return count


def test_totalLength_1():
    assert totalLength(["UCSB","Apple","Pie"])==12

def test_totalLength_2():
    assert totalLength([])==0

def test_totalLength_3():
    assert totalLength(["Cal Poly"])==8
