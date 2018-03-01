#py.checkio-002-The Most Wanted Letter
#
'''
You are given a text, which contains different english letters and punctuation symbols. 
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your 
search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes 
first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

给你一个其中包含不同的英文字母和标点符号的文本，你要找到其中出现最多的字母，返回的字母必须是小写形式，
当检查最想要的字母时，不区分大小写，所以在你的搜索中 "A" == "a"。 
请确保你不计算标点符号，数字和空格，只计算字母。

如果你找到两个或两个以上的具有相同的频率的字母，
返回那个先出现在字母表中的字母。
例如 -- “one”包含“o”，“n”，“e”每个字母一次，因此我们选择“e”。

输入: 用于分析的文本.

输出: 最常见的字母的小写形式。
'''

#一
import re
from collections import Counter

text = input('Input your text:')
text = sorted(filter(str.isalpha, text.lower())) #转换为小写并去除非字母符号，然后排序
result = Counter(text) #统计各个字母及次数
letter = str(result.most_common(1)) #提取出现次数最高的元素
a = re.sub('[^a-zA-Z]','', letter) #提取出现次数最高的字母

print(a)