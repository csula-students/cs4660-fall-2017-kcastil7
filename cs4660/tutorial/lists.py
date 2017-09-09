"""Lists defines simple list related operations"""

def get_first_item(li):
    return li[0]
    pass

def get_last_item(li):
    return li[len(li) - 1]
    pass

def get_second_and_third_items(li):
    """Return second and third item from the list"""
    return li[1:3]

def get_sum(li):
    """Return the sum of the list items"""
    x = 0
    for i in li:
        x = x + i
    return x
    pass

def get_avg(li):
    """Returns the average of the list items"""
    x = 0
    for i in li:
        x = x + i
    return x / len(li)
    pass
