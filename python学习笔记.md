# Python学习笔记

## 部分转义序列

\\\            反斜杠(\\)

\\'            单引号(')

\\"            双引号(")

\\a            ASCII响铃符(BEL)

\\b            ASCII退格符(BS)

\\f            ASCII进纸符(FF)

\\n            ASCII换行符(LF)

\\N{name}      Unicode数据库的字符名，其中name是它的名字，仅适用Unicode

\\r            ASCII回车符(CR)

\\t            ASCII水平制表符(TAB)

\\v            ASCII垂直制表符(VT)

\\ooo          值为八进制值ooo的字符

## input()函数手动类型转换

代码例子：

```python
print("please input str1:")
str1 = input()
print("str2:")
str2 = input()
print("str1 + str2 = %s" % (str1+str2))

print("please input number a1:")
a1 = int(input())
print("a2:")
a2 = int(input())
print("a1 + a2 = %d" % (a1+a2))
```

结果为：

```
str1 + str2 = 1111
please input str1:
11
str2:
11
str1 + str2 = 1111
please input number a1:
11
a2:
11
a1 + a2 = 22
```


## argv用法

创建ex\_9\_get\_argument.py文件
```python
from sys import argv

script, first = argv

print("The script is called:", script)
print("first:", first)
```

在命令行输入

```powershell
python ex_9_get_argument.py 1
```

其中ex\_9\_get\_argument.py，1为参数

显示

```
The script is called: ex_9_get_argument.py
first: 1
```

## print()用法

```python
a = 1
b = 2
print("a =" , a ,",b =" , b)
print("a = %r,b = %r", % (a,b))
print(a,b,a+b)
```

结果为：

```
a = 1,b = 2
a = 1,b = 2
1 2 3
```

## Python类内的变量数据储存问题

### 例子1

```python
class X():
    def __init__(self,J):
        self.J = J
        print("__init__() in class X")
    def My_print_X(self):
        print(self.J)

# A = X(19)
# A.My_print_X()

class Y():
    def __init__(self,J):
        self.J = J
        print("__init__() in class Y")
    def My_print_Y(self):
        print(self.J)

# A = Y(19)
# A.My_print_Y()

class Z(X,Y):
    def __init__(self,J,I):
        print("__init__() in class Z")
        X.__init__(self,J)
        Y.__init__(self,I)

A = Z(19,1)
A.My_print_X()
A.My_print_Y()
```

输出结果为
```
__init__() in class Z
__init__() in class X
__init__() in class Y
1
1
```

### 例子2

```python
class X():
    def __init__(self,J):
        self.J = J
        print("__init__() in class X")
    def My_print_X(self):
        print(self.J)

# A = X(19)
# A.My_print_X()

class Y():
    def __init__(self,I):
        self.I = I
        print("__init__() in class Y")
    def My_print_Y(self):
        print(self.I)

# A = Y(19)
# A.My_print_Y()

class Z(X,Y):
    def __init__(self,J,I):
        print("__init__() in class Z")
        X.__init__(self,J)
        Y.__init__(self,I)

A = Z(19,1)
A.My_print_X()
A.My_print_Y()
```

输出结果为
```
__init__() in class Z
__init__() in class X
__init__() in class Y
19
1
```

我不太清楚Python真正的储存数据的方式，但这两种情况，我直观上感受到的可能为例子1中的X类的J和Y类的J可能用的是同一个储存空间，所以结果都为1，而例子2中X类的J和Y类的I，当然变量名都不一样，空间可能是不一样的。

这样让我有一个大胆的猜测，Python的变量储存空间的申请可能和C++非常不同，在两个不同的类中，相同名字的变量可能用的是同一个空间(我感觉很难受。。。)，当然，这只是猜想，或许实际上可能是另外的机制造成了这个结果。

然而在函数中貌似没有这种情况

```python
def a(num2):
    num1 = num2
    return num1

def b(num1):
    print(num1)
    return num1

num1 = a(2)
b(1)
print(num1)
```

结果为

```
1
2
```

我总感觉Python的多重继承有点怪怪的，可能我前面的推断是错误的，下次得找个大佬问问。。。