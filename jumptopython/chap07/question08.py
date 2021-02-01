f1 = open('abc.txt', 'r')
a = f1.readlines()
f1.close()

a.reverse()
f2 = open('abc.txt', 'w')
for i in a:
    f2.write(i)