#checkio-001-house passwor
#
'''
Stephan and Sophia forget about security and use simple passwords for everything. 
Help Nikola develop a password security check module. The password will be 
considered strong enough if its length is greater than or equal to 10 symbols, 
it has at least one digit, as well as containing one uppercase letter and one 
lowercase letter in it. The password contains only ASCII latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type that can be 
converted and processed as a boolean. In the results you will see the converted results.

斯蒂芬和索菲亚对于一切都使用简单的密码，忘记了安全性。请你帮助尼古拉开发一个密码安全检查模块。
如果密码的长度大于或等于10个符号，至少有一个数字，一个大写字母和一个小写字母，该密码将被视为
足够强大。密码只包含ASCII拉丁字母或数字。

输入: 密码 (str, unicode)。

输出: 密码的安全与否，作为布尔值(bool)，或者任何可以转换和处理为布尔值的数据类型。
你会在结果看到转换后的结果(True 或 False)。
'''

#一
import re
def checkio(data):
    r1=re.search(r'[0-9]+', data) #检查密码是否含有数字
    r2=re.search(r'[a-z]+', data) #检查密码是否含有小写字母
    r3=re.search(r'[A-Z]+', data) #检查密码是否含有大写字母
    r4=re.match(r'\w{10,}', data) #检查密码的长度是否大于或等于10个符号
    if bool(r1) and bool(r2) and bool(r3) and bool(r4):
        return True
    else:
        return False
    #replace this for solution
    #return True or False

#Some hints
#Just check all conditions

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

#二
checkio = lambda s: not(
   len(s) < 10 #检查密码的长度是否少于10个符号
   or s.isdigit() #检查密码是否只包含数字
   or s.isalpha() #检查密码是否所有字符都是字母
   or s.islower() #检查密码是否由小写字母组成
   or s.isupper() #检查密码是否由大写字母组成
   )


def checkio(data):
   if len(data) < 10:
       return False
   if data.isdigit() == True:
       return False
   if data.isalpha() == True:
       return False
   if data.islower() == True:
       return False
   if data.isupper() == True:
       return False
   else:
       return True