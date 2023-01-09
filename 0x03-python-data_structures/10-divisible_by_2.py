#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_a = list(my_list)
    for count, i in enumerate(my_list):
        if my_list[i] % 2 == 0:
            list_a[count] = True
        else:
            list_a[count] = False
    return list_a
