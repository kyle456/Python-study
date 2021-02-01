f1 = open('sample.txt', 'r')
numbers = f1.readlines()
numbers = [int(i.rstrip('\n')) for i in numbers]
f1.close()

f2 = open('result.txt', 'w')
f2.write(str(sum(numbers) / len(numbers)))
f2.close()