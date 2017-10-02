def func1():
    print("this is func1()")

def func2(num1,num2):
    print("this is func2()")
    num = num1 + num2
    return num

def func3():
    print("this is func3()")
    renum1 = 100
    renum2 = 1000
    return renum1,renum2

def func4():
    print("this is func4()")
    a,b = func3()
    print(a,b);

def printFile(a):
    print(a.read())

def rewind(a):
    a.seek(0)

func1()

a = 1
b = 3
print("a + b = %r" % func2(a,b))

print(func2("hello ","world"))

a,b=func3()

print("a = %r,b = %r" % (a,b))

func4()

print("please input file name")
filename = input()

file = open(filename,'r',encoding='utf-8')

printFile(file)
print("print %r again" % filename)
rewind(file)
printFile(file)