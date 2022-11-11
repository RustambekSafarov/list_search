def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    m = data[0]
    for i in data:
        if m > i:
            m = i

    return m
print(find_min([1, 2, -3, 4, 5]))