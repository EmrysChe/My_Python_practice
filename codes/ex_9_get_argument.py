from sys import argv

script, user = argv

prompt = '> '

print("your computer model:")
model = input(prompt)

print("The script is called:%s" % script)
print("user:%s" % user)
print("your computer model:%s" % model)