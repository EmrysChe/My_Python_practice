def func1():
    print("this if func1")

def func2(num1,num2):
    num = num1 + num2
    return num
def printFile(a):
    print(a.read())

def rewind(a):
    a.seek(0)

func1()

a = 1
b = 3
print("a + b = %r" % func2(a,b))

print(func2("hello ","world"))

print("please input file name")
filename = input()

file = open(filename,'r',encoding='utf-8')

printFile(file)
print("print %r again" % filename)
rewind(file)
printFile(file)