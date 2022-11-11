def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    m = 1000
    for i in data:
        if i%2==1:
            if m > i:
                m = i

    return m if m!=1000 else -1
print(find_min_odd([1, 8, 2, 8, 5]))
