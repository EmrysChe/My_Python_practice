# 我在学习Python时遇到的Python 2和Python 3的区别

## 一.print()函数

>
>### 1. 基础
>
>在Python 2中“print”为表达式，用法例子：
>
>```python
>   print "hello python"
>   print 'hello python'
>```
>
>在Python 3中“print”为函数，用法例子：
>
>```python
>   print("hello python")
>   print('hello python')
>```
>
>### 2. 更多
>
>在Python 2中可以
>```python
>   str1 = "W"
>   str2 = "h"
>   str3 = "y"
>   str4 = "I"
>   str5 = "did"
>   str6 = "such"
>   str7 = "a"
>   str8 = "silly"
>   str9 = "thing"
>   str0 = " "
>   print str1+str2+str3+str0+str4+str0+str5+str0+str6,
>   print str7+str0+str8+str0+str9
>```
>
>显示为：
>
>       Why I did such a silly thing
>
>但在Python 3中
>
>```python
>   print(str1+str2+str3+str0+str4+str0+str5+str0+str6+str0+str7+str0+str8+str0+str9)
>```
>
>才能显示为这样。如果
>
>```python
>   print(str1+str2+str3+str0+str4+str0+str5+str0+str6),
>   print(str7+str0+str8+str0+str9)
>```
>
>则会显示为：
>
>       Why I did such
>       a silly thing
>
>我不知道Python 3如何解决那么长的一行代码，变成两行后还是效果一样，但谁会那么傻地去写那么长一行代码，至少，实际中很难遇到这样的情况。

## 二.input()函数

>
>在Python 3中，input()函数整合了Python 2中的raw_input()和input()函数，Python 3中的input()函数的返回值类型为字符串，如果想返回数字类型需要手动转换。
>Python 3代码例子：
>
>```python
>   print("please input str1:")
>   str1 = input()
>   print("str2:")
>   str2 = input()
>   print("str1 + str2 = %s" % (str1+str2))
>
>   print("please input number a1:")
>   a1 = int(input())
>   print("a2:")
>   a2 = int(input())
>   print("a1 + a2 = %d" % (a1+a2))
>```
>
>结果为：
>
>       str1 + str2 = 1111
>       please input str1:
>       11
>       str2:
>       11
>       str1 + str2 = 1111
>       please input number a1:
>       11
>       a2:
>       11
>       a1 + a2 = 22
>
>
>在python 2中从控制台接收输入的方式有两种：
>input()和raw_input(),当输入为纯数字时,input返回的是数值类型。
>
>raw_inpout返回的是字符串类型。
>input()会计算在字符串中的数字表达式，而raw_input()不会。
>如输入 “57 + 3”，input会得到整数60，而raw_input会得到字符串”57 + 3”。
>
>“input()会把你输入的东西当作Python代码处理，这么做会有安全问题，你应该避开这个函数”(《“笨方法”学Python》(Zed A.Shaw)习题11)
>至于raw_input()函数手动转换的用法，与Python 3中的input()相同，代码就不做示例了。