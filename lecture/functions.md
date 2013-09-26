

    from math import pi
    
    unit_circle_area = pi * 0.5 ** 2
    
    def evaluate_poker_hand5(hand):
        pass
    
    def evaluate_poker_hand7(hand):
        for hand5 in hand:
            rank = evaluate_poker_hand5(hand5)
            # find best rank
    
    strength1 = evaluate_poker_hand(hand1)
    for hand in hands5:
        strength = evaluate_poker_hand(hand)
        # Do something with strength values


More on defining functions
--------------------------

### Named arguments

```
def some_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

some_function(1, 2, 3)  # prints 1 2 3
some_function(arg2=4, arg3=10, arg1=5)  # prints 5 4 10
some_function(1, 2)  # Throws an error
```

### Optional arguments

```
def some_function2(arg1, arg2, arg3=None):
    print(arg1, arg2, arg3)

some_function2(1, 2)  # prints 1 2 None

def some_function3(arg1=1, arg2=2, arg3=None):
    print(arg1, arg2, arg3)

some_function3(10)          # prints 10 2 None
some_function3(10, 20)      # prints 10 20 None
some_function3(10, 20, 30)  # prints 10 20 30
some_function3(arg3=50)     # prints 1 2 50
some_function3(10, arg3=50) # prints 10 2 50
some_function3(arg3=50, 10) # ERROR!! positional argument after named argument

```


    def some_function3(arg1=1, arg2=2, arg3=None):
        print(arg1, arg2, arg3)
    
    some_function3(arg3=50, arg1=10)

    10 2 50


### Beware using mutables as default values


    def some_function4(arg1, arg2, arg3=['a', 'b', 'c']):
        print(arg3)
        print(arg1, arg3[2])
        arg3[2] = 5
    
    some_function4(1, 2)
    some_function4(1, 2)
    
    
    # More properly
    print()
    def some_function5(arg1, arg2, arg3=None):
        if arg3 is None:
            arg3 = ['a', 'b', 'c']
        print(arg1, arg3[2])
        arg3[2] = 5
    
    some_function5(1, 2)
    some_function5(1, 2)
    
    
    # This is fine
    def some_function6(arg1, arg2, arg3='Invalid hand'):
        pass


    ['a', 'b', 'c']
    1 c
    ['a', 'b', 5]
    1 5
    
    1 c
    1 c

