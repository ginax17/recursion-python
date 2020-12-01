import itertools
from itertools import combinations_with_replacement

def find_min(element):
    # element = [3,6,8,9,3,11]
    if len(element) == 0:
        return -1

    if not str(element[0]).isdigit() and '-' not in str(element[0]):
        return -1

    if len(element) == 1: #check the indexes in elements and counts how long element is
        return element[0]  #returns the element at index zero
    if element[0] > element[1]:
        element.pop(0)
        return find_min(element)#find min is called each time to slice the list time with each call
    else:
        element.pop(1)
        return find_min(element)

def sum_all(element):
    if len(element) == 0:
        return -1

    elif not str(element[0]).isdigit() and '-' not in str(element[0]):
        return -1 
    elif len(element) == 1: #this is the escape clause in the sum function 
        return element[0]
    else:
        return element[0] + sum_all(element[1:])

def all_possible_strings(character_strings,prefix,number_elements,combination_length): 
    string_list = []
    if combination_length == 0: #base print(prefix) return
        # print(prefix)
        return [prefix]

    for x in range(number_elements):
        new_prefix = prefix + character_strings[x] 
        string_list += all_possible_strings(character_strings,new_prefix,number_elements,combination_length-1)
    
    return string_list
def find_possible_strings(character_strings,combination_length):
    if len(character_strings) == 0:
        return []

    if str(character_strings[0]).isdigit():
        return []
    else:
        return all_possible_strings(character_strings, "",len(character_strings),combination_length)
    
       
print(find_min([3,4,5]))
print(sum_all(['a',100,'b',4,-5]))
print(sum_all([-2,-2,-2,-2]))
print(find_possible_strings('ab',3))
# print(find_possible_strings(['a','b'],2))

