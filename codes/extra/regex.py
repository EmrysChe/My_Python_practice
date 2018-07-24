import re

my_string = "Let the word change you, then you can change the word."

ARegex = re.compile(r'word|you')
mo = ARegex.search(my_string)
print(mo.group())

BRegex = re.compile(r'change(word)?')
mo = BRegex.search(my_string)
print(mo.group())

CRegex = re.compile(r'(\d\d\d\d-)?\d\d\d\d\d\d\d\d')
phone_num = "a number is 0571-11000110"
mo = CRegex.search(phone_num)
print(mo.group())
phone_num = "a number is 11000110"
mo = CRegex.search(phone_num)
print(mo.group())

DRegex = re.compile(r'Bo(o)+m')
my_string = "Boooooooooooooom!"
mo = DRegex.search(my_string)
print(mo.group())

ERegex = re.compile(r'B(oo)*m')
my_string = "Boooooooooooooom!"
mo = ERegex.search(my_string)
print(mo.group())

FRegex = re.compile(r'B(oo){2}m')
my_string = "Boooom!"
mo = FRegex.search(my_string)
print(mo.group())
