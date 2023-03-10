#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = idx = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end='')
                index = index + 1
                idx = idx + 1
            else:
                print()
                return idx
        except (ValueError, TypeError):
            index = index + 1            
