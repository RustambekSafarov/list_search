def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    m = data[0]
    for i in data:
        if m < i:
            m = i
    return m
print(find_max([0,2,1,3,6,9]))
    