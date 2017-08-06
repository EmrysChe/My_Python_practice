from sys import argv

script,filename = argv

print("file name is %r." % filename)

print("Opening the file...")
target = open(filename, 'w+')

print("truncating this file...")
target.truncate()

buf = input("write the words:\n")

target.write(buf)

target.seek(0, 0)
words = target.read()
print("the words in %r is:\n" % filename)
print(words)

target.close()
print("%r is closed\n" % filename)