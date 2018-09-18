# manages phone numbers
import pickle

def addNewNumber(number):
    assert(number[0] == "+") # should contain +1
    assert(len(number) == 12) # should be 12 numbers long
    
    numbers = pickle.load(open("numbers.p", 'rb'))
    try:
        numbers.index(number)
    except:
        numbers.append(number)
    pickle.dump(numbers, open("numbers.p", 'wb'))
        

def removeNumber(number):
    assert(number[0] == "+") # should contain +1
    assert(len(number) == 12) # should be 12 numbers long
    numbers = pickle.load(open("numbers.p", 'rb'))
    try:
        numbers.remove(number)
    except:
        print(number + " not in directory")
    pickle.dump(numbers, open("numbers.p", 'wb'))
    
def getNumberList():
    numbers = pickle.load(open("numbers.p", 'rb'))
    return numbers
    
    
    