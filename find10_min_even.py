def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    m = 1000
    for i in data:
        if i%2==0:
            if m > i:
                m = i

    return m if m!=1000 else -1 
print(find_min_even([1, 8, 2, 8, 5]))
