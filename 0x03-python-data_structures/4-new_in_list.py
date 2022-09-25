#!/usr/bin/python3
def new_in_list(my_list, idx, elem):
      contx = my_list[:]
    if idx < 0 or idx >= len(contx):
        return contx
    contx[idx] = elem
    return contx
