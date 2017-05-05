# Python学习笔记

## 部分转义序列

>\\\            反斜杠(\\)
>
>\\'            单引号(')
>
>\\"            双引号(")
>
>\\a            ASCII响铃符(BEL)
>
>\\b            ASCII退格符(BS)
>
>\\f            ASCII进纸符(FF)
>
>\\n            ASCII换行符(LF)
>
>\\N{name}      Unicode数据库的字符名，其中name是它的名字，仅适用Unicode
>
>\\r            ASCII回车符(CR)
>
>\\t            ASCII水平制表符(TAB)
>
>\\v            ASCII垂直制表符(VT)
>
>\\ooo          值为八进制值ooo的字符

## input()函数手动类型转换

>代码例子：
>
>```python
>print("please input str1:")
>str1 = input()
>print("str2:")
>str2 = input()
>print("str1 + str2 = %s" % (str1+str2))
>
>print("please input number a1:")
>a1 = int(input())
>print("a2:")
>a2 = int(input())
>print("a1 + a2 = %d" % (a1+a2))
>```
>
>结果为：
>
>```
>str1 + str2 = 1111
>please input str1:
>11
>str2:
>11
>str1 + str2 = 1111
>please input number a1:
>11
>a2:
>11
>a1 + a2 = 22
>```
>

## argv用法

>创建ex\_9\_get\_argument.py文件
>```python
>from sys import argv
>
>script, first = argv
>
>print("The script is called:", script)
>print("first:", first)
>```
>
>在命令行输入
>
>```powershell
>python ex_9_get_argument.py 1
>```
>
>其中ex\_9\_get\_argument.py，1为参数
>
>显示
>
>```
>The script is called: ex_9_get_argument.py
>first: 1
>```