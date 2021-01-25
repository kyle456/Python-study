f = open('./jumptopython/chap04/test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('./jumptopython/chap04/test.txt', 'w')
f.write(body)
f.close()