def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    m = -1000
    for i in data:
        if i%2==0:
            if m < i:
                m = i
    
    return m if m!=-1000 else -1
print(find_max_even([1, -14, 1, 1, 9])) 
