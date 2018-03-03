#py.checkio-004-Long Repeat
#
'''
This mission is the first one of the series. Here you should find the length of 
the longest substring that consists of the same letter. For example, line "aaabbcaaaa" 
contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last 
substring is the longest one which makes it an answer.

Input: String.

Output: Int.

这个任务是这个系列中的第一个。在这里你应该找到字符串中最长的相同字符重复出现的次数，
并返回它的重复次数。例如：字符串“aaabbcaaaa”包含具有相同字母“aaa”，“bb”，“c”和“aaaa”的四个子字符串。 
最后一个子字符串是最长的一个字符串，你应该返回 4 。

输入: 一个字符串.

输出: 一个整数. 
'''

#一

line = 'abbcdddfffff'

def long_repeat(line):
	L = len(line)
	count = 1
	output = []
	if L < 2:
		return L
	else:
		for i in range(L-1):
			if line[i] == line[i+1]:
				count += 1
			else:
				count = 1
			output.append(count)
			print(output)
		return max(output)

print(long_repeat(line))


#二

# def long_repeat(line):
    # count = 1
    # maxi = 1
    # if line != "":
        # for i in range(1,len(line)):
            # if line[i] == line[i-1]:
                # count+=1
                # if count > maxi:
                    # maxi = count
            # else:
                # count = 1
        # return maxi
    # else:
        # return 0