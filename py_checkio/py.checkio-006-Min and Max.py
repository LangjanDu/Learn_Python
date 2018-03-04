#py.checkio-006-Min and Max
#
'''
max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])
Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.

If one positional argument is provided, it should be an iterable. The largest (smallest) item in the 
iterable is returned. If two or more positional arguments are provided, the largest (smallest) of the 
positional arguments is returned.

The optional keyword-only key argument specifies a function of one argument that is used to extract a 
comparison key from each list element (for example, key=str.lower).

If multiple items are maximal (minimal), the function returns the first one encountered.

-- Python Documentation (Built-in Functions)

Input: One positional argument as an iterable or two or more positional arguments. Optional keyword 
argument as a function.

Output: The largest item for the "max" function and the smallest for the "min" function.

    在这个任务中，你应该自己写出PY3中实现的内建函数和一些内建函数在这里是不能用的：
	别忘了，你需要在你的代码中实现两个函数。

	style="font-weight: bold">
    max(iterable, *[, key]) 或者 min(iterable, *[, key])
    max(arg1, arg2, *args[, key]) 或者 min(arg1, arg2, *args[, key])
	
    返回迭代中的最大（最小）项中或者返回根据所提供参数的最大（最小）值 。
    如果有一个参数时，它应该是一个迭代器。返回在迭代器的最大（最小）的项。如果提供两个或更多的参数，返回参数中的最大（最小）的项。 
    可选的唯一关键字是一个用于从每个列表元素提取一个用于比较的参数的函数。（例如，key=str.lower.lower）
    如果有多个值同是最大（最小）的，函数返回所遇到的第一个最大值。

	输入:
    一个参数作为一个迭代器或两个以上的参数。 
    一个函数作为可选关键字参数。

    输出: "max" 函数输出最大的项  "min" 函数输出最小的项。
'''

#一
#当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值。
#一种达到可变参数 (Variable Argument) 的方法：使用*args和**kwargs语法。
#其中，*args是可变的positional arguments列表，**kwargs是可变的keyword arguments列表。
#并且，*args必须位于**kwargs之前，因为positional arguments必须位于keyword arguments之前。

def min(*args, **kwargs):
    key=kwargs.get('key')
    if len(args)==1:
       result = sorted(args[0], key=key, reverse=False)[0]
    else:
       result = sorted(args, key=key,reverse=False)[0]
    return result
    
def max(*args, **kwargs):
    key = kwargs.get('key')
    if len(args)==1:
        result = sorted(args[0], key=key, reverse=True)[0]
    else:
        result = sorted(args,key=key, reverse=True)[0]
    return result
print(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))

# #二
# def available(args,key,reverse):
    # if len(args) == 1:
        # args = [arg for arg in args[0]]
    # return sorted(args,key=key,reverse=reverse)[0]

# def min(*args, key=lambda x:x):
    # return available(args,key,False)

# def max(*args, key=lambda x:x):
    # return available(args,key,True)
# print(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))