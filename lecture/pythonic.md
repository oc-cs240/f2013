
Doing Things Pythonically
=========================

Why is there no case statement?
-------------------------------

In python, it is more common to use a dictionary for this.


    strengthInt = 3
    
    if strengthInt == 9:
        newVal = 'Royal Flush'
    elif strengthInt == 8:
        newVal = 'Straight Flush'
    elif strengthInt == 7:
        newVal = 'Four of a Kind'
    elif strengthInt == 6:
        newVal = 'Full House'
    elif strengthInt == 5:
        newVal = 'Flush'
    elif strengthInt == 4:
        newVal = 'Straight'
    elif strengthInt == 3:
        newVal = 'Three of a Kind'
    elif strengthInt == 2:
        newVal = 'Two Pairs'
    elif strengthInt == 1:
        newVal = 'One Pair'
    
    print('Semi-colon style')
    print(newVal)
    
    # Instead, use a dictionary
    descriptions = {9: 'Royal Flush',
                    8: 'Straight Flush',
                    7: 'Four of a Kind',
                    6: 'Full House',
                    5: 'Flush',
                    4: 'Straight',
                    3: 'Three of a Kind',
                    2: 'Two Pairs',
                    1: 'One Pair',
                    0: 'Nothing'}
    print('Pythonically')
    print(descriptions[3])
    
    # When a dictionary might not exist
    print()
    print('No key in dictionary')
    strengthInt = 42
    
    # Old school - good
    if strengthInt in descriptions.keys():
        print(descriptions[strengthInt])
    else:
        print('Invalid hand')
    
    # Using exceptions - better
    try:
        print(descriptions[strengthInt])
    except KeyError:
        print('Invalid hand')
        
    # Preferred missing key method is to use {}.get() - best
    print(descriptions.get(strengthInt, 'Invalid hand'))

    Semi-colon style
    Three of a Kind
    Pythonically
    Three of a Kind
    
    No key in dictionary
    Invalid hand
    Invalid hand
    Invalid hand



    # Getting help in ipython
    dict.get?

Module Runner
-------------


    def function():  # Called by main() or another function or when imported
        pass
    
    def other_function():  # Called by main() or another function or when imported
        pass
    
    def main():  # Does all work when this module is launched
        pass
    
    # A basic module runner that calls main() only when this program is launched
    if __name__ == '__main__':
        main()  # defined above
