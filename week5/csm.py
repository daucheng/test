def is_sorted(n:int):
    """
    takes in an integer n and returns true if the digits of
    that number are increasing from right to left.
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    if n < 10:
        return True
    elif ((n//10) % 10) >= (n % 10): 
        return is_sorted(n//10)
    else:
        return False
    
def mario_number(level):
    """
    Return the number of ways that Mario can traverse the
    level, where Mario can either hop by one digit or two
    digits each turn. A level is defined as being an integer
    with digits where a 1 is something Mario can step on and 0
    is something Mario cannot step on.
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """
    assert only_one_zero(level)
    
    if level == 1:
        return 1
    elif level%10 == 0:
        return 0
    else:
        return mario_number(level//10)+mario_number(level//100)

def only_one_zero(n):
    if n == 1 or n == 0:
        return True
    elif n%10 == 1 or n%10 == 0:
        return only_one_zero(n//10)
    else:
        return False

def make_change(n):
    """
    Write a function, make_change that takes in an
    integer amount, n, and returns the minimum number
    of coins we can use to make change for that n,
    using 1-cent, 3-cent, and 4-cent coins.
    Look at the doctests for more examples.
    >>> make_change(5)
    2
    >>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3
    2
    """
    if n <= 0:
        return 0
    elif n in [1,3,4]:
        return 1
    elif n == 2:
        return 2
    else:
        return min(make_change(n-i) + 1 for i in [1,3,4])
    
#Abstract Data Type
    #constructor
def elephant(name,age,can_fly):
    return [name, age, can_fly]

    #selectors
def elephant_name(e):
    return e[0]
def elephant_age(e):
    return e[1]
def elephant_can_fly(e):
    return e[2]
    #Q1
"""
there’s something wrong about its implementation. How do we fix it?
Takes in a list of elephants and returns a list of their
names.
def elephant_roster(elephants):
    return [elephant[0] for elephant in elephants]
"""
#return [elephant_name(elephant) for elephant in elephants]

#Fill out the constructor for given selectors.
def elephant(name, age, can_fly):
    """
    >>> chris = elephant("Chris Martin", 38, False)
    >>> elephant_name(chris)
    "Chris Martin"
    >>> elephant_age(chris)
    38
    >>> elephant_can_fly(chris)
    False
    """
    def select(command):
        if command == "name":
            return name
        elif command =="age":
            return age
        elif: command == "can_fly"
            return can_fly
    return select    
def elephant_name(e):
    return e("name")
def elephant_age(e):
    return e("age")
def elephant_can_fly(e):
    return e("can_fly")
    
if __name__=='__main__':
    import doctest
    doctest.testmod()