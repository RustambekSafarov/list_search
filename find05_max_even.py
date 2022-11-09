def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    if data[0]%2==0:
        m = 0
    for i in data:
        if i%2==0:
            if m < i:
                m = i
    
    return m
print(find_max_even([1, 14, 10, 8, 9]))