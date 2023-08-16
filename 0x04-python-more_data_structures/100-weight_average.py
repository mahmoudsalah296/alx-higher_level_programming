#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight_average = 0
    dict_list = dict(my_list)
    for i in dict_list:
        weight_average += (i * dict_list[i])
    weight_average /= sum(dict_list.values())
    return weight_average
