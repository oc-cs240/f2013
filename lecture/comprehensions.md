
Comprehensions (list and otherwise)
===================================

A comprehension generates a collection from a collection. (text pp. 337-340)

This includes all iteration, plus the ability to modify and selectively
skip elements.

List Comprehension
------------------

    # Syntax
    # Mapping
    [<item> <iteration>]

    # Filtering
    [<item> <iteration> if <expression>]


    # Examples
    [item for item in other_list]  # Create a copy of the original list
    [modify(item) for item in other_list]  # Modified list
    [item for item in other_list if item > value]  # Filtered list
    [taxpayer for taxpayer in country if random_5_percent()]

Dictionary Comprehension
------------------------

    # Syntax
    # Mapping
    {<key>: <value> <iteration>}

    # Filtering
    {<key>: <value> <iteration> if <expression>}


    d = {'a': 1, 'b': 2, 'c': 3}
    dc1 = {k: v for k, v in d.items()}
    dc2 = {item[1]: item[0] for item in d.items()}
    dc3 = {item[0]: item[1] * 10 for item in d.items() if item[1] % 2 == 1}
    print(d)
    print(dc1)
    print(dc2)
    print(dc3)

    {'b': 2, 'c': 3, 'a': 1}
    {'b': 2, 'c': 3, 'a': 1}
    {1: 'a', 2: 'b', 3: 'c'}
    {'c': 30, 'a': 10}

