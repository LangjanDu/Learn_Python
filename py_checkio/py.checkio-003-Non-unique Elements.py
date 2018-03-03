#py.checkio-003-Non-unique Elements
#
'''
You are given a non-empty list of integers (X). For this task, you should return 
a list consisting of only the non-unique elements in this list. To do so you will 
need to remove all unique elements (elements which are contained in a given list 
only once). When solving this task, do not change the order of the list. 
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

你将得到一个含有整数（X）的非空列表。在这个任务里，你应该返回在此列表中的非唯一元素的列表。
要做到这一点，你需要删除所有独特的元素（这是包含在一个给定的列表只有一次的元素）。
解决这个任务时，不能改变列表的顺序。例如：[1，2，3，1，3] 1和3是非唯一元素，结果将是 [1, 3, 1, 3]

输入: 一个含有整数的列表。

输出: 一个含有不唯一元素的整数列表。
'''

#一

from collections import Counter

data = [1, 2, 3, 2, 5]
#data = ['a', 'b', 'a', 'c', 'b', 'a', 'd']

def checkio(data):

	L1 = list(dict(Counter(data)).keys()) #统计各字符出现的次数，提取词典的key
	L2 = list(dict(Counter(data)).values()) #统计各字符出现的次数，提取词典的value
	L3 = []
	L4 = []
	
	for i in range(len(L2)): #找出出现次数不为一的字符
		if L2[i] != 1:
			L3.append(L1[i])

	for x in data:
		if x in L3:
			L4.append(x)
	print(L4)


#二

# def checkio(data):  
	# new_data = []  
	# for i in data:  
		# if data.count(i) > 1:  
			# new_data.append(i)  
	# print(new_data)

#三

# def checkio(data):  
        # return [i for i in data if data.count(i) > 1] 
#or
#checkio=lambda d:[x for x in d if d.count(x)>1]

checkio(data)