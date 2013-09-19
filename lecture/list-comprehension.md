Comprehensions (list and otherwise)
===================================

A comprehension generates a collection from a collection. (text pp. 337-340)

This includes all iteration, plus the ability to modify and selectively
skip elements.

List Comprehension
------------------

    # Syntax
    # Mapping
    [<action> <iteration>]

    # Filtering
    [<action> <iteration> if <expression>]

    # Examples
    [item for item in other_list]  # Create a copy of the original list
    [modify(item) for item in other_list]  # Modified list
    [item for item in other_list if item > value]  # Filtered list
    [taxpayer for taxpayer in country if random_5_percent()]

