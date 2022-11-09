def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    m = data[0]
    s = 0
    for i in data:
        if m < i:
            m = i
    for i in data:
        
        if m == i:
            s+=1
    return s
print(find_max_count([1, 8, 3, 8, 5]))