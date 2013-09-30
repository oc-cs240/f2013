
The Ternary Operator
====================

A simple if-else that behaves inline.



    a = 5
    b = 10 if a < 5 else 5
    {'a': a, 'b': b}




    {'a': 5, 'b': 5}



Similar to the behavior of filtering in list comprehension.


    alist = list(range(10))
    odds = [item for item in alist if item % 2 == 1]
    evens = [item for item in alist if item % 2 == 0]
    
    {'odds': odds, 'evens': evens}




    {'evens': [0, 2, 4, 6, 8], 'odds': [1, 3, 5, 7, 9]}



A similar operator exists in the semi-colon family of languages.

    b = a < 5 ? 10 : 5;      // C/C++


    
