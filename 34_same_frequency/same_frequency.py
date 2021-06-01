def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    counter1 = {}
    counter2 = {}

    for ltr in str1:
        counter1[ltr] = counter1.get(ltr, 0) + 1

    for ltr in str2:
        counter2[ltr] = counter2.get(ltr, 0) + 1

    return counter1 == counter2