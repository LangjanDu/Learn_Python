#py.checkio-005-All the Same
#
'''
In this mission you should check if all 
elements in the given list are equal.

Input: List.

Output: Bool.
'''

#一

from collections import Counter

def all_the_same(list):
	return True if len(dict(Counter(list))) < 2 else False

print(all_the_same(list=[1,1,1]))


#二
# from typing import List, Any

# def all_the_same(elements: List[Any]) -> bool:
    # return True if len(set(elements)) <= 1 else False #set,去重复
# print(all_the_same([1, 1, 1]))