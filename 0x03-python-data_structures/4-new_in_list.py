#!/usr/bin/python3
def new_in_list(my_list, idx, elem):
      x = my_list[:]
    if idx < 0 or idx > len(x):
        x[idx] = elem
        return x
    return my_list
