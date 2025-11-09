def move(my_list, direction=None):
    index_of_one = my_list.index(1)
    if direction == 'right':
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
    elif direction == 'left':
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1
    return my_list
    def move(the_pig_location, direction):
    index_of_one = the_pig_location.index(1)
    if direction == "left":
        if index_of_one > 0:  
            the_pig_location[index_of_one] = 0
            the_pig_location[index_of_one - 1] = 1
    elif direction == "right":
        if index_of_one < len(the_pig_location) - 1: 
            the_pig_location[index_of_one] = 0
            the_pig_location[index_of_one + 1] = 1
    return the_pig_locatio
def move(lst, direction):
    index_of_one = lst.index(1)
    if direction == "right" and index_of_one < len(lst) - 1:
        lst[index_of_one], lst[index_of_one + 1] = lst[index_of_one + 1], lst[index_of_one]
    elif direction == "left" and index_of_one > 0:
        lst[index_of_one], lst[index_of_one - 1] = lst[index_of_one - 1], lst[index_of_one]
    return lst
    
  
