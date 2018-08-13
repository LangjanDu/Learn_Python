#py.checkio-007-Say Hi
#
'''
In this mission you should write a function that introduce a person with a given parameters in attributes.

Input: Two arguments. String and positive integer.

Output: String.
'''

#一

def say_hi(name, age):
	return "Hi. My name is %s and I'm %d years old"%(name, age)
print(say_hi("Frank", 68))